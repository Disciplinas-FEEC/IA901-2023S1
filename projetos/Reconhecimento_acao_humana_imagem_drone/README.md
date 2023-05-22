# `Reconhecimento de ação humana em imagens de veículos aéreos não tripulado (UAVs)`
# `Recognition of human action in Unmanned Aerial Vehicles (UAVs) images`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*, oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

|Nome  | RA | Curso|
|--|--|--|
| Débora Simões  | 263621  | Doutorado em Engenharia Civil|
| Lucas Ueda  | 156368  | Doutorado em Engenharia Elétrica|
| Wesna de Araujo  | 225843  | Graduação em Engenharia Elétrica|


## Descrição do Projeto

Os Veículos Aéreos Não Tripulados (VANTs), popularmente conhecidos como drones, têm sido amplamente adotados em diferentes aplicações, como mapeamento, logística, vigilância, agricultura, dentre outras. No entanto, o grande número de UAVs no espaço aéreo mundial levanta preocupações relacionadas ao gerenciamento do espaço aéreo e à segurança das pessoas próximas às operações. Em todo o mundo, existem regulamentações sobre o acesso e o controle do espaço aéreo, buscando minimizar os riscos que as operações com UAVs envolvem. Dentre tais regras, há uma preocupação com as pessoas, especialmente àquelas não envolvidas com a operação UAV. No Brasil (BRASIL, 2020), por exemplo, deve ser mantida uma distância mínima de 30 m entre as pessoas e a projeção do UAV no terreno.

Nesse caso, a identificação de pessoas em tempo real em um voo de UAV torna-se crucial para manter a segurança de uma operação, principalmente nas operações em que a roteirização dos UAVs é online: a aeronave identifica mudanças no ambiente e é capaz de reagir a elas, atualizando sua rota em tempo real (ZHAO; ZHENG; LIU, 2018). Após detectar uma pessoa no terreno, o drone deve ser capaz de replanejar sua rota em tempo real e desviar-se para não sobrevoar pessoas, o que garante a segurança nas operações com UAV. Reconhecer se a pessoa está caminhando, por exemplo, também é importante para que a rota do UAV seja evitada na direção para onde a pessoa está indo. Assim, reconhecer o comportamento da pessoa também contribuiu para o planejamento de rotas seguras para o UAV.

Outra aplicação em que é importante detectar e reconhecer o comportamento humano é a vigilância de cidades inteligentes, como mostra o trabalho de Del Rosario et al. (2021), em que é necessário identificar e rastrear pessoas.

Nesse contexto, o objetivo do presente projeto é detectar pessoas e reconhecer o seu comportamento em imagens obtidas com drones, adotando a arquitetura YOLOv7 (WANG; BOCHKOVSKIY; LIAO, 2022). Como há diferentes comportamentos para as pessoas nas imagens aéreas e, dependendo da altura de voo, pode ser difícil detectar se o objeto nessa imagem é um humano, são realizados pré-processamentos nas imagens de drone a fim de melhorar a precisão obtida ao detectar e reconhecer a ação humana. 

# Metodologia

Para desenvolvimento deste projeto, é adotada a base de dados “NTUT 4K Drone Photo Dataset for Human Detection”, descrita com mais detalhes na seção a seguir (“Bases de Dados e Evolução”).

Para a detecção de pessoas, observou-se que, no conjunto de dados de treinamento, há 2156 imagens de drone. Já que em uma mesma imagem pode haver mais de uma pessoa, considerando todos os registros (labels) correspondentes às poses humanas, tem-se 31805 amostras no conjunto de treinamento, sendo que cada amostra corresponde a uma pessoa detectada na imagem. Em cada um desses 31805 dados, são registrados: o nome da imagem em que a pessoa está sendo detectada, as coordenadas digitais que definem o bounding box, e o rótulo correspondente à pose em que a pessoa se encontra. 

