# Identificação de Ocorrências de Tumor em Imagens de Células e Tecidos
# Identification of Tumor Occurrences in Cell and Tissue Images


## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*,
oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).


> |Nome  | RA | Curso|
> |--|--|--|
> | Eduardo Parducci  | 170272  | Graduação em Eng. de Computação|
> | Gianni Shigeru Setoue Liveraro | 265945 | Doutorado em Física Aplicada|
> | Pedro Rodrigues Corrêa  | 243236  | Graduação em Física|


## Descrição do Projeto

O câncer é um dos acometimentos mais letais e prevalentes na população mundial, sendo um termo comum que engloba mais de 100 doenças que ocorrem em diferentes órgãos do corpo humano (próstata, pulmão, boca, pele, cólon e etc). A principal característica do câncer é o crescimento desenfreado de células anormais, que eventualmente podem formar tumores e se espalhar para outros órgãos gerando complicações, processo conhecido como metástase [2].

A principal causa para o surgimento desta doença é a mutação de células comuns, que são alterações na estrutura do DNA contido no núcleo. Existem diversos fatores de risco que podem propiciar a ocorrência destas mutações, como o consumo de substâncias tóxicas ou exposição a fontes de radiação, por exemplo - contudo, este é um fenômeno que também pode ter causas internas, podendo ocorrer em indivíduos por fatores hereditários e imunológicos. 

Todos os anos, milhares de pessoas são acometidas pelo câncer no Brasil e no mundo, e muitas vidas ainda são perdidas. Uma das formas mais eficazes de tratamento (que pode envolver práticas de radioterapia ou quimioterapia) consiste no diagnóstico precoce, momento ao qual a doença ainda está nos primeiros estágios de desenvolvimento e não gerou complicações para o paciente. Nesta fase, maiores são as chances de sucesso no tratamento e de sobrevivência a longo prazo. O diagnóstico precoce pode ocorrer não apenas por exames de rotina, mas também com abordagens que envolvam procedimentos de biópsia, em que partes do tecido na região acometida pelo câncer são analisadas em microscopia.  É nesse cenário que a capacidade de desenvolver algoritmos capazes de analisar imagens de células em lâminas de tecidos e identificar células cancerígenas se torna extremamente valiosa.

As lâminas de tecidos contêm informações visuais sobre as células e suas características morfológicas. No entanto, a análise manual dessas imagens requer um tempo significativo e está sujeita a variações e erros humanos. Ao desenvolver algoritmos de análise de imagens, é possível automatizar e agilizar o processo de detecção de células cancerígenas, melhorando a tomada de decisão dos médicos e levando a práticas mais personalizadas no tratamento de cada paciente [3].

Perante o exposto, este projeto consiste em aplicar técnicas de aprendizado de máquina para classificar imagens de lâminas de tecidos de diferentes órgãos. Serão feitas duas classificações: a primeira irá separar as imagens com presença ou não de tumor no tecido a partir da análise de células neoplásicas, que podem estar presentes (indicação de tumor) ou não; a segunda classificação é do tipo de tecido representado pela imagem da lâmina de microscopia entre dezenove classes distintas. Para o primeiro tipo de classificação, serão utilizadas máscaras com a segmentação das células neoplásicas, as quais extraímos a classe binária da imagem (0: não possui célula neoplásica, 1: possui célula neoplásica).

Finalmente, como objetivo secundário do projeto, buscaremos comparar a performance de classificação de duas abordagens. A primeira consiste no uso de um modelo de Deep Learning, o qual fará a extração de atributos automaticamente e, posteriormente, a classificação das imagens; enquanto a segunda envolve extração manual de atributos e a classificação das imagens com algoritmos tradicionais de Machine Learning. 

# Metodologia
Para o desenvolvimento do projeto, utilizamos o dataset 'PanNuke', disponibilizado no site Kaggle. Mais informações sobre as imagens podem ser vistas a seguir.

## Bases de Dados e Evolução

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

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/distribuicao_mascaras.png" height="350">
</p>

<p align="center">
    Figura 3: Distribuição dos tipos de máscaras no dataset por tipo de tecido. O número à direita representa a quantidade de núcleos celulares segmentados para aquele tipo de máscara [1].
</p>

