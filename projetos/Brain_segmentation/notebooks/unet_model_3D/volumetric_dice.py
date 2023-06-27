import sys
def vol_dice(volume_saida, volume_mask):
    '''
    Calculate DICE of volume
    '''
    #iflat = volume_saida.contiguous().view(-1).cuda() # para 2d
    iflat = volume_saida.contiguous().view(-1)
    tflat = volume_mask.contiguous().view(-1)
    intersection = (iflat * tflat).sum()
    
    eps = sys.float_info.epsilon

    iflat_sum = iflat.sum()
    tflat_sum = tflat.sum()

    dice = (2. * intersection) / (iflat_sum + tflat_sum + eps)

    value = dice.item()

    return value

