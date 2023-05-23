# `<Segmentação do cérebro usando imagens T1>`
# `<Brain Segmentation on T1 image>`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*, 
oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em trios.
> |Nome  | RA | Curso|
> |--|--|--|
> | Jimi Togni           |  226359  | Doutorado em Engenharia Elétrica|
> | Joany Rodrigues      | 264440   | Mestrado em Engenharia Elétrica|
> | Victor Praxedes Rael | 240242   | Mestrado em Engenharia Elétrica|


## Descrição do Projeto
> Descrição do objetivo principal do projeto, incluindo contexto gerador, motivação.
> Muitos desafios na área de imagem médica exigem como pré-processamento a segmentação do cérebro, por exemplo, a realização de registro e segmentação de estruturas cerebrais. Logo, o objetivo deste projeto é desenvolver um método de segmentação do cérebro usando técnicas de deep learning (CNNs) e estudar técnicas de pré-processamento dos dados para averiguar quais são viáveis para a melhoria do modelo. Já existem trabalhos que realizam a extração do cérebro, por exemplo, (Lucena et. al. 2018). Esta questão vem sendo bastante estudada.

> Qual problema vocês pretendem solucionar?
> Qual a relevância do problema e o impacto da solução do mesmo?

# Metodologia

## Versão 3D da U-Net
### Implementação básica para treinamento de uma arquitetura U-Net 3D 
Implementação com quatro camadas de pooling e uma camada de Bottleneck, seguida por quatro camadas de upsampling. Mais detalhes em unet_sem_preproc.ipynb.

### Versão 3D da U-Net modificada 
A versão 3D da U-Net modificada por Carmo et. al (Carmo et.al. 2021) será utilizada para treinamento 3D da base de dados deste trabalho. Para inicializar este estudo, foi executado um treinamento do framework nnU-Net, que busca o melhor pré-processamento de um conjunto de dados, hiperparâmetros da rede e préprocessamento de dados, objetivando o melhor modelo baseado na arquitetura U-Net para obter a segmentação de objetos, automaticamente. Logo, este framework foi executado com o objetivo de adquirir os pré-processamentos dos conjuntos de dados usados neste trabalho e usar como ponto de partida para o treinamento 3D deste projeto. O framework realiza o préprocessamento dos dados usando o comando "nnUNetv2_plan_and_preprocess -d DATASET_ID --verify_dataset_integrity" e para treinamento o comando "nnUNetv2_train DATASET_NAME_OR_ID UNET_CONFIGURATION FOLD --val --npz". Como o objetivo da execução da nnU-Net é apenas obter algumas ideias de pré-processamento deste dataset, não iremos detalhar este framework aqui, para mais informações, consulte (https://github.com/MIC-DKFZ/nnUNet/tree/master).



## Bases de Dados e Evolução

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
LBPA40 | https://www.loni.usc.edu/research/atlas_downloads | conjunto de dados com atlas baseado em ressonância magnética da anatomia do cérebro, gerado por registro não rígido sem modelo a partir de imagens de 24 indivíduos de controle normais.
CC359 | https://portal.conp.ca/dataset?id=projects/calgary-campinas | conjunto de dados de ressonância magnética cerebral Calgary Campinas, composto por imagens de RM do cérebro ponderadas em T1 e máscaras de segmentação do cérebro.
NFBS | http://preprocessed-connectomes-project.org/NFB_skullstripped/ | é um dataset com 125 ressonâncias magnéticas anatômicas ponderadas em T1 que tem anotações manual docérebro. Este conjunto de dados fornece 3 arquivos para cada sujeito: Structural T1-weighted anonymized image, Skull-stripped image, Brain mask.
IBSR | https://www.nitrc.org/projects/ibsr | repositório de Segmentação Cerebral da Internet (IBSR) fornece anotações manuais, juntamente com dados de imagem cerebral por ressonância magnética em T1.

> * Todos os datasets originais (baixados) estão no formato nifti.
> * Foi feita automaticamente a organização dos dados em pastas para cada sujeito.
> * A base de dados IBSR veio com desalinhamento entre a imagem e a máscara. 
> * Para o treinamento da nn-Unet, foi preciso organizar os dados da maneira que o framework exige, consulte (https://github.com/MIC-DKFZ/nnUNet/tree/master). E em seguida as anotações foram binarizada usando limiarização de 0.5. 

# Ferramentas
> nibabel, matplotlib, simpleITK, ITKSnap, framework nn-Unet.

# Workflow
> Fazer na próxima etapa.

# Experimentos e Resultados preliminares
> * Os dados foram organizados em pastas para cada sujeito. Em seguida eles foram separados em trainamento (80%), validação (10%) e teste (10%). O primeiro experimento foi feito sem pré-processamento dos dados.

> * O experimento do treinamento realizado esta destrito no arquivos unet_sem_preproc.ipynb. 

> * Apos o treinamento da nn-Unet, obteve-se os seguintes resultados pré-processamentos sugerimos pelo framework. 

# Próximos passos

> Trainar uma U-Net 3D a partir de alguns pré-processamentos fornecidos pela nn-Unet.

## Referências (ATUALIZAR SE NECESSÁRIO)
> Lucena, O., Souza, R., Rittner, L., Frayne, R., & Lotufo, R. (2018, April). Silver standard masks for data augmentation applied to deep-learning-based skull-stripping. In 2018 IEEE 15th International Symposium on Biomedical Imaging (ISBI 2018) (pp. 1114-1117). IEEE.

Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2021). nnU-Net: a self-configuring 
method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.

Carmo, D., Silva, B., Yasuda, C., Rittner, L., & Lotufo, R. (2021). Hippocampus segmentation on epilepsy and Alzheimer's disease studies with multiple convolutional neural networks. Heliyon, 7(2).