Atualmente, o dataset 'PanNuke' está disponível em três partes - todas com a mesma estrutura/formato de organização das imagens. Os links para os datasets utilizados no projeto assim como um resumo das suas principais informações podem ser vistas na tabela abaixo: 

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Cancer Instance Segmentation and Classification 1 | https://www.kaggle.com/datasets/andrewmvd/cancer-inst-segmentation-and-classification  | Primeira parte do dataset 'PanNuke'. Contém 2523 imagens de tecidos e as respectivas máscaras de segmentação. Os rótulos de cada tipo de tecido também estão disponíveis.|
Cancer Instance Segmentation and Classification 2 | https://www.kaggle.com/datasets/andrewmvd/cancer-instance-segmentation-and-classification-2 | Segunda parte do dataset, contendo 2656 imagens de tecidos e as respectivas máscaras de segmentação. Os rótulos de cada tipo de tecido também estão disponíveis.|
Cancer Instance Segmentation and Classification 3 | https://www.kaggle.com/datasets/andrewmvd/cancer-instance-segmentation-and-classification-3 | Terceira parte do dataset, contendo 2722 imagens de tecidos e as respectivas máscaras de segmentação. Os rótulos de cada tipo de tecido também estão disponíveis.|

## Passo 1: Extração de dados

Para facilitar o uso das imagens (e permitir que elas fossem carregadas na memória RAM/GPU dos sistemas operacionais utilizados), desenvolvemos um algoritmo que faz uma cópia local das três partes do dataset 'PanNuke', extraindo e salvando cada imagem, de dentro dos arquivos .npy, no formato .png. Cada imagem foi salva com um número em seu nome, que serve como um identificador ('Image_*.png'). 

Este mesmo código também faz a leitura da máscara de cada imagem, mais especificamente da banda '0', que corresponde a segmentação de células neoplásicas. Disto, segue que a variável-classe (presença ou não de células neoplásicas) é construída a partir do cálculo do desvio-padrão (STD) desta banda. Se STD=0, a imagem de tecido correspondente é classificada como sem células neoplásicas (classe '0', negativa), caso contrário (STD>0), consideramos que a imagem possui células neoplásicas. 

Além das próprias imagens, este código possui com output uma tabela, em que cada linha representa uma imagem. Nela, ainda existem três colunas que representam: ID das imagens, Tipo de tecido e classe (presença ou não de célula neoplásica). 

 Abaixo vemos a distribuição dos tecidos que possuem ou não células neoplásicas:

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/freq_tumor.png" height="350">
</p>

<p align="center">
    Figura 4: Distribuição da presença de células neoplásicas (tumores) no conjunto de imagens de tecidos.
</p>

Conclui-se então que para o propósito inicial do projeto, que é a classificação de tecidos com ou sem a presença de células neoplásicas, as quais são tumores, tem-se um dataset equilibrado (entre tecidos com e sem tumor) e totalmente anotado para tal propósito.

## Passo 2: Divisão de treino, teste e validação

Como o projeto envolve treinar algoritmos de aprendizado de máquina, foi necessário dividir o conjunto de imagens em grupos de treino, validação e teste. Portanto, foi desenvolvido um algoritmo que acessa o diretório das imagens ‘.png’ e cria cópias destas imagens (sem repetições) em três novos diretórios: ‘/train’, ‘/val’ e ‘/test’. Todos possuem subdiretórios que representam as classes: ‘/0’ e ‘/1’. Escolhemos esta organização para tirar o máximo de proveito do método DataLoader() da biblioteca PyTorch, que foi usada para os experimentos com Deep Learning. 
    
A partição escolhida para os conjuntos foi de 70% treino, 20% teste e 10% validação. Além disso, mantivemos, em cada conjunto, a mesma proporção de tipos de tecido encontradas no dataset original (por exemplo, se no conjunto original de imagens tivéssemos 30% delas sendo do pulmão; nos conjuntos de treino, teste e validação teremos a mesma proporção). 

## Passo 3: Experimentos
	
Nesta etapa, utilizamos os conjuntos de treino, teste e validação para fazer as análises com técnicas de Deep Learning e Machine Learning (via extração de atributos). Uma descrição sucinta destas abordagens pode ser vista abaixo. 

#### Análise com Deep Learning

Para as análises de Deep Learning recorremos, em um primeiro momento, a uma abordagem envolvendo o método de Transfer Learning. A arquitetura escolhida foi a EfficientNet_B0, que foi carregada e treinada via PyTorch. O método DataLoader foi empregado para carregar na memória as imagens processadas dos diretórios e aplicar as transformações necessárias. 

Alguns sub experimentos, testando diferentes configurações de hiperparâmetros, foram feitos visando um ajuste ótimo da rede neural. Ao fim deste processo, fixamos para todos os treinamentos os seguintes hiperparâmetros:


- Learning Rate: 0.0001
- Optmizer: ADAM
- N Epochs: 20 


