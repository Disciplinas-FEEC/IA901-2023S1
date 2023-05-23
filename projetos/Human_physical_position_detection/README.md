# `Detecção de posição física humana`
# `Human physical position detection`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*, 
oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

|Nome  | RA | Curso|
|--|--|--|
| Octavio S Guaschi  | 218390  | Mestrado em Eng. Elétrica|
| Breno Portela  | 253502  | Mestrado em Eng. Elétrica|
| Cesar Bastos  | 264521  | Doutorado em Eng. Elétrica|


## Descrição do Projeto

O objetivo desse projeto é tratar fotos de pessoas em diferentes posições (Em pé, sentado, deitado), visando construir um modelo articulado da estrutura humana. Por conseguinte, esses dados serão inseridos em uma rede neural que irá avaliar a posição do indíviduo. Realizar segmentação das pessoas nas imagens e a diferenciação entre em pé e deitado.

# Metodologia

Métodos visto em sala a serem utilizados - Limiarização, segmentação e redes neurais convolucionais. Avaliação de resultados; qualitativo ou quantitativo. Avaliaremos com base em um baixo nível de falso positivo e falso negativo, sem priorizar um entre os dois, considerando a alta possibilidade de falsa detecção para posições de em pé e deitado, avaliando de forma mais quantitativa do que qualitativa, pois casos de falso positivo ou falsos negativos não são graves. Métrica utilizada para avaliar os resultados quantitativamente - Acurácia, loss e matriz confusão.

## Bases de Dados e Evolução

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Drive Projeto | https://drive.google.com/drive/folders/1zanWzsALmWM7ZpEFpN4s_mhRE8C3CFTW?usp=sharing | Drive com imagens RAW utilizadas no projeto

# Ferramentas

Ferramentas | Endereço na Web | Resumo descritivo
----- | ----- | -----
Draw.io | https://app.diagrams.net/ | Desenho de arquitetura e Workflow
Google Colab | https://colab.research.google.com/ | Notebooks para implementação de código
Google Drive | https://drive.google.com/ | Repositório de Dados e Imagens
GitHub | https://github.com/ | Repositório de Código
Neptune.ai | https://neptune.ai/ | Experiment tracker and model registry

# Workflow

# Experimentos e Resultados preliminares

# Próximos passos

## Referências

http://human-pose.mpi-inf.mpg.de/#dataset

https://www.kaggle.com/datasets/deepshah16/silhouettes-of-human-posture

https://github.com/liruilong940607/OCHumanApi