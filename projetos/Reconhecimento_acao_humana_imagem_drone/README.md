# `Reconhecimento de ação humana em imagens de veículos aéreos não tripulado (UAVs)`
# `Recognition of human action in Unmanned Aerial Vehicles (UAVs) images`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*, oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

|Nome  | RA | Curso|
|--|--|--|
| Débora Simões  | 263621  | Doutorado em Engenharia Civil|
| Lucas Ueda  | 156368  | Doutorado em Engenharia Elétrica|
| Wesna de Araújo  | 225843  | Graduação em Engenharia Elétrica|


## Descrição do Projeto

Os Veículos Aéreos Não Tripulados (VANTs), popularmente conhecidos como drones, têm sido amplamente adotados em diferentes aplicações, como mapeamento, logística, vigilância, agricultura, dentre outras. No entanto, o grande número de UAVs no espaço aéreo mundial levanta preocupações relacionadas ao gerenciamento do espaço aéreo e à segurança das pessoas próximas às operações. Em todo o mundo existem regulamentações sobre o acesso e o controle do espaço aéreo, buscando minimizar os riscos que as operações com UAVs envolvem. Dentre tais regras, há uma preocupação com as pessoas, especialmente àquelas não envolvidas com a operação UAV. No Brasil (BRASIL, 2020), por exemplo, deve ser mantida uma distância mínima de 30 m entre as pessoas e a projeção do UAV no terreno.

Nesse caso, a identificação de pessoas em tempo real em um voo de UAV torna-se crucial para manter a segurança de uma operação, principalmente nas operações em que a roteirização dos UAVs é online: a aeronave identifica mudanças no ambiente e é capaz de reagir com elas, atualizando sua rota em tempo real (ZHAO; ZHENG; LIU, 2018). Após detectar uma pessoa no terreno, o drone pode ser capaz de replanejar sua rota em tempo real e desviar-se para não sobrevoar pessoas, o que garante a segurança nas operações com UAV. Reconhecer se a pessoa está caminhando, por exemplo, também é importante para que a rota do UAV seja evitada na direção para onde a pessoa está indo. Assim, reconhecer o comportamento da pessoa também contribuiu para o planejamento de rotas seguras para o UAV.

Outra aplicação em que é importante detectar e reconhecer o comportamento humano é a vigilância de cidades inteligentes, como mostra o trabalho de Del Rosario et al. (2021), em que é necessário identificar e o rastrear pessoas.

Nesse contexto, o objetivo do presente projeto é detectar pessoas e reconhecer o seu comportamento em imagens obtidas com drones, adotando a arquitetura YOLOv7 (WANG; BOCHKOVSKIY; LIAO, 2022). Como há diferentes comportamentos para as pessoas nas imagens aéreas e, dependendo da altura de voo, pode ser difícil detectar de que o objeto nessa imagem é um humano, são realizados pré-processamentos nas imagens de drone a fim de melhorar a precisão obtida ao detectar e reconhecer a ação humana. 

# Metodologia
> Proposta de metodologia incluindo especificação de quais técnicas pretende-se explorar. Espera-se que nesta entrega você já seja capaz de descrever de maneira mais específica (do que na Entrega 1) quais as técnicas a serem empregadas em cada etapa do projeto.

Para desenvolvimento deste projeto, é adotada a base de dados “NTUT 4K Drone Photo Dataset for Human Detection”, descrita com mais detalhes na seção a seguir (“Bases de Dados e Evolução”).

> Pré-processamento. Verificar o redimensionamento das imagens. 
> Coloquei como "normalização" das imagens um pré-processamento, mas acho que a rede já faz isso. Verificar.

As imagens disponíveis têm dimensão 3840 x 2160 pixels. Assim, todas as imagens foram redimensionadas para XXXX x YYYY pixels. 
Para se obter as melhores métricas de classificação, testaram-se os seguintes pré-processamentos nas imagens:

•	Teste 1: as imagens coloridas foram convertidas para tons de cinza (imagens pancromáticas), objetivando minimizar o custo computacional;

•	Testes 2 e 3: aplicou-se uma filtragem no domínio espacial, objetivando realçar detalhes na imagem (bordas e linhas que possam contribuir para a detecção de pessoas e de suas poses) – filtros de aguçamento. No Teste 2, adotou-se o filtro de Sobel: aplicou-se o gradiente obtido a partir das duas máscaras de Sobel (horizontal e vertical). No Teste 3, aplicou-se o filtro Laplaciano (GONZALES; WOODS, 2010);

