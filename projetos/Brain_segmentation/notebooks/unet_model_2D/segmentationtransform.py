from torchvision import transforms
from torchvision.transforms import Lambda, ToTensor
import torch
import random
import numpy as np



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
            
        # Fixar seed e aplicar transformada na máscara
        random.seed(seed) 
        torch.manual_seed(seed) 
        if self.target_transform is not None:
            seg_image = self.target_transform(seg_image)

        return image, seg_image
    
    def __str__(self):
        return f"SegmentationTransform: {self.transform}/{self.target_transform}"
        
def get_transform(string, patch_size=(120,56)):
    '''
    Mapeamento de uma string a uma transformadas.
    '''
    if string is None:
        image_transform = None
        target_transform = None    
    elif string == "RandomCrop":
        image_transform = transforms.Compose([transforms.ToPILImage(),
                                              transforms.RandomCrop((patch_size)),
                                              transforms.ToTensor()
                                             ])
        
        target_transform = transforms.Compose([transforms.ToPILImage(),
                                               transforms.RandomCrop((patch_size)),
                                               transforms.ToTensor()
                                             ])   
        
    else:
        raise ValueError(f"{string} does not correspond to a transform.")
    
    return SegmentationTransform(image_transform, target_transform)
