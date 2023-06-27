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

Detatalhes importantes sobre os conjuntos de dados e sua organização:
* Todos os conjuntos de dados originais estão no formato NIfTI.
* A organização dos dados foi feita separadamente para cada conjunto de dados. Isso porque os conjuntos de dados eram muito diferentes e nos perdemos ao tentar implementar um único código para organizar e separar em treinamento validação e teste automaticamente. Além disso, alguns passos simples foram feitos manualmente como, criar pastas para cada conjunto de dados ou separar os dados com anotações manuais do conjunto de dados CC359.
* Para o treinamento da nn-Unet não foram usados todos os conjuntos de dados, apenas alguns dados do CC359, LBPA40 e NFBS, pois ainda estávamos muito perdidos nessa organização. A quantidade de dados usados incluído os três conjuntos foi de 240 sujeitos e a divisão do conjunto de dados em treinamento e validação é feito automaticamente pelo framework. 29 sujeitos desses 3 conjuntos de dados foram reservados para teste final do experimento do framework. Ainda, foi preciso organizar os dados da maneira que o framework exige, consulte o [tutorial da nnU-Net](https://github.com/MIC-DKFZ/nnUNet/tree/master). Em seguida, as anotações foram binarizadas usando limiarização de 0.5, uma vez que os dados adquiridos estavam com as máscaras de tipo float (entre 0 e 1) nas bordas e este framework não permite máscaras com labels que não contêm valores inteiros. A implementação para isso está no notebook [organizar de dados para executar a nnU-Net](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/data_organization/organizar_dados_nnUNet.ipynb).
* Essa divisão dos conjuntos de dados foi usada apenas no modelo 3D.

## Metodologia
### Arquitetura U-Net
Este trabalho utilizou a arquitetura [U-Net](https://link.springer.com/chapter/10.1007/978-3-319-24574-4_28), uma rede neural convolucional bastante utilizada para segmentação de imagens médicas. Utilizamos as versões 2D e 3D da [U-Net modificada](https://link.springer.com/chapter/10.1007/978-3-030-72084-1_38), conforme implementado por Carmo et al. (2020). 

![U-Net modificada](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/assets/Unet-IA901A.png)*Figura 01 - U-Net modificada: a resolução espacial é reduzida pela segunda convolução de cada nível do codificador; os blocos verde se referem as características filtradas pela operação de self attention; cada nível do codificador e decodificador (blocos de duas convoluções) possui conexão residual realizando a conexão da entrada da primeira convolução à saída da segunda convolução (seta em laranja)*

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

* [Normalização](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/pre-processing/data_normalization.ipynb): a normalização sugerida pelo framework foi a Z-Score Normalization 'ZScoreNormalization'. Essa é uma técnica utilizada para transformar os valores de uma variável para que tenham média zero e desvio padrão igual a 1. Bastante utilizada quando se tem variáveis que têm escalas diferente, deixando as variáveis em uma escala compatível ou comparável. Em MRIs, para a realização dessa normalização a imagem é subtraída de sua média e essa operação é dividida pelo desvio padrão da imagem: 

$$ X_{nor} =  (X - \mu) / (\sigma)$$

Onde X é a matriz (volume); $\mu$ é a média da matriz; e $\sigma$ é o desvio padrão da matriz. Essa normalização resulta em média igual a 0 e desvio padrão igual a 1.

* [Conversão para o npz](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/pre-processing/get_data_npz.ipynb): Para facilitar a treinamento e diminuir o custo computacional durante o treinamento, os dados foram convertidos de NIfTI para npz. Uma vez os dados corretos e alinhados com a máscara é mais vantajoso computacionalmente converter para um formato mais leve. Neste caso, o npz não armazena a informação do cabeçalho da imagem e isso diminui o custo computacional e tempo de execução ao carregar os dados durante o treinamento. Para cada experimento (3D) os dados foram salvos em npz (imagem e máscara no mesmo arquivo). Por exemplo, após a realização do pré-processamento de normalização, os dados eram salvos em npz.

### Utilização e divisão dos conjuntos de dados 
Para o treinamento da versão da arquitetura 3D, os conjuntos de dados LBPA40, CC359 e NFBS foram usados simultaneamente durante o treinamento do modelo em todos os experimentos. Os dados foram então dividos (incluidos esses 3 conjuntos de dados) em treinamento (392 sujeitos: 87 do NFBS, 277 do CC359 e 28 do LBPA40) e validação (103 sujeitos: 25 do NFBS, 70 do CC359 e 8 do LBPA40). A avaliação do modelo foi feita no conjunto de teste final (xx sujeitos) (VERIFICAR SE ISSO VAI SE MANTER PARA O 2D)

### Métricas de Avaliação
As métricas de avaliação utilizadas foram:
* [Coeficiente Dice (ou DSC, do inglês Dice Similarity Coefficient)](https://www.jstor.org/stable/1932409?casa_token=RFaYUTaEtkUAAAAA%3ANV4GvJGgLFTE922Oa9Paw7Jar5HM07VQYC3_IQf86hbOuUQv2mAjpYDzCBZ_X4BFo7azcJ_uu3mk0tTeY-qi3HufoQaE2t_0SMEPbDAhcHjs-9TBLz3D): bastante utilizada para avaliação de segmentações (DICE, 1945), compara duas segmentações diferentes, fornecendo a semelhança entre elas e. Esta é dada por:

$$ Dice =  2VP / FP + FN + 2VP$$

* [Similaridade de volume (SV)](https://ieeexplore.ieee.org/abstract/document/7053955): complementar ao Dice, mede a similaridade de volume entre duas segmentações (distância volumétrica). Indica a diferença absoluta de volume dividida pela soma dos volumes comparados, definida por:

$$ SV = 1 - \frac{\left| FN - FP \right|}{2VP + FP + FN}$$

$VP$ são valores classificados corretamente como positivos, $FP$ são valores classificados erroneamente como positivos e $FN$ são valores classificados erroneamente como negativos.

* Distância média de Hausdorff (AVD, do inglês average Haousdorff distance): utilizadas como medidas de dissimilaridade, calcula a distância média euclidiana entre os contornos calculados sobre todos os pontos, definida por:

$$ AVD = max(max_{s\in{S}}\left| d_s \right| . max_{r\in{R}}\left| d_r \right|)$$

$d$ é a distância média controlada pela métrica $AVD$, $AVD$ é a segmentação de referência (padrão-ouro), $S$ é a segmentação obtida pelo método, $r$ e $s$ são os pontos contidos nos contornos de $R$ e $S$, respectivamente, e $d_s$ e $d_r$ são as distâncias médias entre os pontos $s$ e $r$ aos pontos de contorno de $R$ e $S$ mais próximos.

### Treinamento da arquiterura 2D

### Treinamento da arquiterura 3D
O treinamento do modelo 3D foi realizado ao utilizar o volume de entrada para obter patch 3D que foi usado como canal de entrada da U-Net 3D. A rede realiza o treinamento e retorna como saída a segmentação do cérebro.  

![Workflow 3D](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/assets/Workflow_3D.png)
*Figura 02 - Workflow 3D: treinamento da U-Net 3D usando patch obtido aleatoriamente do volume de entrada (I) e predição usando patches 3D no volume de entrada (II).*

#### Treinamento e Avaliação do Modelo 3D

Por ser uma arquitetura totalmente convolucional, o tamanho da imagem para o treinamento da U-Net não precisa ser o mesmo da avaliação. Sendo assim, o treinamento do modelo 3D foi feito usando patch 3D de tamanho 102 × 102 × 102 nos canais de entrada (Fig x). Para cada volume (amostra) é escolhido um patch de forma aleatória, como é apenas um de cada imagem, isso introduz variabilidade a cada amostra passada para a rede, mas não é necessariamente um aumento de dados. 

Com o modelo treinado, a segmentação volumétrica do cérebro de uma nova amostra foi feita ao passar uma imagem completa para o modelo (Fig. x-II). Para isso, foi usado um método de inferência de janela deslizante, inspirado na implementação da [nnU-Net](https://www.nature.com/articles/s41592-020-01008-z) e usando uma implementação do [Monai](https://link.springer.com/chapter/10.1007/978-3-031-12053-4_58). Esse método reconstrói a segmentação completa do volume de entrada usando patches com ponderação gaussiana para predições e uma janela 3D de 10%.

#### Aumento de dados
Para a abordagem 3D, foram testadas apenas as técnicas de RandomAffine e a RandomBlur implementadas na biblioteca [TorchIO](https://torchio.readthedocs.io/transforms/augmentation.html).

1. RandomAffine: é uma transformação geométrica aleatória que pode ser aplicada na imagens e permite a combinação aleatória de rotação, translação, redimensionamento, cisalhamento e reflexão em uma imagem. É comumente usada para criar variações sintéticas nos dados de treinamento e melhorar a robustez e generalização de modelos de aprendizado de máquina. Neste trabalho foram aplicados para essa técnica o fator escala (scales) de (0.9, 1.2) e graus (degrees) de 90.  Graus é um intervalo de ângulos de rotação possíveis, em que cada ângulo é escolhido aleatoriamente dentro desse intervalo, enquanto a escala é um fator de escala de mínimo e máximo, em que é escolhido aleatoriamente dentro desse intervalo. 

### Ferramentas

As principais ferramentas utilizadas para o pré-processamento dos dados e treinamento do modelo foram:
* [NiBabel](https://nipy.org/nibabel/): Uma biblioteca para vizualização e pré-processamento de dados no formato nífiti. Neste trabalho esta biblioteca foi usada principalmente para leitura das imagens, uma vez que permite acessar informações do cabeçalho das imagens, como matriz affine (as vezes necessária para salvar corretamente resultados de um pré-processamenta). Também permite obter as imagens no fromato de uma matriz ou numpy para realização dos pré-processamentos.

* [Matplotlib](https://matplotlib.org/stable/index.html): bastante útil para vizualização dos resultados qualitativos, permitindo se necessária a inspeção de cada passo realizado.

* [simpleITK](https://simpleitk.org/doxygen/v2_1/html/): é uma biblioteca com funcionalidade semelhante à nibabel. Esta biblioteca tem sido recorrentemente utilizada por pesquisadores na área da imagem médica, uma vez que permite e simplifica algumas manipulações desses dados, por exemplo, quando o pré-processamento exige a modificação da matriz affine. Garantir resultados coerentes com a biblioteca nibabel quando se deseja modificar a affine dos dados é relativamente mais complexo do que usar a simpleITK. Neste trabalho, ela foi usada para realizar o pré-processamento de [interpolação de voxel](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/notebooks/pre-processing/voxel_interpolation.ipynb).   

* [ITKSnap](http://www.itksnap.org/pmwiki/pmwiki.php?n=Documentation.TutorialSectionInstallation): é uma ferramenta utilizada para inspeção e visualização de dados volumétricos ou 2D em imagens médicas. Ela foi utiliza para este fim neste trabalho. 

* [nnU-net](https://www.nature.com/articles/s41592-020-01008-z): é um framework que realiza automaticamente préprocessamento de dados e trainamento de modelos de segmentação de imagens. Além disso, fornece os pré-processamentos que melhor se adequa a conjuntos de dados especificos, assim como parâmetros da arquitetura. Neste trabalho, ele foi usado para obter sugestões do pré-processamento de dados e hiperparâmetros da rede, que alguns foram escolhidos para serem usados como ponto de partida neste trabalho.

* [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/): é um framework relativamente leve para treinamento de modelos de aprendizado profundo, que oferece uma abstração de alto nível sobre o PyTorch. Ele simplifica e organiza o código, facilitando a criação, o treinamento e o teste de modelos de aprendizado profundo de forma mais estruturada. Além disso, tem fácil conexão com o Neptune.

* [Neptune](https://neptune.ai/): é uma plataforma de colaboração para experimentos de aprendizado de máquina. Ele oferece recursos avançados para rastrear, visualizar e compartilhar experimentos, bem como para monitorar e otimizar modelos de aprendizado de máquina. Com uma interface intuitiva e simples, permite acompanhar todas as etapas de um projeto, desde a coleta de dados até a implantação do modelo. Neste trabalho, foi utilizado apenas para monitoramento do modelo 3D.

* [TorchIO](https://torchio.readthedocs.io/transforms/augmentation.html): uma biblioteca de processamento de imagens baseada no PyTorch, que permite transformações e utilidades para o pré-processamento de dados médicos. Fornece um conjunto de transformações flexíveis para manipulação e aumentação de dados de imagem, como rotação, translação, redimensionamento, normalização, entre outras. O TorchIO é frequentemente usado em imagem 3D, por oferecer simplicidade na implementação de manipulação de volumes, no entanto, não é limitado apenas a dados 3D e pode ser usado para processar dados 2D e 1D, desde que haja ajuste as transformações e operações de acordo com a natureza dos seus dados.

* Além dessas ferramentas, outras foram usadas para monipulação dos dados, como: [NumPy](https://numpy.org/doc/). (COLOCAR OUTRAS FERRAMENTAS). 

> Fazer na próxima etapa.

## Experimentos e Resultados
### nnU-Net
O framework realiza o pré-processamento dos dados usando o comando "nnUNetv2_plan_and_preprocess -d DATASET_ID --verify_dataset_integrity" e para treinamento o comando "nnUNetv2_train DATASET_NAME_OR_ID UNET_CONFIGURATION FOLD --val --npz". Como o objetivo da execução da nnU-Net é apenas obter algumas ideias de pré-processamento deste dataset, este não será detalhado aqui, para mais informações, consulte o tutorial da [nnU-Net](https://github.com/MIC-DKFZ/nnUNet/tree/master).

Apenas o modelo 3D da nnU-Net foi executado e o resultado obtido por este foi um valor de Dice médio de 0,9898 no conjunto de validação. Detalhes sobre este resultados pode ser encontrado no [arquivo summary](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/assets/summary.json) e [gráfico](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/assets/progress.png) fornecidos pelo framework. 

### Avaliação da U-Net 2D

### Avaliação da U-Net 3D
Os experimentos desta seção foram realizados em uma GPU Titan X. Experimentos foram realizados para testar a aplicação de pré-processamento de dados (redimensioanmento de voxel e normalização) e definir aumento de dados e os principais hiperparâmetros, como a learning rate e número de épocas. Desde o início, foram mantidos fixos o uso do [otimizador Adam](https://arxiv.org/abs/1412.6980) com [Dice Loss](https://link.springer.com/chapter/10.1007/978-3-319-67558-9_28), o método de patch RandomCrop com seu tamanhos de (102, 102, 102) e o tamanho do batch de 2. Esses parâmetros fixos foram usados de acordo com os sugeridos pela nnU-Net, com exceção do otimizados e da função de perda. Também o tamanho de patch não foi o mesmo sugerido pela nnU-Net, pois a GPU usada para a execução do treinamento, não permitiu o tamanho de patch de (128, 128, 128).

Os objetivos desses experimentos foram (de acordo com o sugerido pela nnU-Net):
1. Verificar quais pré-processamentos são relevantes para melhorar o desempenho do modelo;
2. Verificar quais aumento de dados ajudam a obter um modelo mais robusto;
3. Verificar se há ganho significativo ao mudar os hiperparâmetros taxa de aprendizado e número de época.

A execução dos experimentos usando a U-Net 3D, objetivou avaliar a aplicação dos pré-processamento: redimensionamento de voxel, normalização e padronização das labels das anotações fornecidas nos conjuntos de dados. Também a avaliação da técnica de aumento de dados RandomAffine (Tab. 2). 


Tabela 1: Dice médio no conjunto de validação para os experimentos realizados usando a U-Net 3D: dados sem nenhum processamento (Experimento 1); ao realizar a padronização das labels de entre os 3 datasets (Experimento 2); Depois de padronizar as labels, foi feita a interpolação de voxel nos dados (Experimento 3); em seguida os dados foram normalizados (Experimento 4); por fim foi testado a técinca de Random Affine (Experimento 5).
|Experimento  | N° de épocas (época) | perda |modelo| pós-processada|
|-------------|-----------------|--------------|-------|------------|
| 1 |500 (459)             | -0.05 | 0.6643     | 0.8309
|2 | 100 (68)             | 0.04  | 0.7752     | 0.8239
|3 |100 (90)              | 0.03  | 0.8953     | 0.9044|
| 4  |100 (55)              | 0.03  | 0.9637     | 0.97307 |
|5   |100 (55)              | 0.03  | 0.9357     | 0.9596 |

Note que o pré-processamento é sequencial, sendo que a interpolação do voxel foi aplica nos dados com as labels padronizadas. Foi observado que realizar o pré-processamento nos dados ajuda no desempenho do modelo, principalmente a normalização dos dados e a interpolação de voxel. 

As figuras abaixo mostram as curvas de perda do treinamento e da validação. O experimento 4 e convergiram melhor se comparados aos demais experimentos, no entanto, o experimento 4 convergiu melhor, apresentando melhores resultados na avaliação feita no conjunto de validação. Este foi definido para a análise subsequente. 

![Train_loss](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/assets/training_loss_epoch.png)*Figura 03 - Curva de aprendizado durante o treinamento (função de perda para o treinamento): experimetos 2 (rosa), 3 (amarelo), 4 (vinho); e 5 (azul)*

![Val_loss](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/assets/training_val_loss.png)*Figura 04 - Curva de aprendizado durante o treinamento (função de perda para a validação: experimetos 2 (rosa), 3 (amarelo), 4 (vinho); e 5 (azul)*

A avaliação no conjunto de teste foi feita apenas no melhor modelo 3D (experimento 4). Foi possível fazer um estudo ao realizar a predição usando todos os conjuntos de dados do conjunto de teste simultaneamente ou separadamente.


Tabela 1 : Resultados das métricas para o melhor modelo 3D (conjunto de teste): média e desvio padrão.
|Conjunto de dados     |Dice             | AVD                  | SV    |
|----------------------|-----------------|----------------------|-------|
|todos                 | $0.9629\pm0.0055$| $0.0673\pm0.0242$   | $0.9849\pm0.0080$   |
| IBSR                |$0.9737\pm0.0032$|$0.0445\pm0.0259$     | $0.9867\pm0.0100$|
| CC359                 |$0.9671\pm0.0031$|$0.0593\pm0.0116$ |$0.9880\pm0.0082$ | 
| LBPA40              | $0.9671\pm0.0031$ |$0.0593\pm0.0116$ | $0.9880\pm0.0082$|

Os resultados foram satisfatórios, uma vez que o dice médio se manteve próximo ao que foi apresentado no conjunto de validação e treinamento. Além disso, não houve divergencia entre os conjuntos de dados, pois os resultados são bastante semelhantes inclusive com os resultados de todos os conjuntos de dados juntos.

Os resultados qualitativos (Figura 5) confirmam a boa qualidade das segmentações obtida pelo modelo. O pior resultado aparenta ser no conjunto de dados LBPA40.

![Res_qual](https://github.com/jimitogni/IA901-2023S1/blob/vers%C3%B5es_unet/projetos/Brain_segmentation/assets/resul_qual_3D.png)*Figura 05 - Resultados qualitativos usando o melhor Dice obtido em cada conjunto de dados. Renderização 3D da saída do modelo (sup.) e sobreposição das anotação manual e a saída do modelo em fatias centrais dos três eixos (axial, coronnal e sagital). Anotação manual (azul) e saída do modelo (vermelho).*

# Conclusão 

# Próximos passos

* Realizar experimentos ao aplicar outras técnicas de aumento de dados, como RandomBlur.
* Testar hiperparâmetros da rede, como variar a taxa de aprendizagem e número de épocas.
* Verificar a normalização implementada, pois para se ter valores entre -1 e 1 a média e o desvio padrão deixaram de ser 0 e 1, respectivamente.

## Referências

Lucena, O., Souza, R., Rittner, L., Frayne, R., & Lotufo, R. (2018, April). Silver standard masks for data augmentation applied to deep-learning-based skull-stripping. In 2018 IEEE 15th International Symposium on Biomedical Imaging (ISBI 2018) (pp. 1114-1117). IEEE.

Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.

Carmo, D., Silva, B., Yasuda, C., Rittner, L., & Lotufo, R. (2021). Hippocampus segmentation on epilepsy and Alzheimer's disease studies with multiple convolutional neural networks. Heliyon, 7(2).