•	Teste 4: normalização das imagens.

> Definição das classes:

Para a detecção de pessoas, observou-se que, no conjunto de dados de treinamento, há 2156 imagens de drone. Como em uma mesma imagem pode haver mais de uma pessoa, considerando todos os registros (labels), tem-se 31805 amostras, sendo que cada amostra corresponde a uma pessoa detectada na imagem. Em cada um desses 31805 dados, há o registro do nome da imagem em que a pessoa está sendo detectada, das coordenadas digitais que definem o bounding box e do rótulo correspondente à pose em que a pessoa se encontra. Entretanto, observou-se muitas classes correspondentes às poses humanas eram indefinidas (registradas como “id” ou “block”). Desse modo, inicialmente, os dados de treinamento foram analisados e definiram-se quatro classes a serem adotadas no presente projeto, dentre as registradas no Dataset. Essas classes são as que contém o maior número de amostras:

•	Walk: 6155 amostras;

•	Stand: 2551 amostras;

•	Sit: 424 amostras;

•	Riding: 2487 amostras.

> Data augmentation:

Objetivando balancear o número de amostras por classe, adotou-se Data augmentation. Considerando possíveis movimentos a serem realizados por um drone no momento da aquisição das imagens, foram testados três processos de aumentação dos dados objetivando melhorar as métricas de classificação – disponíveis em PyTorch (2023): 

•	Espelhamento Horizontal (RandomHorizontalFlip);

•	Espelhamento Vertical (RandomVerticalFlip);

•	Rotação de 15° (RandomRotation).

> Arquitetura adotada: YoloV7

Para detecção das pessoas nas imagens de drone e classificação de suas poses, adotou-se uma a arquitetura YOLOv7, que, segundo Wang, Bochkovskiy e Liao (2022), supera todos os detectores de objetos conhecidos em velocidade e precisão (tem menos parâmetros, menor custo computacional e alcança maior precisão). Para o presente projeto, adaptou-se o código da YOLOv7, disponível em https:// github.com/WongKinYiu/yolov7, alterando-se as classes na etapa de estimativa de pose (YOLOv7 inclui um modelo de estimativa de pose humana). 

> Verificar se há mais alterações na rede.

> Métricas de avaliação: 

## Bases de Dados e Evolução
<!--
> Elencar bases de dados utilizadas no projeto.
> Para cada base, coloque uma mini-tabela no modelo a seguir e depois detalhamento sobre como ela foi analisada/usada, conforme exemplo a seguir.-->
A tabela abaixo mostra resumidamente algumas informações sobre o banco de dados utilizado no desenvolvimento do projeto.

