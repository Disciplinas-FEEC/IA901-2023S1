import os
import numpy as np
import torch
from glob import iglob
from torch.utils.data import Dataset
import torchio as tio


MODES = ["train", "val"]


class DatasetMRI(Dataset):
    '''
    A herança da classe Dataset definida pelo torch garante compatibilidade 
    com utilidades de dataset implementadas pelo torch.
    '''
    def __init__(self, mode, folder, transform=None, debug=False):
        '''
        mode: train, val or test
        folder: pasta em que as imagens estão
        transform: transformadas a serem aplicadas nas imagens
        '''
        self.folder = folder
        self.transform = transform
        self.debug = debug
        
        all_images = sorted(list(iglob(os.path.join(folder, mode, "**", "*.npz"), recursive=True)))        

        self.dataset = all_images
        print('Tamanho do Datset:',len(self.dataset))

        print(f"{mode} DatasetMRI. Localização das Imagens: {self.folder}. Transforms: {self.transform}")
        
    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, i):
        '''
        Pega informações indexadas na posição 'i' e faz o trabalho de conversões 
        e transformadas, retornando os dados prontos para treino.
        '''
        # Carregando dados do .npz como tensores torch 
        npz_file = self.dataset[i]
        npz = np.load(npz_file)

        dirname = os.path.basename(self.folder)

        if dirname in ["dataset_no_preprocessing", "Dataset_HCManualCCexp", "Dataset_HCexpCC"]:
            image = npz["data"][:]
            image = image.astype(np.float32)
            seg_image = npz["mask"].astype(np.float32)
            image = np.expand_dims(image, 0)
            seg_image = np.expand_dims(seg_image, 0)


        else:
            raise ValueError(f"self.folder {dirname} errado")

        if self.transform is not None:
            image, seg_image = self.transform(image, seg_image)

        return_dict = {"image": image, "seg_image": seg_image}

        return return_dict

