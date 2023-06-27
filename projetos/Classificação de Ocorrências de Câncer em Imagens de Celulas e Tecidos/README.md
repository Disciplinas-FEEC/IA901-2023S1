# Identificação de Ocorrências de Tumor em Imagens de Tecidos
# Identification of Tumor Occurrences in Tissue Images


## 0. Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*,
oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

|Nome  | RA | Curso|
|--|--|--|
| Eduardo Parducci  | 170272  | Graduação em Eng. de Computação|
| Gianni Shigeru Setoue Liveraro | 265945 | Doutorado em Física Aplicada|
| Pedro Rodrigues Corrêa  | 243236  | Graduação em Física|


## 1. Descrição do Projeto

O câncer é um dos acometimentos mais letais e prevalentes na população mundial, sendo um termo comum que engloba mais de 100 doenças que ocorrem em diferentes órgãos do corpo humano (próstata, pulmão, boca, pele, cólon e etc). A principal característica do câncer é o crescimento desenfreado de células anormais, que eventualmente podem formar tumores e se espalhar para outros órgãos gerando complicações, processo conhecido como metástase [2].

A principal causa para o surgimento dessa doença é a mutação de células comuns, que são alterações na estrutura do DNA contido no núcleo. Existem diversos fatores de risco que podem propiciar a ocorrência destas mutações, como, por exemplo, o consumo de substâncias tóxicas ou exposição a fontes de radiação. Contudo, esse é um fenômeno que também pode ter causas internas, podendo ocorrer em indivíduos por fatores hereditários ou imunológicos. 

Todos os anos, milhares de pessoas são acometidas pelo câncer no Brasil e no mundo, e muitas vidas ainda são perdidas. Uma das formas mais eficazes de tratamento (que pode envolver práticas de radioterapia ou quimioterapia) consiste no diagnóstico precoce, momento ao qual a doença ainda está nos primeiros estágios de desenvolvimento e não gerou complicações para o paciente. Nesta fase, maiores são as chances de sucesso no tratamento e de sobrevivência a longo prazo. O diagnóstico precoce pode ocorrer não apenas por exames de rotina, mas também com abordagens que envolvam procedimentos de biópsia, em que partes do tecido na região acometida pelo câncer são analisadas em microscopia.  É nesse cenário que a capacidade de desenvolver algoritmos capazes de analisar imagens de células em lâminas de tecidos e identificar células cancerígenas se torna extremamente valiosa.

As lâminas de tecidos contêm informações visuais sobre as células e suas características morfológicas. No entanto, a análise manual dessas imagens requer um tempo significativo e está sujeita a variações e a erros humanos. Ao desenvolver algoritmos de análise de imagens, é possível automatizar e agilizar o processo de detecção de células cancerígenas, melhorando a tomada de decisão dos médicos e levando a práticas mais personalizadas no tratamento de cada paciente [3].

Perante o exposto, este projeto consiste em aplicar técnicas de aprendizado de máquina para classificar imagens de lâminas de tecidos de diferentes órgãos. Serão feitas duas classificações: a primeira irá separar as imagens com presença ou não de tumor no tecido a partir da análise de células neoplásicas, que podem estar presentes (indicação de tumor) ou não. A segunda classificação é do tipo de tecido representado pela imagem da lâmina de microscopia entre dezenove classes distintas. Para o primeiro tipo de classificação, serão utilizadas máscaras com a segmentação das células neoplásicas, as quais extraímos a classe binária da imagem (0: não possui célula neoplásica, 1: possui célula neoplásica).

# 2. Metodologia
Para o desenvolvimento do projeto, utilizamos o dataset 'PanNuke', disponibilizado no site Kaggle. A escolha do dataset se deu pelo fato deste ser atualmente o maior e mais diverso dataset para segmentação de núcleos celulares e classificação, o qual foi feito a partir do NuClick. Além disso, ele foi anotado de maneira semi-automática, com a supervisão de profissionais da área para o controle de qualidade [1]. Mais informações sobre as imagens podem ser vistas a seguir.

## 2.1 Bases de Dados e Evolução

Resumo sobre a base: 
O dataset 'PanNuke' consiste em 7901 imagens RGB com dimensões (256, 256, 3) de rotuladas em 19 tipos de tecido humano. Para cada imagem RGB, estão associadas 7 máscaras de segmentação de núcleos celulares também rotuladas. Tanto as imagens dos tecidos quanto as máscaras estão no formato .npy. Os tipos de tecido são Breast, Colon, Lung, Kidney, Prostate, Bladder, Ovarian, Esophagus, Pancreatic, Thyroid, Skin, Adrenal Gland, Cervix, Bile Duct, Testis, Head Neck, Liver, Stomach, Uterus. As máscaras, por sua vez, são imagens de seis bandas. Cada banda carrega a informação da segmentação de algum elemento específico na imagem:

