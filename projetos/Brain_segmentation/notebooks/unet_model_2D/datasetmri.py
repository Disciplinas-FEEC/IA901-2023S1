import os
import numpy as np
import torch
from glob import iglob
from torch.utils.data import Dataset


MODES = ["train", "val"]


class DatasetMRI(Dataset):
    '''
    A herança da classe Dataset definida pelo torch garante compatibilidade 
    com utilidades de dataset implementadas pelo torch.
    '''
    def __init__(self, mode, folder, transform=None, debug=False, mid_slices_only=False):
        '''
        mode: train, val or test
        folder: pasta em que as imagens estão
        transform: transformadas a serem aplicadas nas imagens
        '''
        self.folder = folder
        self.transform = transform
        self.debug = debug
        self.mid_slices_only = mid_slices_only

        # Encontrar todas as imagens no path fornecido e indexalas por modo de treinamento
        mid_images = sorted(list(iglob(os.path.join(folder, mode, "**", "*DD.npz"), 
                                recursive=True)))

        if self.mid_slices_only:
            self.dataset = mid_images
        else:
            self.dataset = mid_images
        
        print(f"{mode} DatasetMRI. Localização das Imagens: {self.folder}. Transforms: {self.transform}. dataset fatias do meio: {self.mid_slices_only}")
        
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
        if dirname in ["Brain_projeto_IA901A_2D"]:
            image = torch.from_numpy(npz["data"])
            seg_image = torch.from_numpy(npz["mask"]).float()
            image, seg_image = image.unsqueeze(0), seg_image.unsqueeze(0)
        else:
            raise ValueError(f"self.folder {dirname} errado")

        if self.transform is not None:
            image, seg_image = self.transform(image, seg_image)

        return_dict = {"image": image, "seg_image": seg_image}

        return return_dict

