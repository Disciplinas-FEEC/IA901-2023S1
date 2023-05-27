import pytorch_lightning as pl
from dice_score import dice_coeff
from unet import UNet
from torch.optim import Adam 


class LightningMRICCv2(pl.LightningModule):
    '''
    Essa classe define o que é feito durante o treino. o que acontece com um batch retornado pelo Dataloader.
    Note como todo o código depende dos valores no dicionário de hiperparâmetros.
    '''
    def __init__(self, hparams):
        '''
        Método obrigatório
        

        Aqui define-se o modelo que vai ser treinado, além de guardar os hparams.
        '''
        super().__init__()

        self.save_hyperparameters(hparams)

        # Segmentação usa uma UNet
        self.model = UNet(n_channels=self.hparams.nin, n_classes=self.hparams.snout, norm=True, dim='2d', init_channel=64)                          

    def forward(self, x):
        '''
        Método obrigatório
        '''
        return self.model(x).sigmoid()

    def segmentation_step(self, mode, batch):
        '''
        Passo de segmentação, tanto para treino quanto validação
        '''
        x, y = batch["image"].float(), batch["seg_image"].float()
        y_hat = self.forward(x)
        loss = 1 - dice_coeff(y_hat, y)
        val_dice = dice_coeff((y_hat > 0.5).float(), y)

        if mode == "train":
            self.log("loss", loss, on_epoch=True, on_step=True)
            #self.log("dice", val_dice, on_epoch=True, on_step=True)

            # Para treino é obrigatório retornar a loss
            return loss
        elif mode == "val":
            self.log("val_loss", loss, on_epoch=True, on_step=False, prog_bar=True)           
            self.log("val_dice", val_dice, on_epoch=True, on_step=False, prog_bar=True)

    def training_step(self, train_batch, batch_idx):
        '''
        Método obrigatório
        Passo de treino
        '''
        return self.segmentation_step("train", train_batch)

    def validation_step(self, val_batch, batch_idx):
        '''
        Método obrigatório
        Passo de validação
        '''
        self.segmentation_step("val", val_batch)

    def configure_optimizers(self):
        '''
        Método obrigatório
        Configuração dos otimizadores
        '''
        optimizer = Adam(self.model.parameters(), lr=self.hparams.lr)

        return optimizer
