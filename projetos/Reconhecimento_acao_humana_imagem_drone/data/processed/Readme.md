### Dados finais usados para a modelagem

Seis conjunto de dados foram adotados no treinamento do modelo:
- Imagens RGB (pasta "Dados_filtrados"), filtradas do conjunto original do dataset "NTUT 4K Drone Photo Dataset for Human Detection". Conjunto completo disponível em: <https://drive.google.com/drive/folders/1whsJovK-29ZBCNZhqMQ-Ihot55qsegCe?usp=sharing>;
- Imagens em níveis de cinza (pasta "NC") definidas após a filtragem dos dados originais em função dos labels "walk", "riding", "sit" e "stand". Conjunto completo disponível em: <https://drive.google.com/drive/folders/1-0ampfZunDklLZBQg2RVy9EQ9BAnzFJ7?usp=share_link>;
- Imagens resultantes da filtragem espacial adotando o Filtro de Sobel (pasta "Filtro_Sobel"), definidas após a filtragem dos dados originais em função dos labels "walk", "riding", "sit" e "stand". Conjunto completo disponível em: <https://drive.google.com/drive/folders/1tNVJLCYaUojwDgW0lghAYnrlVFRyueSj?usp=sharing>;
- Imagens resultantes da filtragem espacial adotando o Filtro de Prewitt (pasta "Filtro_Prewitt"), definidas após a filtragem dos dados originais em função dos labels "walk", "riding", "sit" e "stand". Conjunto completo disponível em: <https://drive.google.com/drive/folders/1t1M_E_MC0-GXDTVXmc7rqrvA84rdOYvX?usp=sharing>;
- Imagens em níveis de cinza definidas após o balanceamento dos dados (pasta "NC_balanceado"), excluindo imagens em que somente a pose "walk" fosse detectada. Conjunto completo disponível em: <https://drive.google.com/drive/folders/1H921k0ksIbwOe_WDKUKSqmEYq5EzjuLs?usp=sharing>;
- Imagens em níveis de cinza correspondentes aos dados filtrados somados os dados aumentados a partir das técnicas de aumentação dos dados (pasta "NC_augmentation"). Conjunto completo disponível em: <https://drive.google.com/drive/folders/1c4LA8X00-Nvp_lqsKgqVHrjYE6XTdgQt?usp=sharing>.
  
As pastas anexas apresentam um conjunto ilustrativo das imagens de cada um desses conjuntos de dados, juntamente com seus arquivos de labels.

**Nota:** o conjunto de imagens RBG (pasta "Dados_filtrados") está incluída tanto nos dados intermediários (pasta "/data/interim/") quanto aqui nos dados finais adotados para modelagem. Isso porque esses dados foram adotados tanto como dados intermediários para geração de outros dados finais apresentados nesse sub-item (NC, Filtro_Sobel, Filtro_Prewitt e NC_augmentation), quanto um para a modelagem final (também adotou-se as imagens RGB - filtradas dos dados originais - para treinamento do modelo). 
