# `Segmentação do cérebro usando imagens T1`
# `Brain Segmentation on T1 images`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*, oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

|Nome  | RA | Curso|
|--|--|--|
| Jimi Togni           | 226359   | Doutorado em Engenharia Elétrica |
| Joany Rodrigues      | 264440   | Mestrado em Engenharia Elétrica  |
| Victor Praxedes Rael | 240242   | Mestrado em Engenharia Elétrica  |

## Descrição do Projeto

Muitos desafios na área de imagem médica exigem como pré-processamento a segmentação do cérebro, por exemplo, a realização de registro e segmentação de estruturas cerebrais. Muitas propostas tem surgindo para solucionar este problema, o que já tem boas propostas na literatura, por exemplo, o trabalho por [LUCENA, Oeslle et al.](https://ieeexplore.ieee.org/abstract/document/8363766?casa_token=Y9VwrDbJQJ8AAAAA:7MsKQIPK9IAl2PD8zla2eRkO2jNtqUilIMtqGjEBGlRb_P9SNNJkXwgJR91otfmY_wGeJSfhGJg). 

Tem surgido propostas na literatura mostrando que ao aplicar técnicas de pré-processamento e aumento de dados pode ser mais vantajoso do que apenas usar técnicas de última geração. Por exemplo, a implementação do framework [nnU-Net](https://www.nature.com/articles/s41592-020-01008-z), que busca o melhor pré-processamento de um conjunto de dados e hiperparâmetros da rede para este conjunto de dados, automaticamente. O objetivo deste framework é usar a arquitetura de uma CNN simples [U-Net](https://link.springer.com/chapter/10.1007/978-3-319-24574-4_28) para buscar de maneira autônoma o melhor modelo de segmentação de objetos de acordo com as características dos dados. Logo, este framework foi executado com o objetivo de adquirir os pré-processamentos dos conjuntos de dados usados neste trabalho e usar como ponto de partida para o treinamento 3D deste projeto.

Logo, o objetivo deste projeto é usar partes de um conjunto de dados de segmentação do cérebro para executar um experimento na nnU-Net e obter suas sugestões de pŕe-processamento de dados e parâmetros da rede para estudá-los e definir os mais intuitivéis e factíveis, para em seguida, desenvolver um método de segmentação do cérebro usando uma versão da arquitetura U-Net. Este estudo incluí averiguar quais dos pré-processamentos dos dados são viáveis para a melhoria de um modelo de segmentação do cérebro.

## Bases de Dados e Evolução

Base de Dados | Endereço na Web | Resumo descritivo
------------- | --------------- | -----------------
LBPA40 | [link de acesso](https://www.loni.usc.edu/research/atlas_downloads) | este conjunto de dados é público e contém dados de 40 sujeitos. Dentre outros arquivos, este conjunto de dados contém as imagens ponderadas em T1 e segmentações manuais do cérebro também em T1. Esse conjunto de dados foi fornecido por um membro do grupo MICLab. Os dados originais estão no formato mri.img.gz, porém os dados fornecidos para este estudo já se encontrava no formato nifti. A conversão de img.gz para NIfTI foi feita usando o software [ITKSnap](http://www.itksnap.org/pmwiki/pmwiki.php?n=Documentation.TutorialSectionInstallation). Para a organização desses dados, foi feito a separação apenas dos arquivos que foram usados neste trabalho (imagens e segmentação do cérebro); em seguida renomeamos estes arquivos para brainmask_T1w (segmentação do cérebro) e brain_T1w (imagem do cérebro) e então realizamos a divisão deste dataset em treinamento (70%), validação (20%) e teste (10%). Detalhes para esta organização estão no notebook [organização dos dados LBPA40](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/data_organization/LBPA40_dataset_organization.ipynb). 
CC359 | [link de acesso](https://portal.conp.ca/dataset?id=projects/calgary-campinas) | este é um conjunto de dados de ressonância magnética cerebral desenvolvido por pesquisadores da universidade de Calgary e Unicamp (MICLab). É composto por imagens de RM do cérebro ponderadas em T1 e máscaras de segmentação do cérebro também em T1. Contém 359 sujeitos todos com segmentação padrão-prata gerada a partir de um consenso entre segmentações obtidas por pelo menos 3 ferramentas (STAPLE). Apenas 12 sujeitos desses conjunto de dados contém máscaras manuais geradas por um especialista. Este conjunto de dados foi adquirido no formato NIfTI e em dois diretórios: um onde continham todas as imagens de todos os sujeito (original) e outro com todas as máscaras de todos os sujeitos (staple). Novamente, este conjunto de dados foi fornecido por um membro do grupo MICLab. A partir dos dados fornecidos não foi possível identificar os dados que continham segmentação manual. Para isso, foi preciso baixar os dados com anotação manual do site e identificar os sujeitos com anotações manuais, para separá-los manualmente e utilizá-los para teste final do modelo. Também, foi preciso separar os dados de cada sujeito em pastas (uma pasta para cada sujeito) com as imagens e as máscaras. Em seguida as imagens foram renomeadas para brain_T1w e as segmentações para brainmask_T1w. Por fim foi feito a divisão dos dados sem anotação manual (347 sujeitos) em treinamento (80%) e validação (20%). Detalhes da organização desse conjunto de dados estão no notebook [organização dos dados CC359](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/data_organization/CC359_dataset_organization.ipynb).
NFBS | [link de acesso](http://preprocessed-connectomes-project.org/NFB_skullstripped/) | é um dataset com 125 ressonâncias magnéticas anatômicas ponderadas em T1 que tem anotações manuais do cérebro. Este conjunto de dados fornece 3 arquivos para cada sujeito: Structural T1-weighted anonymized image, Skull-stripped image, Brain mask. (FALTA DESCREVER COMO FOI FEITA A ORGANIZÇÃO DESTE CONJUNTO DE DADOS)
IBSR | [link de acesso](https://www.nitrc.org/projects/ibsr) | este conjunto de dados é um repositório de segmentação cerebral da internet (IBSR, do inglês Internet Brain Segmentation Repository) que fornece anotações manuais, juntamente com dados de imagem cerebral por ressonância magnética em T1. Contém 18 sujeitos, todos com anotações manuais. Novamente adquiridos por um membro do MICLab. No entanto, os dados estão com incompatibilidade, uma vez que as anotações manuais não estão alinhadas com as imagens. Por isso e para tentar corrigir isto, todo o conjunto de dados foi reservado para teste final. Os arquivos das imagens e máscaras foram transferidos para outro diretório e em seguida as imagens foram renomeadas para  brain_T1w e as segmentações para brainmask_T1w. Detalhes da organização desse conjunto de dados estão no notebook [organização dos dados IBSR](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/data_organization/IBSR_dataset_organization.ipynb).

Detatalhes importantes sobre os conjuntos de dados e sua organização:
* Todos os conjuntos de dados originais estão no formato NIfTI.
* A organização dos dados foi feita separadamente para cada conjunto de dados. Isso porque os conjuntos de dados eram muito diferentes e nos perdemos ao tentar implementar um único código para organizar e separar em treinamento validação e teste automaticamente. Além disso, alguns passos simples foram feitos manualmente como, criar pastas para cada conjunto de dados ou separar os dados com anotações manuais do conjunto de dados CC359.
* Para o treinamento da nn-Unet não foram usados todos os conjuntos de dados, pois ainda estávamos muito perdidos nessa organização, foram usados apenas xx sujeitos. Ainda, foi preciso organizar os dados da maneira que o framework exige, consulte o [tutorial da nnU-Net](https://github.com/MIC-DKFZ/nnUNet/tree/master). Em seguida, as anotações foram binarizadas usando limiarização de 0.5, uma vez que os dados adquiridos estavam com as máscaras de tipo float (entre 0 e 1) nas bordas e este framework não permite máscaras com labels que não contêm valores inteiros. A implementação para isso está no notebook [organizar de dados para executar a nnU-Net](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/data_organization/organizar_dados_nnUNet.ipynb).

## Metodologia
### Arquitetura U-Net
Este trabalho utilizou a arquitetura [U-Net](https://link.springer.com/chapter/10.1007/978-3-319-24574-4_28), uma rede neural convolucional bastante utilizada para segmentação de imagens médicas. Utilizamos as versões 2D e 3D da [U-Net modificada](https://link.springer.com/chapter/10.1007/978-3-030-72084-1_38), conforme implementado por Carmo et al. (2020). 

![U-Net modificada: a resolução espacial é reduzida pela segunda convolução de cada nível do codificador; os blocos verde se referem as características filtradas pela operação de self attention; cada nível do codificador e decodificador (blocos de duas convoluções) possui conexão residual realizando a conexão da entrada da primeira convolução à saída da segunda convolução (seta em laranja).](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/assets/Unet-IA901A.png)

Mudaças da U-Net modificada em relação a original inclui: a utilização de convoluções stride para a redução da resolução espacial em vez de operações de agregação; adição de [conexão residual](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html) propagando a entrada à saída de cada nível do codificador (utilizando soma e uma convolução com kernel de 1 × 1 (seta laranja) realizando adaptação de canal e resolução espacial e adição de uma operação [self attention](http://proceedings.mlr.press/v102/gorriz19a.html) para filtrar as características produzidas em cada nível do codificador.

Modificações entre as versões 2D e 3D inclui: o número de canais de entrada para a versão 3D é reduzido devido ao aumento da dimensionalidade da variante 3D, uma vez que cada volume é considerado um canal, enquanto para a versão 2D cada fatia de um volume é considerado um canal; utilização de normalização de instância para a versão 3D, comumente usada em redes convolucionais 3D com batch pequeno e a normalização em lote para a versão 2D, pois o tamanho do batch é consideravelmente maior e costuma funcionar bem neste caso quando utiliza convoluções 2D.

### Pré-Processamento de dados
#### nnU-Net 
Os dados foram executados no framework nnU-Net apenas para obtermos sugestões de pré-processamento dos dodos e parâmetros da rede. Para a execusão dos dados na nnU-Net, foi necessário organizar os dados da forma que esta exige. A implementação usada para organização no conjunto de dados usados neste trabalho pode ser encontrado no notebook [organizar de dados para executar a nnU-Net](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/data_organization/organizar_dados_nnUNet.ipynb), para mais informações acesse o tutorial do framework. 

Ao executarmos os dados na nnU-Unet, esta forneceu um problema nas segmentações anotadas, uma vez que as essas não era binárias (continham valores entre 0 e 1) e este framework não aceita labels que não sejam numéros inteiros. Isso foi importante para sabermos que as segmentações dos dados não estavam binarizadas. Isso foi corrigido para execução da nnU-Net usando o código presente também no notebook [organizar de dados para executar a nnUNet](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/data_organization/organizar_dados_nnUNet.ipynb).

Após a execução da nnU-Net, foi obtido uma [lista de pré-processamento](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/assets/debug.json) do treinamento 3D e 2D realizado pelo framework. A partir dessa lista, consideramos os seguintes pré-processamentos para o treinamento das duas versões da arquitetura U-Net (2D e 3D):

#### Definição de Pré-processamentos
* [Redimensionamento de voxel](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/pre-processing/voxel_interpolation.ipynb) (spacing): redimensionamento de voxel é interpolar o voxel para mudar seu tamanho, o que influencia diretamente na resolução da imagem. Isso modifica significativamente os dados chegando a introduzir ruído a partir da interpolação. No entando, além de ter sido sugerido pelo framewark, este trabalho usa 4 conjunto de dados diferentes e para manter os voxels de todos os dados padronizados foi feito a interpolação de voxel, mantendo todos os volumes de treinamento e validação isométricos com tamanho de voxel igual a 1. Observe que a sujestão da nnU-Net foi de [1.0, 0.9999008178710938, 1.0], mas foi usado [1.0, 1.0, 1.0] para deixar os dados isométricos. A tabela abaixo resume o tamanho de voxel e resolução dados de cada conjunto de dados antes e após a interpolação de voxel.

|Aquisição| Tam. Vox. original (𝑚𝑚^3) | Tam. Vox. Iso (𝑚𝑚^3) | resolução original | resolução c/ Interpolação de Voxel |
|---------|---------------------------|-----------------------|--------------------|-----------------------|
| CC359   | 1 x 1 x 1                 | 1 x 1 x 1             | 171 x 256 x 256    | 171 x 256 x 256 |
| LBPA40  | 0.8594 x 1.5 x 0.8594     | 1 x 1 x 1             | 256 x 124 x 256    | 220 x 186 x 120 |
| NFBS    | 1 x 1 x 0.9999            | 1 x 1 x 1             |  256 x 256 x 192   | 256 x 256 x 192 |
| IBSR    | 0.9375 x 0.9375 x 1.5     | 1 x 1 x 1             |  256 x 256 x 128   | - |

* [Normalização](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/pre-processing/data_normalization.ipynb): a normalização sugerida pelo framework foi a Z-Score Normalization 'ZScoreNormalization'. Essa é uma técnica utilizada para transformar os valores de uma variável para que tenham média zero e desvio padrão igual a 1. Bastante utilizada quando se tem variáveis que têm escalas diferente, deixando as variáveis em uma escala compatível ou comparável. Em MRIs, para a realização dessa normalização a imagem é subtraída de sua média e essa operação é dividida pelo desvio padrão da imagem: 

$$ X_{nor} =  (X - \mu) / (\sigma$)$$

Onde X é a matriz (volume); $\mu$ é a média da matriz ($mean(X)$); e $\sigma$ é o desvio padrão da matriz ($std(X)$). Essa normalização resulta em média igual a 0 e desvio padrão igual a 1.

* [Conversão para o npz](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/pre-processing/get_data_npz.ipynb): Para facilitar a treinamento e diminuir o custo computacional durante o treinamento, os dados foram convertidos de NIfTI para npz. Uma vez os dados corretos e alinhados com a máscara é mais vantajoso computacionalmente converter para um formato mais leve. Neste caso, o npz não armazena a informação do cabeçalho da imagem e isso diminui o custo computacional e tempo de execução ao carregar os dados durante o treinamento. Para cada experimento (3D) os dados foram salvos em npz (imagem e máscara no mesmo arquivo). Por exemplo, após a realização do pré-processamento de normalização, os dados eram salvos em npz.

### Utilização e divisão dos conjuntos de dados 
Para o treinamento das versões arquitetura (2D e 3D), os conjuntos de dados LBPA40, CC359 e NFBS foram usados simultaneamente durante o treinamento do modelo em todos os experimentos. Os dados foram então dividos (incluidos esses 3 conjuntos de dados) em treinamento (392 sujeitos: 87 do NFBS, 277 do CC359 e 28 do LBPA40) e validação (103 sujeitos: 25 do NFBS, 70 do CC359 e 8 do LBPA40). A avaliação do modelo foi feita no conjunto de teste final (xx sujeitos) (VERIFICAR SE ISSO VAI SE MANTER PARA O 2D)

### Treinamento da arquiterura 2D

### Treinamento da arquiterura 3D
O treinamento do modelo 3D foi realizado ao utilizar o volume de entrada para obter patch 3D que foi usado como canal de entrada da U-Net 3D. A rede realiza o treinamento e retorna como saída a segmentação do cérebro.  

![Workflow 3D: treinamento da U-Net 3D usando patch obtido aleatoriamente do volume de entrada (I) e predição usando patches 3D no volume de entrada (II).](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/assets/Workflow_3D.png)

#### Treinamento e Avaliação do Modelo 3D

Por ser uma arquitetura totalmente convolucional, o tamanho da imagem para o treinamento da U-Net não precisa ser o mesmo da avaliação. Sendo assim, o treinamento do modelo 3D foi feito usando patch 3D de tamanho 102 × 102 × 102 nos canais de entrada (Fig x). Para cada volume (amostra) é escolhido um patch de forma aleatória, como é apenas um de cada imagem, isso introduz variabilidade a cada amostra passada para a rede, mas não é necessariamente um aumento de dados. 

Com o modelo treinado, a segmentação volumétrica do cérebro de uma nova amostra foi feita ao passar uma imagem completa para o modelo (Fig. x-II). Para isso, foi usado um método de inferência de janela deslizante, inspirado na implementação da [nnU-Net](https://www.nature.com/articles/s41592-020-01008-z) e usando uma implementação do [Monai](https://link.springer.com/chapter/10.1007/978-3-031-12053-4_58). Esse método reconstrói a segmentação completa do volume de entrada usando patches com ponderação gaussiana para predições e uma janela 3D de 10%.

# Ferramentas

Dentre as ferramentas utilizadas estão: nibabel, matplotlib, simpleITK, ITKSnap e framework nn-Unet.

# Workflow

> Fazer na próxima etapa.

## Experimentos e Resultados preliminares
### nnU-Net
O framework realiza o pré-processamento dos dados usando o comando "nnUNetv2_plan_and_preprocess -d DATASET_ID --verify_dataset_integrity" e para treinamento o comando "nnUNetv2_train DATASET_NAME_OR_ID UNET_CONFIGURATION FOLD --val --npz". Como o objetivo da execução da nnU-Net é apenas obter algumas ideias de pré-processamento deste dataset, não iremos detalhar este framework aqui, para mais informações, consulte o tutorial da [nnU-Net](https://github.com/MIC-DKFZ/nnUNet/tree/master).

> * Os dados foram organizados em pastas para cada sujeito. Em seguida eles foram separados em trainamento (80%), validação (10%) e teste (10%). O primeiro experimento foi feito sem pré-processamento dos dados.

> * O experimento do treinamento realizado está descrito no arquivo unet_sem_preproc.ipynb.

> * Após o treinamento da nn-Unet, obtiveram-se os seguintes resultados e pré-processamentos sugeridos pelo framework.

### Avaliação da U-Net 3D
> O treinamento do modelo inclui o uso de [Dice Loss](https://link.springer.com/chapter/10.1007/978-3-319-67558-9_28) como função de perda e [otimizador Adam](https://arxiv.org/abs/1412.6980). O tamanho do batch foi o mesmo sugerido pelo framework nnU-Net, 2. O tamanho de patch não foi o mesmo sugerido pala nnU-Net, isso porque não havia GPU que coubesse o tamanho de patch sugerido, logo foi necessário diminuir o tamanho de patch para (102 x 102 x102)

# Próximos passos

Trainar uma U-Net 3D a partir de alguns pré-processamentos fornecidos pela nn-Unet.

## Referências

Lucena, O., Souza, R., Rittner, L., Frayne, R., & Lotufo, R. (2018, April). Silver standard masks for data augmentation applied to deep-learning-based skull-stripping. In 2018 IEEE 15th International Symposium on Biomedical Imaging (ISBI 2018) (pp. 1114-1117). IEEE.

Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.

Carmo, D., Silva, B., Yasuda, C., Rittner, L., & Lotufo, R. (2021). Hippocampus segmentation on epilepsy and Alzheimer's disease studies with multiple convolutional neural networks. Heliyon, 7(2).
