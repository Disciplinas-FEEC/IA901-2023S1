'''
Modified from Livia code
'''
import numpy as np
import SimpleITK as sitk
from math import nan
from typing import List, Dict
from collections import defaultdict
import nibabel as nib
import torch
import os
from post_processed import get_post_processed_cc3d
from monai.inferers import sliding_window_inference

import dipy
import  dipy.io.peaks
    

def initialize_metrics_dict():
    '''
    Initializes an empty metrics dict to be given to seg_metrics
    '''
    return defaultdict(lambda: defaultdict(list))


def seg_metrics(gts: np.ndarray, preds: np.ndarray, metrics: Dict[str, Dict[str, List[float]]], struct_names=["bg", "healthy", "unhealthy"]):
    '''
    finds overlap and distance measures of two given segmentations.
    "Overlap measures: Dice, FNError, FPError, jaccard, Volume Similarity (SimpleITK) and Volume Similarity(Taha et al)
    "Distance measures: Hausdorff distance and average hausdorff distance
    '''
    assert (len(gts.shape) == len(preds.shape) and 
            isinstance(gts, np.ndarray) and isinstance(preds, np.ndarray) and gts.dtype == np.uint8 and preds.dtype == np.uint8 and
            (gts >= 0).all() and (gts <= 1).all() and (preds <= 1).all() and (preds >= 0).all()), "Malformed input for seg_metrics"
    
    for gt, pred, str_label in zip(gts, preds, struct_names):
        hausdorff_distance_filter = sitk.HausdorffDistanceImageFilter()
        overlap_measures_filter = sitk.LabelOverlapMeasuresImageFilter()
        
        img_gt_sitk = sitk.GetImageFromArray(gt)
        img_pred_sitk = sitk.GetImageFromArray(pred)
        
        overlap_measures_filter.Execute(img_pred_sitk, img_gt_sitk)
        
        metrics[str_label]["dice"].append(overlap_measures_filter.GetDiceCoefficient())
        metrics[str_label]["false_negative_error"].append(overlap_measures_filter.GetFalseNegativeError())
        metrics[str_label]["false_positive_error"].append(overlap_measures_filter.GetFalsePositiveError())
        metrics[str_label]["jaccard"].append(overlap_measures_filter.GetJaccardCoefficient())
        metrics[str_label]["volume_similarity"].append(overlap_measures_filter.GetVolumeSimilarity())
        metrics[str_label]["abs_volume_similarity"].append(1-abs(overlap_measures_filter.GetVolumeSimilarity())/2)
        
        try:
            hausdorff_distance_filter.Execute(img_pred_sitk, img_gt_sitk)    
            metrics[str_label]["avg_hd"].append(hausdorff_distance_filter.GetAverageHausdorffDistance())
            metrics[str_label]["hd"].append(hausdorff_distance_filter.GetHausdorffDistance())
        except:
            metrics[str_label]["avg_hd"].append(nan)
            metrics[str_label]["hd"].append(nan)

def get_metrics(model, data_paths):
	device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



	#vol_file = "FreeSurfer/brain-in-rawavg.nii.gz"
	#mask_file = "manual_mask_T1space.nii.gz"

	vol_file = "iso_brain_T1w.nii.gz"
	mask_file = "iso_brainmask_T1w.nii.gz"

	metrics = initialize_metrics_dict()
	with torch.no_grad():
		#dice_per_subject = {}
		Dice_per_subject = {}
		avg_HD_per_subject = {}
		SVA_per_subject = {}
		for data_path in data_paths:
			patient_id = os.path.basename(data_path)
			vol_path = os.path.join(data_path, vol_file)
			vol_data = nib.load(vol_path).get_fdata().astype(np.float32)
			vol_data_affine = nib.load(vol_path).affine
			vol_data = (vol_data - vol_data.mean()) / (vol_data.std())

			vol_data = (vol_data - vol_data.min()) / (vol_data.max() - vol_data.min())

			vol_data = (vol_data*2) - 1
			print(vol_data.max(), vol_data.min())
			mask_path = os.path.join(data_path, mask_file)
			mask_data = nib.load(mask_path).get_fdata()#.astype(np.uint8)
			vol_data = torch.from_numpy(vol_data).unsqueeze(0).unsqueeze(0)
			mask_data = torch.from_numpy(mask_data)

			test_outputs = sliding_window_inference(
				vol_data,
				roi_size=(102, 102, 102), #(112, 160, 56), #(128, 192, 56),# (112, 160, 56), #(128, 192, 56), #
				sw_batch_size=1, 
				predictor=model,
				overlap=0.1,
				mode="gaussian",
				device=torch.device(device)
			)

			#dipy.io.peaks.save_nifti(os.path.join(data_path, "mask.nii.gz"), mask_data.numpy(), vol_data_affine, hdr = None )
			
			vol_data = vol_data.cpu()
			mask_data_save = mask_data.cpu()
			#mask_data_save = mask_data.cpu()
			mask_data = mask_data.cpu().unsqueeze(0)
			test_outputs = test_outputs.cpu().squeeze().detach()
			vol_data = vol_data.cpu().squeeze().detach()


			test_outputs = (test_outputs > 0.6).float()#.unsqueeze(0)
			pos_process_save = get_post_processed_cc3d(test_outputs)
			
			#dipy.io.peaks.save_nifti(os.path.join(data_path, "output.nii.gz"), pos_process_save.numpy(), vol_data_affine, hdr = None )

			

			pos_process = pos_process_save.unsqueeze(0)

			#dipy.io.peaks.save_nifti(os.path.join(data_path, "teste_t1_output.nii.gz"), pos_process_save.numpy().astype(np.uint8), vol_data_affine, hdr = None )
			#dipy.io.peaks.save_nifti(os.path.join(data_path, "teste_t1_mask.nii.gz"), mask_data_save.numpy().astype(np.uint8), vol_data_affine, hdr = None )

			#metrics = initialize_metrics_dict()
			seg_metrics(gts=mask_data.numpy().astype(np.uint8), preds=pos_process.numpy().astype(np.uint8), metrics=metrics, struct_names=["brain"])

			avg = list(metrics["brain"]["avg_hd"])
			avg_HD_per_subject[os.path.basename(data_path)] = list(metrics["brain"]["avg_hd"])
		
			Dice_per_subject[os.path.basename(data_path)] = list(metrics["brain"]["dice"])
			SVA_per_subject[os.path.basename(data_path)] = list(metrics["brain"]["abs_volume_similarity"])
	
			
	return metrics, vol_data, mask_data, avg_HD_per_subject, avg, Dice_per_subject, SVA_per_subject, vol_data, mask_data_save, pos_process, vol_data_affine