E uma semente aleatória igual à 42 foi utilizada para garantir reprodutibilidade. Em todos os casos, usamos Data Augmentation, com métodos de Random Crop, Flips horizontais e verticais, Pad e Random Erasing. 

Dois experimentos principais foram realizados neste estudo. A sua descrição detalhada pode ser vista a seguir:

##### Baseline

Neste experimento, utilizamos todos os tecidos nas etapas de treinamento, validação e testes. O objetivo foi verificar a performance do modelo de Deep Learning no cenário mais básico possível, em termos de dataset. 
 Adicionalmente, neste experimento, verificamos o quanto o modelo treinado acertava na tarefa de classificação considerando os diferentes tipos de tecido - a pergunta a ser respondida era: será que algum tecido é mais desafiador para o modelo classificar?

##### Experimento I:
	
Neste experimento, treinamos o modelo de Deep Learning com as imagens de todos os tecidos, menos o tecido ‘Breast’, que foi separado para ser utilizado apenas na fase de testes. Esta escolha se deu pelo fato do tecido ‘Breast’ ser o mais populoso do dataset (>2000 imagens). 
Portanto, a pergunta a ser respondida neste experimento foi: será que o modelo de Deep Learning é capaz de generalizar e aprender a reconhecer células neoplásicas em um tipo de tecido não visto durante o treinamento? 

#### Análise com técnicas tradicionais

##### Extração de atributos
`<Em construção>`

##### Treinamento dos modelos
`<Em construção>`

## Passo 4: Análise de desempenho

As técnicas de classificação podem fornecer a probabilidade P de uma observação pertencer a uma determinada classe. Pelo fato desta saída probabilística P ser contínua e restrita ao intervalo [0, 1], a classificação em si ocorre ao se determinar um parâmetro livre conhecido como Decision Threshold, que representa um valor de corte sobre as probabilidades. Considerando um cenário com duas classes, uma observação é classificada como positiva se P ≥Decision Threshold - caso contrário, ela é rotulada como sendo negativa. Cada valor de Decision Threshold produz uma matriz de confusão diferente, modificando também as suas métricas de desempenho. Mesmo assim, ainda é possível avaliar a performance geral de classificadores binários recorrendo a um método conhecido como ROC Curve, que não depende da escolha de qualquer limiar sobre as probabilidades. Resumidamente: A ROC Curve correlaciona os valores de True Positive Rate (TPR) e False Positive Rate (FPR) para todos os valores possíveis de Decision Threshold [Ref].Uma quantidade que sintetiza as informações das ROC Curves é a Area Under the Curve (AUC), que varia no intervalo $[0, 1]$.
Mesmo recorrendo às ROC Curves para fazer avaliações gerais dos modelos é fato que, na prática, a qualidade das classificações depende fortemente do valor escolhido para o Decision Threshold. Algumas análises adotam o seu valor padrão de $0.5$. No entanto, o ideal é que a escolha deste limiar leve em consideração as demandas e particularidades de cada estudo. Em situações em que os erros de classificação possuem um custo alto, pode ser mais adequado trabalhar com valores mais elevados de Decision Threshold. Por outro lado, se os erros de classificação forem menos importantes do que identificar a classe positiva, pode ser mais interessante recorrer a Decision Thresholds menores. De todo modo, existem algumas figuras de mérito que podem ser empregadas para otimizar esta escolha, como o Youden's Index, que mede a diferença entre as Taxas de Verdadeiro e Falso Positivo:

