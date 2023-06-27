import torch
from volumetric_dice import vol_dice
from monai.inferers import sliding_window_inference
import nibabel as nib
import numpy as np
from unet_module import LightningMRICCv2
import dipy
from dipy.io.peaks import save_nifti
import glob
import os
from tqdm import tqdm

from post_processed import get_post_processed_cc3d

def predict_brain_model(model, data_paths):
	device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  

	vol_file = "iso_brain_T1w.nii.gz"
	mask_file = "iso_brainmask_T1w.nii.gz"

	with torch.no_grad():
		dice_per_subject = {}
		dice_per_subject_pos = {}
		for data_path in tqdm(data_paths):
			vol_path = os.path.join(data_path, vol_file)
			vol_data = nib.load(vol_path).get_fdata().astype(np.float32)
			vol_data_affine = nib.load(vol_path).affine
			vol_data = (vol_data - vol_data.min()) / (vol_data.max() - vol_data.min())
			mask_path = os.path.join(data_path, mask_file)
			mask_data = nib.load(mask_path).get_fdata().astype(np.uint8)
			vol_data = torch.from_numpy(vol_data).unsqueeze(0).unsqueeze(0)
			mask_data = torch.from_numpy(mask_data)

			# Apply sliding inference over ROI size
			test_outputs = sliding_window_inference(
				vol_data,
				roi_size=(102, 102, 102), # (112, 160, 56)
				sw_batch_size=1, 
				predictor=model,
				overlap=0.1,
				mode="gaussian",
				device=torch.device(device)
			)
			vol_data = vol_data.cpu()
			mask_data = mask_data.cpu()
			test_outputs = test_outputs.cpu().squeeze().detach()

			test_outputs = (test_outputs > 0.5).float()

			dice = vol_dice(test_outputs.cpu(), mask_data.cpu())

			dice_per_subject[os.path.basename(data_path)] = dice

			dice_mean = np.array([dice for _, dice in dice_per_subject.items()]).mean()

			pos_process = get_post_processed_cc3d(test_outputs)
       
			dice_pos = vol_dice(pos_process, mask_data.cpu())
			dice_per_subject_pos[os.path.basename(data_path)] = dice_pos
			dice_mean_pos = np.array([dice_pos for _, dice_pos in dice_per_subject_pos.items()]).mean()

			test_outputs_save = test_outputs.numpy()

			dipy.io.peaks.save_nifti(os.path.join(data_path, "t1_output.nii.gz"), pos_process.numpy().astype(np.uint8), vol_data_affine, hdr = None )

	return vol_data, mask_data, test_outputs, dice_mean, dice_per_subject, pos_process, dice_mean_pos, dice_per_subject_pos, vol_data_affine, test_outputs_save