Como algumas classes correspondentes às poses humanas eram indefinidas (registradas como “id_” ou “block_”), os dados foram analisados e, considerando as classes com maior número de amostras, definiram-se quatro classes a serem adotadas no presente projeto:

- Walk: 6155 amostras;

- Stand: 2551 amostras;

- Sit: 424 amostras;

- Riding: 2487 amostras.

Filtrados os dados com base nas quatro classes estabelecidas, dividiu-se os dados de treino em Treino (80%) e Validação (20%). Os dados de teste, já disponíveis no dataset “NTUT 4K Drone Photo Dataset for Human Detection” e com 20920 amostras, também foi filtrado com base nas quatro classes. 

Dispondo, portanto, dos conjuntos de treino (1677 imagens), teste (1266 imagens) e validação (1006 imagens), definiram-se os arquivos (.txt) correspondentes aos labels das quatro classes, considerando as imagens que foram mantidas após a filtragem. Nos arquivos "label_train.txt", "label_val.txt" e "label_test.txt" são registrados: nome da imagem (image), coordenadas em pixels do bounding box (xmin, ymin, xmax, ymax) e o rótulo da classe (label).

A partir desses dados, realizou-se o treinamento do modelo (arquitetura Yolov7). Tanto para a detecção das pessoas nas imagens de drone quanto  para a classificação de suas poses, adotou-se uma a arquitetura YOLOv7, que, segundo Wang, Bochkovskiy e Liao (2022), supera todos os detectores de objetos conhecidos em velocidade e precisão (tem menos parâmetros, menor custo computacional e alcança maior precisão). Para o presente projeto, adaptou-se o código da YOLOv7, disponível em <https://github.com/WongKinYiu/yolov7>.

Para tanto, inicialmente, criou-se um arquivo (.txt) para cada uma das imagens, com as informações de "ids" das classes presentes naquela imagem ('walk': 0, 'riding': 1, 'stand': 2, 'sit': 3), as coordenadas do centro do "bouding box" normalizadas (x_center e y_center) e a largura (w) e altura(h) do "bounding box" normalizado. Para o treinamento, redimensinou-se as imagens para 640x640 pixels. Os hiperparâmetros definidos foram: tamanho dos mini batches (BATCH_SIZE = 16 imagens) e número de épocas (EPOCHS = 20).

Além do treinamento adotando os dados filtrados (imagens RGB), realizaram-se treinamentos com as imagens resultantes dos seguintes pré-processamentos, a fim de melhorar as métricas de avaliação do modelo:

- Pré-processamento 1: conversão das imagens RGB para imagens em níveis de cinza;

- Pré-processamento 2: filtragem no domínio espacial, adotando o filtro de Sobel (aplicou-se o gradiente obtido a partir das duas máscaras de Sobel - horizontal e vertical) (GONZALES; WOODS, 2009);

- Pré-processamento 3: filtragem no domínio espacial, adotando o filtro de Prewitt (aplicou-se o gradiente obtido a partir das duas máscaras de Prewitt - horizontal e vertical) (GONZALES; WOODS, 2009).

Cabe ressaltar que um quarto pré-processamento também foi realizado  - filtragem no domínio espacial, adotando o filtro de Laplace (GONZALES; WOODS, 2009). Entretanto, em função das imagens resultantes dessa filtragem, optou-se por não utilizá-las para treinamento do modelo.

Destaca-se, também, que para cada conjunto de imagens obtido após os pré-processamentos dos conjuntos de imagens de treino, teste e validação, copiou-se o arquivo (.txt) correspondente às labels, bem como os arquivos gerados para cada uma das imagens com as informações de "ids" das classes presentes naquela imagem ('walk': 0, 'riding': 1, 'stand': 2, 'sit': 3), coordenadas do centro do "bouding box" normalizadas (x_center e y_center) e a largura (w) e altura(h) do "bounding box" normalizado.