0: Células neoplásicas;
1: Inflamatórias;
2: Células do tecido conectivo/mole;
3: Células mortas;
4: Epiteliais;
6: Background. 

Alguns exemplos podem ser vistos abaixo, assim como a distribuição das imagens.
<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/exemplos dataset.png" height="350">
</p>

<p align="center">
    Figura 1: Algumas imagens do dataset que representam as segmentações dos núcleos celulares, onde cada cor se refere a um tipo de máscara.
</p>

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/freq_tecido.png" height="350">
</p>

<p align="center">
    Figura 2: Distribuição das imagens do dataset por tipo de tecido.
</p>

Atualmente, o dataset 'PanNuke' está disponível em três partes - todas com a mesma estrutura/formato de organização das imagens. Os links para os datasets utilizados no projeto assim como um resumo das suas principais informações podem ser vistas na tabela abaixo: 

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Cancer Instance Segmentation and Classification 1 | https://www.kaggle.com/datasets/andrewmvd/cancer-inst-segmentation-and-classification  | Primeira parte do dataset 'PanNuke'. Contém 2523 imagens de tecidos e as respectivas máscaras de segmentação. Os rótulos de cada tipo de tecido também estão disponíveis.|
Cancer Instance Segmentation and Classification 2 | https://www.kaggle.com/datasets/andrewmvd/cancer-instance-segmentation-and-classification-2 | Segunda parte do dataset, contendo 2656 imagens de tecidos e as respectivas máscaras de segmentação. Os rótulos de cada tipo de tecido também estão disponíveis.|
Cancer Instance Segmentation and Classification 3 | https://www.kaggle.com/datasets/andrewmvd/cancer-instance-segmentation-and-classification-3 | Terceira parte do dataset, contendo 2722 imagens de tecidos e as respectivas máscaras de segmentação. Os rótulos de cada tipo de tecido também estão disponíveis.|

## 2.2 Processamento das imagens

Para facilitar o uso das imagens (e permitir que elas fossem carregadas na memória RAM/GPU dos sistemas operacionais utilizados), desenvolvemos um algoritmo que faz uma cópia local das três partes do dataset 'PanNuke', extraindo e salvando cada imagem, de dentro dos arquivos .npy, no formato .png. Cada imagem foi salva com um número em seu nome, que serve como um identificador ( `Image_*.png`). 

Este mesmo código também faz a leitura da máscara de cada imagem, mais especificamente da banda '0', que corresponde a segmentação de células neoplásicas, visando a classificação. Assim, segue que a variável-classe (presença ou não de células neoplásicas) é construída a partir do cálculo do desvio-padrão (STD) dessa banda. Se STD=0, a imagem de tecido correspondente é classificada como sem células neoplásicas (classe '0', negativa), caso contrário (STD>0), consideramos que a imagem possui células neoplásicas. 

Além das próprias imagens, este código possui como output uma tabela, em que cada linha representa uma imagem. Nela, ainda existem três colunas que representam ID das imagens, Tipo de tecido e Classe (presença ou não de célula neoplásica). 

Abaixo vemos a distribuição dos tecidos que possuem ou não células neoplásicas:

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/freq_tumor.png" height="350">
</p>

<p align="center">
    Figura 4: Distribuição da presença de células neoplásicas (tumores) no conjunto de imagens de tecidos.
</p>

Conclui-se então que para o propósito inicial do projeto, que é a classificação de tecidos com ou sem a presença de células neoplásicas, as quais são tumores, tem-se um dataset equilibrado (entre tecidos com e sem tumor) e totalmente anotado para tal propósito.

### 2.2.1 Análise de data augmentation

Inicialmente, foi realizado um estudo exploratório para identificar os efeitos do processo de data augmentation sobre as imagens dos tecidos. Este passo foi necessário para verificar quais transformações são coerentes com o que se esperaria no processo de aquisição das imagens. 
Nesta análise, as transformações mais tradicionais foram vistas: VerticalFlip, HorizontalFlip, Pad (padding=30), Random Crop (padding mode=’reflect’) e Random Erasing. Os resultados podem ser vistos na Figura 5. Os flips horizontal e vertical preservam a estrutura espacial da imagem original. O Random Crop também preserva grande parte da informação estrutural da imagem, apesar da pequena distorção causada pelo preenchimento de borda do tipo ‘reflect’. Por outro lado, as transformações Pad e Random Erasing criam cenários pouco realistas, introduzindo bordas fixadas ou apagando regiões inteiras - o que pode prejudicar a etapa de treinamento. Em vista disso, excluímos estas transformações do processo de data augmentation de todos os treinamentos contidos neste trabalho.

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Data Augmentation Study/Augmentation_0.png" height="150">
</p>

