# `Segmentação do cérebro usando imagens T1`
# `Brain Segmentation on T1 images`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*, oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> |Nome  | RA | Curso|
> |--|--|--|
> | Jimi Togni           | 226359   | Doutorado em Engenharia Elétrica |
> | Joany Rodrigues      | 264440   | Mestrado em Engenharia Elétrica  |
> | Victor Praxedes Rael | 240242   | Mestrado em Engenharia Elétrica  |

## Descrição do Projeto

Muitos desafios na área de imagem médica exigem como pré-processamento a segmentação do cérebro, por exemplo, a realização de registro e segmentação de estruturas cerebrais. Muitas propostas tem surgindo para solucionar este problema, o que já tem boas propostas na literatura, por exemplo, o trabalho por [LUCENA, Oeslle et al.](https://ieeexplore.ieee.org/abstract/document/8363766?casa_token=Y9VwrDbJQJ8AAAAA:7MsKQIPK9IAl2PD8zla2eRkO2jNtqUilIMtqGjEBGlRb_P9SNNJkXwgJR91otfmY_wGeJSfhGJg). 

Tem surgido propostas na literatura mostrando que ao aplicar técnicas de pré-processamento e aumento de dados pode ser mais vantajoso do que apenas usar técnicas de última geração. Por exemplo, a implementação do framework [nnU-Net](https://www.nature.com/articles/s41592-020-01008-z), que busca o melhor pré-processamento de um conjunto de dados e hiperparâmetros da rede para este conjunto de dados, automaticamente. O objetivo deste framework é usar a arquitetura de uma CNN simples [U-Net](https://link.springer.com/chapter/10.1007/978-3-319-24574-4_28) para buscar de maneira autônoma o melhor modelo de segmentação de objetos de acordo com as características dos dados. Logo, este framework foi executado com o objetivo de adquirir os pré-processamentos dos conjuntos de dados usados neste trabalho e usar como ponto de partida para o treinamento 3D deste projeto.

Logo, o objetivo deste projeto é usar partes de um conjunto de dados de segmentação do cérebro para executar um experimento na nnU-Net e obter suas sugestões de pŕe-processamento de dados e parâmetros da rede para estudá-los e definir os mais intuitivéis e factíveis, para em seguida, desenvolver um método de segmentação do cérebro usando uma versão da arquitetura U-Net. Este estudo incluí averiguar quais dos pré-processamentos dos dados são viáveis para a melhoria de um modelo de segmentação do cérebro.

# Metodologia
## Arquitetura U-Net
Este trabalho utilizará a arquitetura [U-Net](https://link.springer.com/chapter/10.1007/978-3-319-24574-4_28), uma rede neural convolucional bastante utilizada para segmentação de imagens médicas. Utilizaremos as versões 2D e 3D da [U-Net modificada](https://link.springer.com/chapter/10.1007/978-3-030-72084-1_38), conforme implementado por Carmo et al. (2020). 

![U-Net modificada: a resolução espacial é reduzida pela segunda convolução de cada nível do codificador; os blocos
verde se referem as características filtradas pela operação de self attention; cada nível do codificador e decodificador (blocos de duas convoluções) possui
conexão residual realizando a conexão da entrada da primeira convolução à saída da segunda convolução (seta em laranja).](/home/joany/IA901-2023S1/projetos/Brain_segmentation/assets/Unet-IA901A.png)

Mudaças da U-Net modificada para a original incluí: a utilização de convoluções stride para a redução da resolução espacial em vez de operações de agregação; adição de [conexão residual](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html) propagando a entrada à saída de cada nível do codificador (utilizando soma e uma convolução com kernel de 1 × 1 (seta laranja) realizando adaptação de canal e resolução espacial e adição de uma operação [self attention](http://proceedings.mlr.press/v102/gorriz19a.html) para filtrar as características produzidas em cada nível do codificador.

Modificações entre as versões 2D e 3D inclui: o número de canais de entrada para a versão 3D é reduzido devido ao aumento da dimensionalidade da variante 3D, uma vez que cada volume é considerado um canal, enquanto para a versão 2D cada fatia de um volume é considerado um canal; utilização de normalização de instância para a versão 3D, comumente usada em redes convolucionais 3D com batch pequeno e a normalização em lote para a versão 2D, pois o tamanho do batch é consideravelmente maior e costuma funcionar bem neste caso quando utiliza convoluções 2D.

## Pré-Processamento de dados
### nnU-Net 
Os dados foram executados no framework nnU-Net apenas para obtermos sugestões de pré-processamento dos dodos e parâmetros da rede. Para a execusão dos dados na nnU-Net, foi necessário organizar os dados da forma que esta exige. A implementação usada para organização no conjunto de dados usados neste trabalho pode ser encontrado no notebook xxxxx, para mais informações acesse o tutorial do framework. 

Ao executarmos os dados na nnU-Unet, esta forneceu um problema nos dados, pois este framework não aceita labels que não sejam numéros inteiros. Isso foi importante para sabermos que as segmentações dos dados não estavam binarizadas. Isso foi corrigido para execução da nnU-Net usando o código presente também no notebook xxxx.

Após a execução da nnU-Net, foram obtidos uma lista de pré-processamento para o treinamento deste dados 3D e 2D. A partir dessas listas, consideramos os seguintes pré-processamentos para o treinamento das duas versões da arquitetura U-Net (2D e 3D).

### Definição de Pré-processamentos
Após a realização do treinamento da nnU-Net, obtivemos os pré-processamentos sugeridos para este framework de ambas as versões (2D e 3D). Ao avlaiar esses pré-processamentos, optamos por utilizar os seguites pré-processamentos para a realização de experimentos neste trabalho: rotação: angle_x = (-0.5235987755982988, 0.5235987755982988), ângulo_y = (-0.5235987755982988, 0.5235987755982988), ângulo_z = (-0.5235987755982988, 0.5235987755982988); GaussianNoiseTransform(p_per_sample = 0.1, data_key = 'data', noise_variance = (0, 0.1), p_per_channel = 1, per_channel = False ); GaussianBlurTransform( p_per_sample = 0.2, different_sigma_per_channel = True, p_per_channel = 0.5, data_key = 'data', blur_sigma = (0.5, 1.0), different_sigma_per_axis = False, p_isotropic = 0 ); ContrastAugmentationTransform( p_per_sample = 0.15, data_key = 'data', contrast_range = (0.75, 1.25), preserve_range = True, per_channel = True, p_per_channel = 1 ); GammaTransform( p_per_sample = 0.1, retain_stats = True, per_channel = True, data_key = 'data', gamma_range = (0.7, 1.5), invert_image = True ); 'spacing': [1.0, 0.9999008178710938, 1.0].

#### Definição de pré-processamento da U-Net 2D
COLOCAR AQUI O QUE FOR DEFINIDO A PARTIR DA NNUNET.

### Treinamento da arquiterura 3D
O treinamento do modelo 3D foi realizado ao utilizar o volume de entrada para obter patches 3D que serçao usados como canal de entrada da U-Net 3D. A rede realiza o treinamento e retorna como saída a segmentação do cérebro.  

Dedicir onde incluir isso: 'batch_size': 2;  patch_size = [128, 128, 128]


## Bases de Dados e Evolução

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
LBPA40 | https://www.loni.usc.edu/research/atlas_downloads | conjunto de dados com atlas baseado em ressonância magnética da anatomia do cérebro, gerado por registro não rígido sem modelo a partir de imagens de 24 indivíduos de controle normais.
CC359 | https://portal.conp.ca/dataset?id=projects/calgary-campinas | conjunto de dados de ressonância magnética cerebral Calgary Campinas, composto por imagens de RM do cérebro ponderadas em T1 e máscaras de segmentação do cérebro.
NFBS | http://preprocessed-connectomes-project.org/NFB_skullstripped/ | é um dataset com 125 ressonâncias magnéticas anatômicas ponderadas em T1 que tem anotações manuais do cérebro. Este conjunto de dados fornece 3 arquivos para cada sujeito: Structural T1-weighted anonymized image, Skull-stripped image, Brain mask.
IBSR | https://www.nitrc.org/projects/ibsr | repositório de Segmentação Cerebral da Internet (IBSR) fornece anotações manuais, juntamente com dados de imagem cerebral por ressonância magnética em T1.

> * Todos os datasets originais (baixados) estão no formato nifti.
> * Foi feita automaticamente a organização dos dados em pastas para cada sujeito.
> * A base de dados IBSR veio com desalinhamento entre a imagem e a máscara.
> * Para o treinamento da nn-Unet, foi preciso organizar os dados da maneira que o framework exige, consulte (https://github.com/MIC-DKFZ/nnUNet/tree/master). Em seguida, as anotações foram binarizadas usando limiarização de 0.5.

# Ferramentas

Dentre as ferramentas utilizadas estão: nibabel, matplotlib, simpleITK, ITKSnap e framework nn-Unet.

# Workflow

> Fazer na próxima etapa.

# Experimentos e Resultados preliminares
## nnU-Net
O framework realiza o pré-processamento dos dados usando o comando "nnUNetv2_plan_and_preprocess -d DATASET_ID --verify_dataset_integrity" e para treinamento o comando "nnUNetv2_train DATASET_NAME_OR_ID UNET_CONFIGURATION FOLD --val --npz". Como o objetivo da execução da nnU-Net é apenas obter algumas ideias de pré-processamento deste dataset, não iremos detalhar este framework aqui, para mais informações, consulte o tutorial da [nnU-Net](https://github.com/MIC-DKFZ/nnUNet/tree/master).

> * Os dados foram organizados em pastas para cada sujeito. Em seguida eles foram separados em trainamento (80%), validação (10%) e teste (10%). O primeiro experimento foi feito sem pré-processamento dos dados.

> * O experimento do treinamento realizado está descrito no arquivo unet_sem_preproc.ipynb.

> * Após o treinamento da nn-Unet, obtiveram-se os seguintes resultados e pré-processamentos sugeridos pelo framework.

# Próximos passos

Trainar uma U-Net 3D a partir de alguns pré-processamentos fornecidos pela nn-Unet.

## Referências

Lucena, O., Souza, R., Rittner, L., Frayne, R., & Lotufo, R. (2018, April). Silver standard masks for data augmentation applied to deep-learning-based skull-stripping. In 2018 IEEE 15th International Symposium on Biomedical Imaging (ISBI 2018) (pp. 1114-1117). IEEE.

Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.

Carmo, D., Silva, B., Yasuda, C., Rittner, L., & Lotufo, R. (2021). Hippocampus segmentation on epilepsy and Alzheimer's disease studies with multiple convolutional neural networks. Heliyon, 7(2).