Assim, no total, quatro treinamentos foram realizados até o momento para o presente projeto:

- Treinamento 1: adotando as imagens RBG;

- Treinamento 2: adotando as imagens em nível de cinza;

- Treinamento 3: adotando as imagens filtradas pelo Filtro de Sobel;

- Treinamento 4: adotando as imagens filtradas pelo Filtro de Prewitt.

Para avaliar o modelo, foram adotadas as seguintes métricas:

- Matriz de Confusão;

- Precisão: mede a proporção de positivos previstos que estão realmente corretos - Precisão = TP/(TP + FP). O valor varia de 0 a 1 (KUKIL, 2022b);

- Recall: mede a proporção de positivos reais que foram previstos corretamente - Recall = TP / (TP + FN). Varia de 0 a 1 (KUKIL, 2022b); 

- Mean Average Precision (mAP): é a média das "Precisão média (AP)" calculadas para todas as classes - mAP = 1/n * soma(APs), onde n é o número de classes. A Precisão média (AP) é igual a soma dos valores de precisão interpolados em 11 valores de chamada, dividido por 11 (AP = 1/11 * Soma de 11 valores de precisão interpolados). AP é definida para cada uma das classes (KUKIL, 2022b).

## Bases de Dados e Evolução
<!--
> Elencar bases de dados utilizadas no projeto.
> Para cada base, coloque uma mini-tabela no modelo a seguir e depois detalhamento sobre como ela foi analisada/usada, conforme exemplo a seguir.-->
A tabela abaixo mostra resumidamente algumas informações sobre o banco de dados utilizado no desenvolvimento do projeto.