<p align="center">
    Figura 5: Exemplos de aplicação das transformações de data augmentation (horizontal e vertical flips, Pad, Random Crop e Random Erasing) em uma imagem do conjunto de dados.
</p>


## 2.3 Divisão de treino, teste e validação

Como o projeto envolve treinar algoritmos de aprendizado de máquina, foi necessário dividir o conjunto de imagens em grupos de treino, validação e teste. Portanto, foi desenvolvido um algoritmo que acessa o diretório das imagens ‘.png’ e cria cópias destas imagens (sem repetições) em três novos diretórios: ‘/train’, ‘/val’ e ‘/test’. Todos possuem subdiretórios que representam as classes: ‘/0’ e ‘/1’. Escolhemos essa organização para tirar o máximo de proveito do método DataLoader() da biblioteca PyTorch, que foi usada para os experimentos com Deep Learning. 
    
Em todos os estudos (com exceção daqueles em que o treinamento usava um único tecido), a partição escolhida para os conjuntos foi de 70% treino, 20% teste e 10% validação. Além disso, mantivemos, em cada conjunto, a mesma proporção de tipos de tecido encontradas no dataset original (por exemplo, se no conjunto original de imagens tivéssemos 30% delas sendo do pulmão; nos conjuntos de treino, teste e validação teremos a mesma proporção). 

## 2.4 Experimentos
	
Nesta etapa, utilizamos os conjuntos de treino, teste e validação para fazer as análises com técnicas de Deep Learning. Uma descrição sucinta destas abordagens pode ser vista abaixo. 

Para tais análises recorremos, em um primeiro momento, a uma abordagem envolvendo o método de Transfer Learning. A arquitetura escolhida foi a EfficientNet_B0, a qual obteve um melhor desempenho dentre as outras arquiteturas testadas. O método DataLoader foi empregado para carregar na memória as imagens processadas dos diretórios e aplicar as transformações necessárias. Uma etapa de resize necessário para tamanho 224 x 224 por conta do tamanho de entrada da EfficientNet_B0. 

Alguns sub experimentos, testando diferentes configurações de hiperparâmetros, foram feitos visando um ajuste ótimo da rede neural. Ao fim deste processo fixamos para todos os treinamentos, que envolveram tarefas de classificação, os seguintes hiperparâmetros:


- Learning Rate: 0.0001
- Optimizer: ADAM
- N Epochs: 20 
- Loss Function: Cross Entropy

Finalmente, ajustamos uma semente aleatória igual à 42 para garantir reprodutibilidade em todos os estudos. 

A seguir, todos os estudos e experimentos feitos serão detalhados.

#### 2.4.1 Classificação de Tumores

No primeiro tipo de classificação realizado no projeto, o de tumores, são utilizadas as máscaras disponibilizadas no dataset, que rotulam, dentre outros canais, a presença de tecido neoplásico, isto é, um tumor. Então, ao associar tal imagem a uma das duas classes retiradas dessa máscara (com tumor ou sem tumor), pode-se então treinar o algoritmo de DL para classificar imagens não vistas no treinamento. Mesmo que a máquina não utilize dos mesmos critérios que um ser humano utilizaria para determinar tal presença ou não, como citado em [4], ela será capaz de aprender a identificar certos padrões e utilizá-los, então, para cumprir seu objetivo.

##### 2.4.1.1 Experimento I (Baseline)

Neste experimento, utilizamos todos os tecidos nas etapas de treinamento, validação e testes. O objetivo foi verificar a performance do modelo de Deep Learning no cenário mais básico possível, em termos de dataset. 
Adicionalmente, neste experimento, verificamos o quanto o modelo treinado acertava na tarefa de classificação considerando os diferentes tipos de tecido. A pergunta a ser respondida era: será que algum tecido é mais desafiador para o modelo classificar?

<p align="middle">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/Baseline/Cópia de EpochsxAccuracy.png" height="300">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/Baseline/Cópia de EpochsxLoss.png" height="300">
</p>
Fig. 6. Curvas de Loss (Cross Entropy) e Acurácia em função do número de épocas para o treinamento da EfficientNetB0 neste estudo.  


##### 2.4.1.1 Experimento II
	
Neste experimento, treinamos o modelo de Deep Learning com as imagens de todos os tecidos, menos o tecido ‘Breast’, que foi separado para ser utilizado apenas na fase de testes. Esta escolha se deu pelo fato do tecido ‘Breast’ ser o mais populoso do dataset (>2000 imagens). 
Portanto, a pergunta a ser respondida neste experimento foi: o modelo de Deep Learning é capaz de generalizar e aprender a reconhecer células neoplásicas em um tipo de tecido não visto durante o treinamento? 