Base de Dados | Endereço na Web | Resumo descritivo
----- | :-----: | -----
NTUT 4K Drone Photo Dataset for Human Detection | [Link](https://www.kaggle.com/datasets/kuantinglai/ntut-4k-drone-photo-dataset-for-human-detection) | <!--Breve resumo (duas ou três linhas) sobre a base.--> Esse banco de dados é formado por imagens de alta resolução extraídas de vídeos gravados por drones em Taiwan. Para cada imagem, estão disponíveis as coordenadas digitais que definem o *bounding box* em torno de uma pessoa detectada, bem como o rótulo que identifica a pose do indivíduo detectado.
---
A base de dados NTUT 4K Drone Photo Dataset for Human Detection, como comentado anteriormente, é formada por 4095 imagens de drone coletadas em Taiwan com dimensões 3840 x 2160 pixels, sendo as imagens organizadas em pastas de acordo com o cenário, altura de voo e orientação da câmera. Dessa quantidade, 2156 imagens (53% do conjunto de dados) foram separadas para treino emquanto que 1939 (47% do conjunto de dados) foram destinados para teste. Como em cada imagem pode haver mais de uma pessoa realizando ações distintas o conjunto de treino passa a ter ao todo 31804 amostras, ao passo que o conjunto de teste tem 20920 amostras. Além disso, todas as imagens estão em formato jpg.

Como forma de rotulação, cada pasta vem acompanhada de um arquivo csv que informa para cada amostra as coordenadas do centro do *bounding box* em torno de uma pessoa detectada, isto é, (Xmin, Ymin, Xmax e Ymax) e ainda tráz a informação sobre a pose da pessoa detectada (walk, push, stand, etc).

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

Note que a classe "outros" é referente a rotulações que não especificam diretamente a pose da pessoa detectada, ao invés disso nomeia com o termo id_ seguido de um número ou usa a palavra blocked. Assim, considerando o tamanho do conjunto e a fim de evitar as classes não nomeadas optou-se por utilizar as 4 classes mais numerosas de modo a obter um conjunto de dados mais balanceado. Dessa forma, foram selecionadas apenas as classes walk, stand, sit e riding. O histograma abaixo ilustra a distribuição de dados, tanto do conjunto de treino (11617 amostras) quanto do conjunto de teste (7163 amostras) com a nova seleção.

<p align="left">
    <img src="../Reconhecimento_acao_humana_imagem_drone/assets/Dados_selecionados_treino_teste.png" height="350">
</p>

<!--confirmar se vamos ter que rerotular os labels --> 

<!--
> Faça uma descrição sobre o que concluiu sobre esta base. Sugere-se que respondam perguntas ou forneçam informações indicadas a seguir:
> * Qual o formato dessa base, tamanho, tipo de anotação?
> * Quais as transformações e tratamentos feitos? Limpeza, reanotação, etc.
> * Inclua um sumário com estatísticas descritivas da(s) base(s) de estudo.
> * Utilize tabelas e/ou gráficos que descrevam os aspectos principais da base que são relevantes para o projeto.-->

# Ferramentas
> Ferramentas e/ou bibliotecas já utilizadas e/ou ainda a serem utilizadas (com base na visão atual do grupo sobre o projeto).

# Workflow
> Use uma ferramenta que permita desenhar o workflow e salvá-lo como uma imagem (Draw.io, por exemplo). Insira a imagem nessa seção.
> Você pode optar por usar um gerenciador de workflow (Sacred, Pachyderm, etc) e nesse caso use o gerenciador para gerar uma figura para você.
> Lembre-se que o objetivo de desenhar o workflow é ajudar a quem quiser reproduzir seus experimentos. 
> <!-- [](image.jpg)-->

# Experimentos e Resultados preliminares
> Descreva de forma sucinta e organizada os experimentos realizados
> Para cada experimento, apresente os principais resultados obtidos
> Aponte os problemas encontrados nas soluções testadas até aqui

# Próximos passos
> Liste as próximas etapas planejadas para conclusão do projeto, com uma estimativa de tempo para cada etapa

## Referências (ATUALIZAR SE NECESSÁRIO)
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.

BRASIL. Departamento de Controle do Espaço Aéreo. Aeronaves Não Tripuladas e o Acesso ao Espaço Aéreo Brasileiro. ICA 100-40.  Ministério da Defesa, 2020. Disponível em: <https://publicacoes.decea.mil.br/publicacao/ica-100-40>. Acesso em 13 mai. 2023.

DEL ROSARIO, J. R. B. et al. Development of a Multi-Object Detection and Human Tracking System from Cooperative Dual Cameras in an Unmanned Aerial Vehicle. In: 2021 IEEE 13th International Conference on Humanoid, Nanotechnology, Information Technology, Communication and Control, Environment, and Management (HNICEM). IEEE, 2021. pág. 1-4. Disponível em: <https://doi.org/10.1109/HNICEM54116.2021.9732035>.

GONZALEZ, R. ; WOODS, R. E. Processamento Digital de Imagens. 3 ed. Pearson, 2009.

PYTORCH. Transforming and augmenting images. Disponível em: <https://pytorch.org/vision/0.12/transforms.html>. Acesso em: 15 maio 2023.

WANG, C.; BOCHKOVSKIY, A.; LIAO, H. M. YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors. arXiv preprint arXiv:2207.02696, 2022. Disponível em: 
<https://doi.org/10.48550/arXiv.2207.02696>.

ZHAO, Y.; ZHENG, Z.; LIU, Y. Survey on computational-intelligence-based UAV path planning. Knowledge-Based Systems, v. 158, p. 54–64, 2018. Elsevier. Disponível em: <https://doi.org/10.1016/j.knosys.2018.05.033>.


