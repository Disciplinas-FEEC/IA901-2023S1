import pytorch_lightning as pl

from torch.utils.data import  DataLoader

from segmentationtransform import get_transform
from datasetmri import DatasetMRI

class MRICCDataModule(pl.LightningDataModule):
    '''
    O datamodule organiza o carregamento de dados
    ''' 
    def __init__(self, hparams):
        super().__init__()
        self.save_hyperparameters(hparams)

    def setup(self, stage=None):
        '''
        Definição dos datasets de treino validação e teste e das transformadas.
        '''
        train_transform = get_transform(self.hparams.train_transform_str, self.hparams.patch_size)
        eval_transform = get_transform(self.hparams.eval_transform_str, self.hparams.patch_size)

        self.train = DatasetMRI("train", folder=self.hparams.data_folder, mid_slices_only=self.hparams.mid_slices_only, transform=train_transform)
        self.val = DatasetMRI("val", folder=self.hparams.data_folder, mid_slices_only=self.hparams.mid_slices_only, transform=eval_transform)

    def train_dataloader(self):
        return DataLoader(self.train, batch_size=self.hparams.batch_size_train, num_workers=self.hparams.nworkers, shuffle=True)

    def val_dataloader(self):
        return DataLoader(self.val, batch_size=self.hparams.batch_size_val, num_workers=self.hparams.nworkers, shuffle=False)
        