##### 2.4.1.1 Experimento III

Neste experimento, treinamos o modelo somente com as imagens do tecido ‘Breast’, enquanto os demais tecidos foram utilizados como conjunto teste. Pelo mesmo motivo do experimento anterior, a escolha do tecido ‘Breast’ se deu por ser aquele mais populoso do dataset. Assim, a pergunta a ser respondida neste experimento foi: o modelo de Deep Learning é capaz de aprender e generalizar a presença de células neoplásicas no restante dos tecidos sendo que foi treinado somente com um deles?

#### 2.4.2 Classificação de Tecidos

Para o segundo tipo de classificação do projeto, o de tipos de tecidos, assim como no primeiro, fez-se o treinamento com as imagens rotuladas do dataset com base no seu tipo. Enquanto nós, humanos, somos capazes de diferenciar tipos de tecido com base em algumas características de seu estrutura, como discutido em [5], a máquina, assim como no caso dos tumores, irá aprender a identificar tais padrões para, assim, conseguir predizer o tipo daquele tecido.

Neste estudo, utilizamos a EfficientNetB0 em vista dos seus bons resultados no estudo anterior e por ser  pequena o suficiente para treinamentos no ambiente do Google Collaboratory. Os hiperparâmetros hiperparâmetros usados em todos os experimentos anteriores
		- O conjunto de imagens foi dividido seguindo as mesmas proporções dos experimentos anteriores:
70% treinamento
10% validação
20% teste

Ao todo, temos imagens de 19 tipos de tecidos disponíveis no banco de dados.
A discriminação do tipo de tecido, neste caso, configura um problema de classificação multi-classe
Neste cenário, existem pelo menos duas abordagens para se atacar este problema:
One vs All: O problema multiclasse é transformado em um problema de classificação binária, onde uma categoria é tida como “positiva” e todas as demais são tidas como “negativas”. O problema desta abordagem é que é necessário treinar um modelo para cada combinação possível de classes. Por outro lado, a vantagem é que se torna possível aplicar métricas da classificação binária (ROC Curve, AUC, TPR, FPR e etc) nas análises, que são facilmente interpretadas. 
All vs All: Um único modelo é treinado para discriminar todas as categorias possíveis. A dificuldade desta abordagem reside na forma de mensurar a qualidade das predições. Por outro lado, a vantagem é o treino e uso de um único modelo. 

#### 2.4.2.1 Experimento I

Treinamento para discriminar 'Breast' dos demais tecidos (One vs All)

#### 2.4.2.1 Experimento II

Treinamento para discriminar 'Colon' dos demais tecidos (One vs All)

#### 2.4.2.1 Experimento III

Treinamento para discriminar seis tecidos - Breast, Colon, Esophagus, HeadNeck, Adrenal_gland e Bile-duct (estratégia "All vs All")

<p align="middle">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Tissue Classification/Experiment_III/EpochsxAccuracy.png" height="300">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Tissue Classification/Experiment_III/EpochsxLoss.png" height="300">
</p>
Fig. 7. Curvas de Loss (Cross Entropy) e Acurácia em função do número de épocas para os grupos treino e teste no treinamento da EfficientNetB0 neste estudo.  


#### 2.4.3 Contagem de células

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cell Counting/Cópia de EpochsxLoss.png" height="350">
</p>

<p align="center">
    Figura 8: Curvas de Loss (Mean Squared Error) e Acurácia em função do número de épocas para os grupos treino e teste no treinamento da EfficientNetB0 neste estudo.
</p>

## 2.5 Análise de dados

### 2.5.1 Problema de classificação binário
As técnicas de classificação podem fornecer a probabilidade P de uma observação pertencer a uma determinada classe. Pelo fato desta saída probabilística P ser contínua e restrita ao intervalo [0, 1], a classificação em si ocorre ao se determinar um parâmetro livre conhecido como Decision Threshold, que representa um valor de corte sobre as probabilidades. Considerando um cenário com duas classes, uma observação é classificada como positiva se P ≥Decision Threshold - caso contrário, ela é rotulada como sendo negativa. Cada valor de Decision Threshold produz uma matriz de confusão diferente, modificando também as suas métricas de desempenho. Mesmo assim, ainda é possível avaliar a performance geral de classificadores binários recorrendo a um método conhecido como ROC Curve, que não depende da escolha de qualquer limiar sobre as probabilidades. Resumidamente: A ROC Curve correlaciona os valores de True Positive Rate (TPR) e False Positive Rate (FPR) para todos os valores possíveis de Decision Threshold [Ref].Uma quantidade que sintetiza as informações das ROC Curves é a Area Under the Curve (AUC), que varia no intervalo $[0, 1]$.
Mesmo recorrendo às ROC Curves para fazer avaliações gerais dos modelos, é fato que, na prática, a qualidade das classificações depende fortemente do valor escolhido para o Decision Threshold. Algumas análises adotam o seu valor padrão de $0.5$. No entanto, o ideal é que a escolha desse limiar leve em consideração as demandas e particularidades de cada estudo. Em situações em que os erros de classificação possuem um custo alto, pode ser mais adequado trabalhar com valores mais elevados de Decision Threshold. Por outro lado, se os erros de classificação forem menos importantes do que identificar a classe positiva, pode ser mais interessante recorrer a Decision Thresholds menores. De todo modo, existem algumas figuras de mérito que podem ser empregadas para otimizar essa escolha, tais como:

$$\textrm{Youden's Index} = TPR - FPR $$

$$\textrm{F1-Score} = 2*\frac{Precision*TPR}{Precision+TPR}$$

$$\textrm{G-Mean} = \sqrt{TPR*(1 - FPR)} $$

Nesse caso, o Decision Threshold escolhido deve ser aquele que maximiza as relações acima, por representar o valor de corte em que a quantidade de acertos do classificador é máxima ou equilibrada com relação aos seus erros. 

Portanto, todas estas métricas (TPR, FPR e AUC) serão usadas em nossas análises. Adicionalmente, usaremos outras métricas de classificação conhecidas, tais como: 

  Acurácia: porcentagem de observações classificadas corretamente 

  Precisão: porcentagem de observações classificadas como positivas que são realmente positivas. 

Em geral, para o cálculo delas, consideramos o valor de Decision Threshold que maximiza uma das três figuras de mérito apresentadas. 

### 2.5.2 Problema de classificação multi-classe

Para o problema multiclasse, 

### 2.5.3 Problema de Regressão

## 2.6 Ferramentas

Para a organização e visualização dos dados do dataset, foram utilizadas as bibliotecas Pandas, Numpy e Matplotlib. Para a confecção do workflow do projeto, o grupo utilizou a ferramenta de desenho de workflows Draw.io. Para a execução do projeto em si, isto é, as classificações da imagens, irão ser utilizadas as bibliotecas PyTorch, para a parte de Deep Learning, e o SciKit-Learn para a parte de algoritmos tradicionais de machine learning voltados à classificação.
Todo o projeto tem sido desenvolvido, em linguagem Python, no formato de Notebooks do Google Colaboratory - com uso de GPUs/CPUs. Adicionalmente, todos os arquivos (raw, intermediários e finais) têm sido salvos na plataforma Google Drive - sendo, eventualmente, repassados para o Github. 

Os detalhemento completo sobre todos os pacotes/bibliotecas utilizadas assim como suas versões pode ser encontrada nao diretório /src. Instruções para instalação também estão inclusas. 

# 3. Workflow

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/workflow_2.png" height="350">
</p>

# 4. Resultados Finais

Nesta seção, apresentamos os resultados finais do projeto, considerando todos os experimentos realizados. 

## 4.1 Classificação de Tumores

### 4.1.1 Experimento Baseline: 
#### 4.1.1.1 Performance Geral
A Figura 5 apresenta a ROC Curve comparando o experimento Baseline (treinamento/validação/teste com todos os tecidos) com o experimento 1 (treinamento/validação com todos os tecidos, exceto ‘Breast’ que foi usado apenas para os testes). No cenário Baseline, o modelo de Deep Learning apresentou um desempenho elevado (AUC=0.97), indicando que mesmo sem qualquer tipo de pré-processamento, foi possível identificar a existência de células neoplásicas na maior parte das imagens de teste. 
Já no experimento 1, a EfficientNet_B0 apresentou uma queda de performance em comparação com o cenário baseline (AUC=0.917). Mesmo assim, esta ainda é uma performance razoavelmente alta - o que é um indício de que um modelo de Deep Learning é capaz de generalizar e identificar padrões em imagens não vistas durante o treinamento. 

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/Baseline/Cópia de ROC.png" height="350">
</p>
Fig. 9. ROC Curve comparando o modelo de Deep Learning no cenário baseline (treino e teste com todos os tecidos) com o experimento baseline (treino e teste com todos os tecidos). 

A Figura 6 mostra os gráficos de True Positive Rate e False Positive Rate em função do Decision Threshold. Em geral, para todo o intervalo de Decision Threshold, tanto o caso Baseline quanto no experimento 1, as curvas de False Positive Rate são praticamente iguais. A grande diferença entre os modelos é, portanto, no True Positive Rate - que é consideravelmente maior no cenário Baseline.

A Tabela 1 sintetiza algumas métricas de desempenho, para os dois estudos, considerando também o valor de Decision Threshold que maximiza o Índice de Youden. É possível ver que, em geral, os valores obtidos de acurácia e precisão também são elevados (>87%). 

<p align="middle">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/Baseline/Cópia de TPRxThreshold.png" height="300">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/Baseline/Cópia de FPRxThreshold.png" height="300">
</p>
Fig. 10. True Positive Rate e False Positive Rate em função do Decision Threshold para os dois estudos.  


Tab. 1. Síntese das principais métricas de performance para os estudos: Baseline e experimento 1. 
|Estudos|AUC|TPR*|FPR*|Precision*|Accuracy*|F1-score*|D. Threshold*|
|---|---|---|---|---|---|---|---|
|Baseline|0\.974|0\.94|0\.07|0\.93|0\.94|0\.93|0\.22|
* Métricas calculadas com base no valor ótimo (máximo) do F1-score, que retornou o resultado com o menor D. Threshold. 

#### 4.1.1.2 Análise de desempenho por tecido

A Figura 7 mostra a performance do modelo baseline para diferentes tecidos. Apenas aquelas com as três maiores (Stomach, Lung, Prostate) e três menores (Uterus, HeadNeck, Bile-duct) performances estão representadas. Para as maiores performances, temos AUCs=1 - indicando uma classificação perfeita dos tecidos. Nos piores casos, temos AUC~0.92, que é uma performance considerada razoável para um classificador. A Tabela 2 mostra o resultado para todos os tecidos e outras métricas de desempenho.Por fim, na próxima subseção, exibimos alguns exemplos de imagens cuja a rede neural errou a classificação - porém, não conseguimos detectar padrões que fizeram ela errar as classificações.

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/FinalComparison/ROCAllTissues_Baseline.png" height="350">
</p>
Fig. 11. ROC Curve comparando a performance do modelo baseline para diferentes tecidos. Apenas aquelas com as três maiores (Skin, Thyroid, Esophagus) e três menores (Liver, Bile-duct, Lung) performances estão representadas. 


Tab. 2. Síntese das principais métricas de performance para o estudo Baseline considerando os diferentes tecidos.
|N\. amostras|Types|AUC|TPR*|FPR*|Precision*|Accuracy*|F1-Score*|
|---|---|---|---|---|---|---|---|
|37|Skin|1\.0|1\.0|0\.0|1\.0|1\.0|1\.0|
|45|Thyroid|0\.997|1\.0|0\.09|0\.92|0\.93|0\.96|
|84|Esophagus|0\.997|0\.98|0\.08|0\.92|0\.95|0\.95|
|35|Prostate|0\.99|1\.0|0\.23|0\.81|0\.91|0\.9|
|39|Testis|0\.989|0\.86|0\.0|1\.0|0\.92|0\.92|
|26|Kidney|0\.988|0\.88|0\.1|0\.9|0\.88|0\.89|
|58|Cervix|0\.987|0\.95|0\.06|0\.94|0\.95|0\.94|
|87|Adrenal\_gland|0\.983|0\.98|0\.03|0\.97|0\.98|0\.97|
|76|HeadNeck|0\.978|0\.89|0\.05|0\.95|0\.92|0\.92|
|470|Breast|0\.972|0\.95|0\.1|0\.9|0\.93|0\.92|
|29|Stomach|0\.966|0\.94|0\.08|0\.92|0\.93|0\.93|
|37|Uterus|0\.965|0\.96|0\.09|0\.91|0\.95|0\.93|
|39|Pancreatic|0\.964|0\.85|0\.08|0\.91|0\.9|0\.88|
|29|Bladder|0\.963|1\.0|0\.06|0\.94|0\.97|0\.97|
|29|Ovarian|0\.961|0\.94|0\.08|0\.92|0\.93|0\.93|
|288|Colon|0\.938|0\.86|0\.01|0\.99|0\.96|0\.92|
|44|Liver|0\.93|0\.87|0\.0|1\.0|0\.93|0\.93|
|84|Bile-duct|0\.913|0\.92|0\.33|0\.74|0\.82|0\.82|
|36|Lung|0\.886|1\.0|1\.0|0\.5|0\.97|0\.67|
* Métricas calculadas com base no valor ótimo (máximo) do F1-score do modelo Baseline junto aos dados de todos os tecidos. 


#### 4.1.1.3 Identificando padrões nas imagens classificadas incorretamente

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/Baseline/Cópia de WrongPredictions_Image_4732.png" height="250">
</p>

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/Baseline/Cópia de WrongPredictions_Image_4130.png" height="250">
</p>

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/Baseline/Cópia de WrongPredictions_Image_3654.png" height="250">
</p>

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/Baseline/Cópia de WrongPredictions_Image_2356.png" height="250">
</p>


<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/Baseline/Cópia de WrongPredictions_Image_2156.png" height="250">
</p>

Fig. 12. Exemplos de imagens de diferentes tecidos classificadas incorretamente e suas respectivas masks. 


### 4.1.2 Comparação entre experimentos


<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/FinalComparison/Cópia de ROC_GeneralAnalysis.png" height="350">
</p>
Fig. 11. ROC Curve comparando a performance do modelo baseline com o experimentos I e II. 

Tab. 3. Síntese das principais métricas de performance para os três estudos envolvendo a identificação de células neoplásicas nos tecidos.
|Estudo|AUC|TPR*|FPR*|Precision*|Accuracy*|F1-Score*|
|---|---|---|---|---|---|---|
|Baseline|0\.974|0\.94|0\.07|0\.93|0\.94|0\.93|
|Experiment I|0\.859|0\.59|0\.07|0\.89|0\.72|0\.71|
|Experiment II|0\.852|0\.92|0\.42|0\.69|0\.75|0\.79|
* Métricas calculadas com base no valor ótimo (máximo) do F1-score do modelo Baseline junto aos dados de todos os tecidos. 

#### 4.1.2.1 Performance entre tecidos para o experimento II


<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cancer Classification/FinalComparison/Cópia de ROC_TissueAnalysis.png" height="350">
</p>
Fig. 12. ROC Curve comparando a performance do modelo obtido no experimento II para diferentes tecidos. Apenas aquelas com as três maiores e três menores  performances estão representadas. 

## 4.2 Classificação de Tecidos

## 4.2.1 Experimentos I e II (One vs All)

Tab. 4. Síntese das principais métricas de performance para os experimentos I e II, que usam uma abordagem One vs All para a classificação de tecidos. 

|Estudo|AUC|TPR*|FPR*|Precision*|Accuracy*|F1Score*|
|---|---|---|---|---|---|---|
|Experiment\_I|0\.995|0\.99|0\.0|1\.0|0\.99|0\.99|
|Experiment\_II|0\.995|0\.99|0\.0|1\.0|0\.99|0\.99|
* Métricas calculadas com o valor default do decision threshold (=0.5).


## 4.2.2 Experimento III (All vs All)


<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Tissue Classification/Experiment_III/CM.png" height="450">
</p>
Fig. 13. Matriz de confusão da EfficientNetB0 treinada para classificar todos os tecidos.

General accuracy:  0.9739
General precision: 0.9661
General F1 score:  0.9570


Tab. 4. Síntese das principais métricas de performance para a EfficientNet_B0 aplicada na classificação de cada tecido.

|Classe|precision|recall|f1-score|N. de amostras|
|---|---|---|---|---|
|Adrenal\_gland|0\.9666666666666667|1\.0|0\.983050847457627|87\.0|
|Bile-duct|0\.9120879120879121|0\.9880952380952381|0\.9485714285714287|84\.0|
|Lung|0\.9210526315789473|0\.9722222222222222|0\.9459459459459458|36\.0|
|Ovarian|0\.9310344827586207|0\.9310344827586207|0\.9310344827586207|29\.0|
|Pancreatic|0\.9736842105263158|0\.9487179487179487|0\.9610389610389611|39\.0|
|Prostate|0\.9705882352941176|0\.9705882352941176|0\.9705882352941176|34\.0|
|Skin|0\.9166666666666666|0\.8918918918918919|0\.9041095890410958|37\.0|
|Stomach|1\.0|1\.0|1\.0|29\.0|
|Testis|0\.9487179487179487|0\.9487179487179487|0\.9487179487179487|39\.0|
|Thyroid|1\.0|0\.9333333333333333|0\.9655172413793104|45\.0|
|Uterus|0\.9705882352941176|0\.8918918918918919|0\.9295774647887325|37\.0|
|Bladder|1\.0|0\.8275862068965517|0\.9056603773584906|29\.0|
|Breast|0\.9873417721518988|0\.9957446808510638|0\.9915254237288136|470\.0|
|Cervix|0\.9649122807017544|0\.9482758620689655|0\.9565217391304347|58\.0|
|Colon|0\.9829351535836177|1\.0|0\.9913941480206541|288\.0|
|Esophagus|1\.0|0\.9404761904761905|0\.9693251533742331|84\.0|
|HeadNeck|0\.9743589743589743|1\.0|0\.9870129870129869|76\.0|
|Kidney|0\.9583333333333334|0\.8846153846153846|0\.9199999999999999|26\.0|
|Liver|0\.9761904761904762|0\.9318181818181818|0\.9534883720930233|44\.0|


## 4.3 Contagem de células

### 4.3.1 Desempenho geral e por tecido

Tab. 5. Comparação de atributos estatísticos (Mean, standard-deviation (STD), Median, Min e Max) das distribuições dos dados reais e preditos pela EfficientNet_B0. Análise feita para o número de células totais e neoplásicas. Para as predições, foram calculados os valores de Mean Squared Error (MSE) e Mean Absolute Error (MAE). 

| EfficientNet_B0 performance w.r.t the Test images (N=1571) |
| ---------------------------------------------------------- |        
|                                                            | Actual | Predicted |
| Feature                                                    | Mean | STD | Median | Min | Max | Mean | STD | Median | Min | Max | MAE | MSE |
| N. of

Neoplasic Cells                                     | 9.21 | 13.97 | 1 | 0 | 112 | 9.36 | 12.91 | 3 | 0 | 100 | 2.2 | 16.8 |
| N. of Total Cells                                          | 23.71 | 20.49 | 19 | 0 | 196 | 23.17 | 20.24 | 19 | 0 | 225 | 2.7 | 16.4 |

<p align="middle">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cell Counting/Cópia de ScatterTotalCells.png" height="300">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cell Counting/Cópia de ScatterTotalNeoplasic.png" height="300">
</p>
Fig. 14. Comparação entre os valores preditos do número total de células (gráfico superior) e de células neoplásicas (gráfico inferior) pela EfficientNet_B0, assim como os valores esperados para a distribuição das imagens da amostra de testes. O gráfico da esquerda mostra a correlação entre as predições e os seus respectivos valores verdadeiros. A linha diagonal tracejada, que indica um regressor ideal, foi incluída para comparação. Por completeza, o gráfico da direita mostra a correlação dos valores preditos com a diferença entre as predições e os valores esperados. 

<p align="middle">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cell Counting/Cópia de BoxPlotTotalCells.png" height="300">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cell Counting/Cópia de BoxPlotTotalNeoplasic.png" height="300">
</p>
Fig. 15. Boxplots representando a distribuição do Erro Absoluto cometido pela EfficientNet_B0 com relação a todos os tecidos da amostra de testes na contagem do número total de células (gráfico superior) e de células neoplásicas (gráfico inferior). As linhas amarelas indicam a mediana enquanto os triângulos verdes representam o Mean Absolute Error (MAE). A linha azul tracejada (MAE=12) indica a performance obtida na referência [6] e foi incluída para comparação.

### 4.3.1 Inspeção visual das predições feitas pela EfficientNet_B0

Abaixo, temos alguns exemplos de imagens com as respectivas masks relacionadas com a performance da  EfficientNet_B0. Olhando as imagens, podemos concluir que:
Em alguns casos, o modelo foi capaz de reconhecer com perfeição todas as estruturas dos tecidos. Identificamos também que a reden neural apresentou uma Dificuldade maior em diferenciar as células neoplásicas das demais (especialmente as inflamatórias e epiteliais)

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cell Counting/Cópia de CellCounts_Image_7504.png" height="250">
</p>
<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cell Counting/Cópia de CellCounts_Image_4591.png" height="250">
</p>
<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cell Counting/Cópia de CellCounts_Image_6435.png" height="250">
</p>
<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/Cell Counting/Cópia de CellCounts_Image_4533.png" height="250">
</p>

Fig. 16. Exemplos de imagens de diferentes tecidos classificadas incorretamente e suas respectivas masks. 

# 5. Conclusão e futuro


<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Entrega 3/ProjectConclusion.png" height="250">
</p>

## Referências 

[1]: G., Jevgenij et. al,  “PanNuke Dataset Extension, Insights and Baselines”, 2020. 

[2]: Defining Cancer. National Cancer Institute

[3]: Bhuiyan MR, Abdullah J. Detection on Cell Cancer Using the Deep Transfer Learning and Histogram Based Image Focus Quality Assessment. Sensors (Basel). 2022 
Sep 16;22(18):7007. doi: 10.3390/s22187007. PMID: 36146356; PMCID: PMC9504738.

[4]: Jaber, N. "Can Artificial Intelligence Help See Cancer in New, and Better, Ways?" (cancer.gov/news-events/cancer-currents-blog/2022/artificial-intelligence-cancer-imaging). March 22, 2022.

[5]: Rachel. "Classification and Types of Epithelial Tissues" (rsscience.com/epithelium-classification-and-types/)

[6]: Lavitt, Falko, et al. "Deep learning and transfer learning for automatic cell counting in microscope images of human cancer cell lines." Applied Sciences 11.11 (2021): 4912.


