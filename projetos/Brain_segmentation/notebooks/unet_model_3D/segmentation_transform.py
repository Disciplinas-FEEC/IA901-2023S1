from torchvision import transforms
from torchvision.transforms import Lambda, ToTensor
import torch
import random
import numpy as np

from return_patch import ReturnPatch
import torchio as tio


class SegmentationTransform():
    '''
    Applies a torchvision transform into image and segmentation target
    '''
    def __init__(self, transform, target_transform):
        self.transform = transform
        self.target_transform = target_transform
    
    def __call__(self, image, seg_image):
        '''
        Precisa-se fixar a seed para mesma transformada ser aplicada
        tanto na máscara quanto na imagem. 
        '''
        # Gerar uma seed aleatória
        seed = np.random.randint(2147483647)

        # Fixar seed e aplicar transformada na imagem
        random.seed(seed) 
        torch.manual_seed(seed) 
        if self.transform is not None:
            image = self.transform(image)
            
        # # Fixar seed e aplicar transformada na máscara
        random.seed(seed) 
        torch.manual_seed(seed) 
        if self.target_transform is not None:
            seg_image = self.target_transform(seg_image)
        
        #if self.transform is not None:
        #    seg_image = seg_image.numpy()
        #    image, seg_image = self.transform(image, seg_image)

        return image, seg_image
    
    def __str__(self):
        return f"SegmentationTransform: {self.transform}/{self.target_transform}"
        
def get_transform(string): 
    '''
    Mapeamento de uma string a uma transformadas.
    '''
    if string is None:
        image_transform = None
        target_transform = None
#    elif string == 'RAffine':
            #subject = tio.Subject(image=tio.ScalarImage(tensor = image))
#        image_transform = tio.transforms.Compose([tio.transforms.RandomAffine(scales=(0.9, 1.2), degrees=90)])
 #       target_transform = tio.transforms.Compose([tio.transforms.RandomAffine(scales=(0.9, 1.2), degrees=90)])    

    elif string == "RandomCrop":
        return ReturnPatch(None, (102, 102, 102), fullrandom=True)
    elif string == "FocusedCrop_0333":
        return ReturnPatch(0.333, (96, 64, 96))
    else:
        raise ValueError(f"{string} does not correspond to a transform.")
    
    return SegmentationTransform(image_transform, target_transform)
