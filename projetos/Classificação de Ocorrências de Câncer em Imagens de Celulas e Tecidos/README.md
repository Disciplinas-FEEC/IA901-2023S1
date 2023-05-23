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
Cancer Instance Segmentation and Classification 3 | https://www.kaggle.com/datasets/andrewmvd/cancer-instance-segmentation-and-classification-3 | Segunda parte do dataset, contendo 2722 imagens de tecidos e as respectivas máscaras de segmentação. Os rótulos de cada tipo de tecido também estão disponíveis.|

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


# Ferramentas
> Ferramentas e/ou bibliotecas já utilizadas e/ou ainda a serem utilizadas (com base na visão atual do grupo sobre o projeto).

# Workflow
> Use uma ferramenta que permita desenhar o workflow e salvá-lo como uma imagem (Draw.io, por exemplo). Insira a imagem nessa seção.
> Você pode optar por usar um gerenciador de workflow (Sacred, Pachyderm, etc) e nesse caso use o gerenciador para gerar uma figura para você.
> Lembre-se que o objetivo de desenhar o workflow é ajudar a quem quiser reproduzir seus experimentos.

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/workflow.png" height="350">
</p>

# Experimentos e Resultados preliminares
> Descreva de forma sucinta e organizada os experimentos realizados
> Para cada experimento, apresente os principais resultados obtidos
> Aponte os problemas encontrados nas soluções testadas até aqui

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/ROC_GeneralAnalysis.png" height="350">
</p>

<p align="middle">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/TPR_GeneralAnalysis.png" height="300">
  <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/FPR_GeneralAnalysis.png" height="300">
</p>

<p align="center">
    <img src="../Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/ROC_TissueAnalysis.png" height="350">
</p>




# Próximos passos
> Liste as próximas etapas planejadas para conclusão do projeto, com uma estimativa de tempo para cada etapa

## Referências (ATUALIZAR SE NECESSÁRIO)
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.

[1]: G., Jevgenij et. al,  “PanNuke Dataset Extension, Insights and Baselines”, 2020. (URL)

[2]: Defining Cancer. National Cancer Institute

[3]: Bhuiyan MR, Abdullah J. Detection on Cell Cancer Using the Deep Transfer Learning and Histogram Based Image Focus Quality Assessment. Sensors (Basel). 2022 Sep 16;22(18):7007. doi: 10.3390/s22187007. PMID: 36146356; PMCID: PMC9504738. (URL)