$$\textrm{Youden's Index} = TPR - FPR $$

Neste caso, o Decision Threshold escolhido deve ser aquele que maximiza a relação acima, por representar o valor de corte em que a quantidade de acertos do classificador é máxima com relação aos seus erros. 

Portanto, todas estas métricas (TPR, FPR e AUC) serão usadas em nossas análises. Adicionalmente, usaremos outras métricas de classificação conhecidas, tais como: 
Acurácia: porcentagem de observações classificadas corretamente 
Precisão: porcentagem de observações classificadas como positivas que são realmente positivas. 

Para o cálculo delas, consideramos o valor de Decision Threshold que maximiza o Índice de Youden. 

# Ferramentas

Para a organização e visualização dos dados do dataset, foram utilizadas as bibliotecas Pandas, Numpy e Matplotlib. Para a confecção do workflow do projeto, o grupo utilizou a ferramenta de desenho de workflows Draw.io. Para a execução do projeto em si, isto é, as classificações da imagens, irão ser utilizadas as bibliotecas PyTorch, para a parte de Deep Learning, e o SciKit-Learn para a parte de algoritmos tradicionais de machine learning voltados à classificação.
Todo o projeto tem sido desenvolvido, em linguagem Python, no formato de Notebooks do Google Colaboratory - com uso de GPUs/CPUs. Adicionalmente, todos os arquivos (raw, intermediários e finais) têm sido salvos na plataforma Google Drive - sendo, eventualmente, repassados para o Github. 

# Workflow

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/workflow_2.png" height="350">
</p>

# Experimentos e Resultados preliminares

Nesta seção, apresentamos os resultados preliminares desta primeira entrega. 

## Análise com Deep Learning:

### Baseline vs Experimento 1: 
A Figura 5 apresenta a ROC Curve comparando o experimento Baseline (treinamento/validação/teste com todos os tecidos) com o experimento 1 (treinamento/validação com todos os tecidos, exceto ‘Breast’ que foi usado apenas para os testes). No cenário Baseline, o modelo de Deep Learning apresentou um desempenho elevado (AUC=0.97), indicando que mesmo sem qualquer tipo de pré-processamento, foi possível identificar a existência de células neoplásicas na maior parte das imagens de teste. 
Já no experimento 1, a EfficientNet_B0 apresentou uma queda de performance em comparação com o cenário baseline (AUC=0.917). Mesmo assim, esta ainda é uma performance razoavelmente alta - o que é um indício de que um modelo de Deep Learning é capaz de generalizar e identificar padrões em imagens não vistas durante o treinamento. 

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/ROC_GeneralAnalysis.png" height="350">
</p>
Fig. 5. ROC Curve comparando o modelo de Deep Learning no cenário baseline (treino e teste com todos os tecidos) com o experimento 1 (treino com todos os tecidos menos ‘Breast’, que é usado para o teste). 

A Figura 6 mostra os gráficos de True Positive Rate e False Positive Rate em função do Decision Threshold. Em geral, para todo o intervalo de Decision Threshold, tanto o caso Baseline quanto no experimento 1, as curvas de False Positive Rate são praticamente iguais. A grande diferença entre os modelos é, portanto, no True Positive Rate - que é consideravelmente maior no cenário Baseline.

A Tabela 1 sintetiza algumas métricas de desempenho, para os dois estudos, considerando também o valor de Decision Threshold que maximiza o Índice de Youden. É possível ver que, em geral, os valores obtidos de acurácia e precisão também são elevados (>87%). 

<p align="middle">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/TPR_GeneralAnalysis.png" height="300">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/FPR_GeneralAnalysis.png" height="300">
</p>
Fig. 6. True Positive Rate e False Positive Rate em função do Decision Threshold para os dois estudos.  
Tab. 1. Síntese das principais métricas de performance para os estudos: Baseline e experimento 1. 

|Estudos|AUC|TPR*|FPR*|Precision*|Accuracy*|D. Threshold*|
|---|---|---|---|---|---|---|
|Baseline|0\.970|0\.92|0\.05|0\.95|0\.94|0\.43|
|Experimento 1|0\.917|0\.84|0\.09|0\.9|0\.87|0\.01|

*Métricas calculadas com base no valor ótimo (máximo) do Índice de Youden. 

### Análise por tecido com modelo Baseline
<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/ROC_TissueAnalysis.png" height="350">
</p>
Fig. 7. ROC Curve comparando a performance do modelo baseline para diferentes tecidos. Apenas aquelas com as três maiores (Stomach, Lung, Prostate) e três menores (Uterus, HeadNeck, Bile-duct) performances estão representadas. 

Tab. 2. Síntese das principais métricas de performance para o estudo Baseline considerando os diferentes tecidos. 

|N\. amostras|Types|AUC|TPR*|FPR*|Precision*|Accuracy*|D. Threshold*|
|---|---|---|---|---|---|---|---|
|29|Stomach|1\.0|1\.0|0\.0|1\.0|0\.97|0\.74|
|36|Lung|1\.0|1\.0|0\.0|1\.0|0\.97|0\.22|
|35|Prostate|1\.0|1\.0|0\.0|1\.0|0\.83|1\.0|
|58|Cervix|0\.997|0\.95|0\.0|1\.0|0\.95|0\.95|
|87|Adrenal\_gland|0\.988|0\.98|0\.0|1\.0|0\.98|0\.08|
|84|Esophagus|0\.984|0\.94|0\.06|0\.94|0\.93|0\.56|
|26|Kidney|0\.981|0\.88|0\.0|1\.0|0\.92|0\.98|
|29|Bladder|0\.98|1\.0|0\.12|0\.89|0\.9|0\.33|
|39|Testis|0\.976|0\.95|0\.0|1\.0|0\.95|0\.99|
|470|Breast|0\.974|0\.91|0\.04|0\.96|0\.93|0\.63|
|29|Ovarian|0\.966|0\.94|0\.0|1\.0|0\.93|0\.7|
|37|Skin|0\.962|0\.95|0\.12|0\.89|0\.89|0\.56|
|39|Pancreatic|0\.959|0\.92|0\.0|1\.0|0\.95|0\.57|
|45|Thyroid|0\.936|0\.9|0\.03|0\.97|0\.91|1\.0|
|288|Colon|0\.932|0\.86|0\.01|0\.99|0\.96|0\.93|
|44|Liver|0\.928|0\.83|0\.0|1\.0|0\.91|0\.86|
|37|Uterus|0\.923|0\.85|0\.0|1\.0|0\.86|0\.98|
|76|HeadNeck|0\.922|0\.83|0\.05|0\.94|0\.89|0\.72|
|84|Bile-duct|0\.918|0\.88|0\.15|0\.85|0\.87|0\.43|


#### Exemplo de imagens classificadas incorretamente pelo modelo

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/DL_WrongPredictions.png" height="550">
</p>

## Problemas encontrados até aqui:
Aparentemente, algumas imagens não são totalmente informativas - isto é, estão em baixíssima qualidade ou correspondem a imagens das lâminas sem informações dos tecidos. Por exemplo, as duas imagens abaixo deveriam ser do cólon: 

<p align="middle">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Problem1.png" height="300">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/Problem2.png" height="300">
</p>

1. Algumas imagens do dataset estão corrompidas e percebemos isto apenas na hora de treinar/testar os modelos. Excluímos elas manualmente dos diretórios para que não fossem usadas nas análises. Porém, por uma questão de reprodutibilidade, pretendemos incluir algumas salvaguardas nos códigos para automatizar a exclusão de imagens corrompidas. 

2. Ainda não foi possível realizar uma quantidade exaustiva de testes com os modelos de Deep Learning para encontrar uma arquitetura que seja, certamente, ótima. Estamos utilizando a GPU do Google Colab, que impõe limitações em seu uso. 


# Próximos passos

Com base nos resultados obtidos, os próximos passos imediatos seriam:

1. Realizar extração de atributos e testar modelos tradicionais de Machine Learning na classificação de imagens; (médio/longo prazo)

2. Aprimorar o modelo baseline testando outras arquiteturas (com ou sem Transfer Learning) ou métodos de data augmentation ; (curto prazo)

3. Fazer fine-tuning do modelo de Deep Learning para aumentar a performance de classificação do tecido ‘Breast’ (experimento 1); (médio prazo)

4. Em geral, o modelo de Deep Learning apresentou uma alta performance em classificar as imagens no nosso problema - mesmo considerando o caso em que excluímos um dos tipos de tecido. Por isso, estudaremos algumas possíveis extensões para o projeto (médio/longo prazo):

4.1 Contagem do número de células neoplásicas em cada imagem - tarefa de regressão;

4.2 Uso de técnicas de interpretação das redes neurais treinadas;

4.3 Analisar a necessidade de balancear o dataset para o número de cada tipo de tecido;

4.4 Analisar a possibilidade de classificação entre tumores benignos e malignos;

5. Aspectos técnicos a serem trabalhados:

5.1 Adicionar salvaguardas nos códigos para evitar que imagens corrompidas sejam usadas; (curto prazo)

5.2 Criar algum critério de exclusão para imagens com baixa qualidade; (curto prazo)

5.3 Adaptar os códigos para salvar mais resultados intermediários e garantir a reprodutibilidade e fácil entendimento pelos usuários; (curto prazo)

5.4 Implementar ferramentas para o arquivamento dos experimentos (por ex. NeptuneAI) (médio prazo)

5.5 Documentar as versões e pré-requisitos das bibliotecas e programas utilizados. (curto prazo)

Dado que teremos 1 mês até a entrega final, estamos considerando que:

Curto prazo: 1-2 semanas

Médio prazo: 2-3 semanas

Longo prazo: 3-4 semanas

## Referências 

[1]: G., Jevgenij et. al,  “PanNuke Dataset Extension, Insights and Baselines”, 2020. (URL)

[2]: Defining Cancer. National Cancer Institute

[3]: Bhuiyan MR, Abdullah J. Detection on Cell Cancer Using the Deep Transfer Learning and Histogram Based Image Focus Quality Assessment. Sensors (Basel). 2022 Sep 16;22(18):7007. doi: 10.3390/s22187007. PMID: 36146356; PMCID: PMC9504738. (URL)