Base de Dados | Endereço na Web | Resumo descritivo
----- | :-----: | -----
NTUT 4K Drone Photo Dataset for Human Detection | [Link](https://www.kaggle.com/datasets/kuantinglai/ntut-4k-drone-photo-dataset-for-human-detection) | <!--Breve resumo (duas ou três linhas) sobre a base.--> Esse banco de dados é formado por imagens de alta resolução extraídas de vídeos gravados por drones em Taiwan. Para cada imagem, estão disponíveis as coordenadas digitais que definem o *bounding box* em torno de uma pessoa detectada, bem como o rótulo que identifica a pose do indivíduo detectado.
---
A base de dados NTUT 4K Drone Photo Dataset for Human Detection, como comentado anteriormente, é formada por 4095 imagens de drone coletadas em Taiwan com dimensões 3840 x 2160 pixels, sendo as imagens organizadas em pastas de acordo com o cenário, altura de voo e orientação da câmera. Dessa quantidade, 2156 imagens (53% do conjunto de dados) foram separadas para treino emquanto que 1939 (47% do conjunto de dados) foram destinados para teste. Como em cada imagem pode haver mais de uma pessoa realizando ações distintas o conjunto de treino passa a ter ao todo 31805 amostras, ao passo que o conjunto de teste tem 20920 amostras. Além disso, todas as imagens estão em formato jpg.

Como forma de rotulação, cada pasta vem acompanhada de um arquivo csv que informa para cada amostra as coordenadas do centro do *bounding box* em torno de uma pessoa detectada, isto é, (Xmin, Ymin, Xmax e Ymax) e ainda traz a informação sobre a pose da pessoa detectada (walk, push, stand, etc).

Através de uma análise considerando todas as classes existentes nos conjuntos de treino e teste, chegou-se aos seguintes valores:

Classes | Dados de Treino | Dados de teste
----- | :-----: | :-----:
walk  |     6155    |   4858 
stand |     2551    |   1752 
push  |    143      |   34
watchphone  |     167     |   0
baseball  |     118     |   0
sit  |    424      |    481 
riding  |    2487      |    72 
outros  |    19760      |   13723 

Note que a classe "outros" é referente a rotulações que não especificam diretamente a pose da pessoa detectada, ao invés disso nomeia com o termo id_ seguido de um número ou usa a palavra block. Assim, considerando o tamanho do conjunto e a fim de evitar as classes não nomeadas, optou-se por utilizar as 4 classes mais numerosas de modo a obter um conjunto de dados mais balanceado. Dessa forma, foram selecionadas apenas as classes walk, stand, sit e riding. 

Além disso, foi necessário separar os dados de treino, teste e validação. Em relação ao conjunto de teste após a filtragem das classes obteve-se um total de 6271 amostras (1266 imagens). Como o banco de dados bruto possui apenas o conjunto de treino, sem considerar validação, foi definido que 20% dos dados de treino já selecionados com as 4 classes seriam destinados ao conjunto de validação enquanto que os 80% restante formariam o conjunto de treino. Assim, 8479 amostras foram destinadas para treino (1677 imagens) e 2123 amostras ficaram para a validação (1006 imagens).

O histograma abaixo ilustra a distribuição de dados do conjunto de treino, teste e validação que serão utilizados durante o projeto.

<p align="left">
    <img src="../Reconhecimento_acao_humana_imagem_drone/assets/Dados_selecionados_treino_teste_validacao.png" height="350">
</p>

Ademais é importante destacar que as classes walk, stand, sit e riding foram remapeadas com valores númericos para se adequar ao algoritimo da rede YOLOv7. A tabela abaixo mostra a nova identificação.

Classe Original | Classe YOLOv7
:-----: | :-----: | 
walk  |     0   
riding |    1
stand |     2
sit   |     3

Por fim, os valores do *bounding box* foram normalizados para atender também as especificações da rede YOLOv7.

<!--
> Faça uma descrição sobre o que concluiu sobre esta base. Sugere-se que respondam perguntas ou forneçam informações indicadas a seguir:
> * Qual o formato dessa base, tamanho, tipo de anotação?
> * Quais as transformações e tratamentos feitos? Limpeza, reanotação, etc.
> * Inclua um sumário com estatísticas descritivas da(s) base(s) de estudo.
> * Utilize tabelas e/ou gráficos que descrevam os aspectos principais da base que são relevantes para o projeto.-->

# Ferramentas

Ferramentas adotadas no desenvolvimento do projeto:

- Google Colab, ou "Colaboratory": permitiu escrever e executar Python no navegador, além de contar com acesso a GPUs sem custo financeiro, que foram adotadas para o treinamento do modelo. Acesso ao Google Colab: <https://colab.research.google.com/#scrollTo=5fCEDCU_qrC0> (versão do Google Colab utilizada: atualizada em 05/05/2023);
- Google Drive: tanto os dados brutos (dataset "NTUT 4K Drone Photo Dataset for Human Detection") quanto os dados filtrados e aqueles resultados dos pré-processados foram armazenados no Google Drive. Os notebooks desenvolvidos no Google Colab também encontram-se salvos no Google Drive (acesso ao Google Drive: <https://drive.google.com/drive/my-drive>);
- Github: um repositório no Github (<https://github.com/>) foi criado e contém todos os arquivos do projeto, histórico de revisão e discussões dos colaboradores (Versão do Github adotada: atualizada em 08/2022).

Quanto às bibliotecas adotadas no projeto, todas se encontram definidas no arquivo "requirements.txt" (disponível em: 
<https://drive.google.com/file/d/11c1_tUSCeSvkG8aUJiVq-PQIpSXtAFUh/view?usp=sharing>).

# Workflow
<!-- > Use uma ferramenta que permita desenhar o workflow e salvá-lo como uma imagem (Draw.io, por exemplo). Insira a imagem nessa seção.
> Você pode optar por usar um gerenciador de workflow (Sacred, Pachyderm, etc) e nesse caso use o gerenciador para gerar uma figura para você.
> Lembre-se que o objetivo de desenhar o workflow é ajudar a quem quiser reproduzir seus experimentos. 
>  -->
![](IA901_workflow.png "workflow")

O workflow dos nossos procedimentos é apresentado na figura acima. Inicialmente os dados são baixados da plataforma Kaggle e colocados em uma pasta do GoogleDrive compartilhada entre os membros do projeto. A partir disso, um notebook (Dados.ipynb) é rodado para uma seleção e filtragem prévia dos dados, retirando-se imagens com rótulos diferentes de ['walk','stand','sit','riding'], separando o dataset nos conjuntos de treino, validação e teste. Isto tudo engloba o bloco "Data Wrangling I". Em seguida, opcionalmente, um pre processamento é rodado nas imagens (transformações de cor, aplicação de filtros, etc). Está etapa é chamada de "Data Pre-Processing", e é opcional pois é possível rodar com os dados crus. Por fim, a etapa de "Data Wrangling II" é rodada ("Creating labels from folders.ipynb") para formatar os dados de acordo com a pipeline da Yolov7, isto é, formatação das labels por imagem e organização das pastas. Por fim, podemos rodar o "training_template.ipynb" para treinar o modelo e "inference.ipynb" para a avaliação dos resultados.

# Experimentos e Resultados preliminares
<!--
> Descreva de forma sucinta e organizada os experimentos realizados
> Para cada experimento, apresente os principais resultados obtidos
> Aponte os problemas encontrados nas soluções testadas até aqui-->

Na primeira parte do projeto buscou-se um melhor entendimento sobre o conjunto de dados utilizado bem como da rede YOLOv7 que será usada tanto no reconhecimento de pessoas em imagens de drone quanto na classificação de suas ações. Assim, inicialmente foi feita uma seleção de imagens para garantir que todas estivessem devidamente rotuladas (com labels conhecidas) e que de fato estivessem presentes tanto na pasta de imagens original quanto no csv original (algumas imagens apareciam no csv mas não estavam presentes nas pastas de imagem). Dessa forma, depois de dividir as imagens em três grupos (treino, teste e validação) foi feita uma etapa de processamento afim de futuramente avaliar o desempenho da rede. Com isso, foram aplicadas 4 técnicas de processamento:

- Escala em Cinza;
- Filtro de Sobel;
- Filtro Laplaciano;
- Filtro de Prewitt.

Todas as técnicas aplicadas foram salvas em pastas intermediárias.

Com o objetivo de fazer uma comparação entre as diferentes técnicas de processamento e os dados brutos (apenas com a seleção inicial) fez-se um primeiro treinamento com a rede YOLOv7 com os dados sem processamento utilizando a plataforma Google Collaboratory. Foram definidas como ponto de partida 10 épocas considerando a demora do treinamento. Em seguida foram realizados treinamentos utilizando os dados pré processados em escala de cinza, com filtro de Sobel e por fim com o filtro de Prewitt. A tabela abaixo mostra os resultados preliminares de cada experimento.


Processamento dos Dados | Precisão | Recall | mAP
:-----: | :-----: | :-----: | :-----: |
Dados brutos filtrados  |    0.32    |   0.211  | 0.0625
Escala de Cinza |  0.526   |  0.0168 | 0.00558  |
Filtro Sobel |     0.555    |  0.131  |  0.0341 |
Filtro de Prewitt   |  0.277   | 0.073  | 0.0117


Além disso, durante o processamento das imagens com o filtro Laplaciano perecebeu-se que este possívelmente não traria bons resultados pois não realçava de maneira adequada as imagens (os datalhes/contornos das imagens foram cobertos por uma camada cinza densa). Por isso, pensou-se em utilizar um outro filtro de aguçamento: o filtro de Prewitt.

De maneira geral, os principais desafios enfrentados até o momento estão relacionados as limitações do uso da plataforma Google Collaboratory, ao tamanho das imagens o que implica na demora do treinamento por época, no rearranjo do conjunto de dados escolhido para se adequar a rede YOLOv7 e a escolha de um pré processamento que melhore o desempenho da rede.


# Próximos passos

Para as próximas etapas, pretende-se:

- Treinar a rede com um maior número de épocas (a princípio, pretende-se adotar 30 épocas de treinamento), adotando tanto os dados brutos (imagens RGB) quanto as imagens resultantes dos pré-processamentos realizados, e realizar comparações;
- Implementar a métrica Intersection Over Union (IoU) para validar a qualidade do reconhecimento de pessoas. Segundo Kukil (2022a), IoU avalia o grau de sobreposição entre a região de "Ground Truth" e "Prediction". É dada pela razão entre a área de sobreposição e a área combinada de previsão e dados de campo, e seus valores podem variar de 0 (nenhuma sobreposição) a 1 (sobreposição perfeita). Esse métrica é adotada, especificamente, para avaliar a detecção de pessoas, sendo, portanto, uma métrica auxiliar para avaliar a exatidão do modelo.
- Caso o desempenho não seja satisfatório, aplicar *Data augmentation* em algumas classes (com menos dados) para balanceá-las e auxiliar na generalização da rede. Para tanto, considerando possíveis movimentos a serem realizados por um drone no momento da aquisição das imagens, serão testados três processos de aumentação dos dados, disponíveis em PyTorch (2023): Espelhamento Horizontal (RandomHorizontalFlip), Espelhamento Vertical (RandomVerticalFlip) e Rotação de 15° (RandomRotation);
- Aplicar o melhor modelo obtido no treinamento para inferência no conjunto de teste e discutir os resultados finais obtidos.

O cronograma a seguir apresenta o tempo estimado para cada etapa futura:

<p align="left">
    <img src="../Reconhecimento_acao_humana_imagem_drone/assets/Cronograma_etapas_futuras.png" height="200">
</p>

## Referências

BRASIL. Departamento de Controle do Espaço Aéreo. Aeronaves Não Tripuladas e o Acesso ao Espaço Aéreo Brasileiro. ICA 100-40.  Ministério da Defesa, 2020. Disponível em: <https://publicacoes.decea.mil.br/publicacao/ica-100-40>. Acesso em 13 mai. 2023.

DEL ROSARIO, J. R. B. et al. Development of a Multi-Object Detection and Human Tracking System from Cooperative Dual Cameras in an Unmanned Aerial Vehicle. In: 2021 IEEE 13th International Conference on Humanoid, Nanotechnology, Information Technology, Communication and Control, Environment, and Management (HNICEM). IEEE, 2021. pág. 1-4. Disponível em: <https://doi.org/10.1109/HNICEM54116.2021.9732035>.

GONZALEZ, R. ; WOODS, R. E. Processamento Digital de Imagens. 3 ed. Pearson, 2009.

KUKIL. Intersection over Union (IoU) in Object Detection & Segmentation. 2022a. Disponível em: https://learnopencv.com/intersection-over-union-iou-in-object-detection-and-segmentation/. Acesso em: 16 maio 2023.

KUKIL. Mean Average Precision (mAP) in Object Detection. 2022b. Disponível em: https://learnopencv.com/mean-average-precision-map-object-detection-model-evaluation-metric/. Acesso em: 16 maio 2023.

PYTORCH. Transforming and augmenting images. Disponível em: <https://pytorch.org/vision/0.12/transforms.html>. Acesso em: 15 maio 2023.

WANG, C.; BOCHKOVSKIY, A.; LIAO, H. M. YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors. arXiv preprint arXiv:2207.02696, 2022. Disponível em: 
<https://doi.org/10.48550/arXiv.2207.02696>.

ZHAO, Y.; ZHENG, Z.; LIU, Y. Survey on computational-intelligence-based UAV path planning. Knowledge-Based Systems, v. 158, p. 54–64, 2018. Elsevier. Disponível em: <https://doi.org/10.1016/j.knosys.2018.05.033>.


