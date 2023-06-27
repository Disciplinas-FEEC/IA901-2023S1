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

A robótica tem se demonstrado uma tecnologia muito presente e útil com o passar dos anos, motivando estudos e projetos ao redor do mundo. Dentre suas aplicações, os ambientes domésticos não estão excluídos desta área de pesquisa, trazendo assim propostas de modelos robóticos cada vez mais sofisticados e modernos para o cotidiano das casas contemporâneas da atualidade. A partir da inclusão de robôs de serviço no ambiente familiar, tendo como exemplo os dispositivos de limpeza inteligentes (robôs aspiradores *smart*), outros aparelhos, porém com o propósito de exercer uma função assistiva, apareceram na intuição de  auxiliar pessoas que requerem assistência para suas tarefas e atividades diárias, como idosos e pessoas com deficiência.

A proposta de uma linha de robôs assistivos tem sido bem recente e pode ser considerada uma área ainda inovadora no ramo das pesquisas e projetos a depender da sua aplicação. Segundo dados da ONU de 2019, em 2050 a população mundial será de 9,7 bilhões de pessoas, e 16% da população terá idade superior a 65 anos, sendo que em 2019, esse percentual era de 9%. A partir dessa informação é possível ter uma noção de quantos indivíduos passarão a demandar de atenção e cuidados para com o seu dia a dia. 

Devido aos fatos citados, o projeto propõe oferecer um sistema de detecção de posição física humana, com o objetivo de tratar fotos de pessoas em diferentes posições (Em pé, sentado, deitado), a partir de processos de segmentação. Por conseguinte, esses dados serão inseridos em uma rede neural que irá avaliar e classificar a posição do indivíduo. Esse procedimento de classificação visa oferecer a robôs assistivos uma capacidade de reconhecimento da condição em que a pessoa a quem ele auxilia se encontra, a ponto de poder tomar decisões que podem identificar possíveis emergências.

# Metodologia

Os métodos adotados para a elaboração desse projeto foram baseados nas atividades da disciplina citada na apresentação deste documento. Dentre os procedimentos adotados se destacam a limiarização, segmentação e redes neurais convolucionais. As abordagens levantadas foram as descritas a seguir.

## Divisão das etapas

Neste trabalho pretendemos comparar duas maneiras de abordar o problema. Primeiramente, através do dataset composto por silhueta de pessoas, treina-se diversas redes de classificação de imagem, tomando como base as melhores. Então, visto que estas imagens possuem carência de informações, um fine-tunning será realizado com um dataset menor com mais informações. Uma segunda via é explorar redes neurais que realizam segmentação de pessoas, para então criar a imagem já em silhueta, o que entrará direto na rede primeiramente treinada.

## Preparação do dataset

O dataset de silhuetas é composto por 4800 imagens e 4 labels. Cada label possui 1200 imagens e eles estão a primeiro momento separados apenas pelos labels, que são:

* Bending
* Lying
* Standing
* Sitting

Nele é possível definir o estado atual da pessoa, que em um contexto relacionado a entender como o idoso está e em caso de emergência, o sistema robótico tomar uma decisão, ter essa informação se torna essencial.

O primeiro passo para já trabalhar com este dataset, se deu em separá-lo de maneira a poder utilizar o método utilizando dataloader, conforme apresentado em aula. Desta forma, a seguinte divisão foi definida:

* 60% para treinamento;
* 20% para validação;
* 20% para teste

Utilizando a função do pytorch que realiza uma separação aleatória dos dados, foi possível realizar a separação. Um notebook foi gerado apenas para esta etapa e as seeds inicialmente geradas com a divisão do dataset foi salva.

## Treinamento rede de silhuetas
A partir desta primeira base de dados irão ser propostas os treinamentos de algumas redes conhecidas em classificação de imagens.

* AlexNet
* VGG19
* Efficientnet
* Efficient_V2
* Googlenet
* Resnet18

Todas estas redes possuem histórico de terem sido utilizadas para classificar imagens com vários labels. Então a primeiro momento, é necessário alterar o layer de saída para que seja compatível com o problema atual, com 4 labels.

## Fine-Tunning

Devido a baixa complexidade do dataset adotado e que ao testar com imagens reais, a sua acurácia diminui, se faz necessário utilizar de técnicas que consigam utilizar as informações obtidas pelas redes com silhuetas e adicione informações de imagens reais. O fine-tunning propõe exatamente este ponto, pois de maneira bastante objetiva, pretende-se congelar as primeiras camadas da rede, responsáveis pela aquisição de features e então “retreinar” as últimas camadas com um learn rate menor visando então refinar a classificação para casos que não entrem com silhueta.

Para isso será utilizado um dataset menor composto de imagens com os mesmos labels da rede previamente treinada, uma comparação do antes e depois do fine-tunning será apresentado.

## Segunda abordagem

Uma abordagem secundária que trabalha com a imagem diretamente, segmentando-a é ao utilizar uma rede de segmentação de objetos, no caso seres humanos que irá gerar a silhueta e então entrará direto na rede de silhuetas que foi treinada no passo anterior.
A rede a ser utilizada é a [Mask R-CNN](https://github.com/matterport/Mask_RCNN), baseada FPN (Feature pyramid network) e Resnet01 a ser utilizada no desafio COCO (Common Objects in Context). Essa rede então irá encontrar objetos em uma imagem, definirá bounding boxes e a partir delas irá gerar máscaras correspondentes a silhueta do objeto.

## Bases de Dados e Evolução

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Silhouettes of human posture | [Kaggle](https://www.kaggle.com/datasets/deepshah16/silhouettes-of-human-posture) | Imagens segmentadas ,em preto e branco, de silhuetas humanas nas posições de sentado, levantado, deitado e inclinado.
MPII Human Pose Dataset | [MPII](http://human-pose.mpi-inf.mpg.de/#download) | Imagens não tratadas de poses humanas tiradas de vídeos, com diferentes tipos de atividades sendo exercidas.
Common Objects in Context | [COCO - 2017](https://cocodataset.org/#download) | Imagens de pessoas ocultas em diferentes poses, com marcações do tipo bounding-box, mask e modelo articulado.

### Silhouettes of human posture


![IA901a-Page-3 (1)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/6aa4f8c1-aa2e-4b60-a120-58d4165fd48a)

Dataset com imagens de silhuetas humanas em 4 posições (Inclenado, sentado, levantado, deitado) em .jpg, no tamanho total de 4800 imagens, sendo 1200 imagens para cada posição, alocadas em pastas separadas de acordo com a classificação da imagem. As imagens já estão segmentadas e prontas para inserir à rede para treinamento, não sendo necessário qualquer tipo de tratamento a priori. A divisão do conjunto para aplicação em rede será de 60% das imagens para treino, 20% para validação e 20% para teste, sendo as imagens selecionadas através de um script de aleatóriedade. O dataset original e o dataset separado estão contidos nesse repositório.

### MPII Human Pose Dataset

![MPII](http://human-pose.mpi-inf.mpg.de/images/random_activities.png)

Dataset com imagens de poses humanas exercendo 410 atividades diferentes, em .jpg, no tamanho total de 25000 imagens. O dataset conta com anotação em label em arquivo .mat, porém, além do fato de que não será selecionado todo, ele passará por um processo de reanotação para atender aos labels do dataset citado anteriormente para ser inserido numa rede treinada, sendo aplicado como um fine tuning. A quantidade  de imagens a serem selecionadas serão de 200 e serão disponibilizadas nesse repositório.

### COCO

![COCO](https://github.com/liruilong940607/OCHumanApi/raw/master/figures/dataset.jpg)

Este dataset é focado em seres humanos com partes do corpo ocultas, anotadas com bound-box, pose humana, modelo articulado e máscara. Composto por  13360 diferentes posições humanas em 5081 imagens. Este dataset será utilizado para treinar a rede de segmentação, responsável por gerar silhuetas humanas a partir das imagens reais.

# Ferramentas

Ferramentas | Endereço na Web | Resumo descritivo
----- | ----- | -----
Draw.io | https://app.diagrams.net/ | Desenho de arquitetura e Workflow
Google Colab | https://colab.research.google.com/ | Notebooks para implementação de código
Google Drive | https://drive.google.com/ | Repositório de Dados e Imagens
GitHub | https://github.com/ | Repositório de Código
Neptune.ai | https://neptune.ai/ | Experiment tracker and model registry

# Workflow


![IA901a-Workflow (3)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/41344f76-1b96-4a8e-8a64-e50c5d02db02)


# Experimentos e Resultados preliminares

Como informado anteriormente, foram selecionadas 6 redes conhecidas para serem treinadas e determinar qual ferramenta seria ideal para a classificação das imagens de silhuetas. Apesar da Alexnet possuir melhores resultados, ela foi a rede que foi mais treinada durante nossos experimentos, devido ao fato de que ela era a primeira a ser treinada e no meio do processo o notebook atingia seu limite de memória, acarretando na falta de treino das redes seguintes. Devido a esse fato, ficou claro que há uma necessidade de focar somente em uma rede, e dar preferência a redes mais leves como as convolucionais, para evitar problemas de processamento futuros.



## Efficient_V2

Efficient_V2 - Train Acc

![train_epoch_acc (15)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/b2e15b27-23cb-4e13-9637-cc0754f315f2)

Efficient_V2 - Val Acc
![val_epoch_acc (10)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/da729945-cd01-42cf-8a9b-f59e21de62c9)

Efficient_V2 - Train Loss
![train_epoch_loss (12)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/498c50f6-f513-4a2a-992d-d549ae34df33)

Efficient_V2 - Val Loss
![val_epoch_loss (10)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/4b72047a-1cb4-43c6-8def-33f7da18212f)


## AlexNet

AlexNet - Train Acc

![train_epoch_acc (8)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/7a8689ce-fd86-442b-9059-67a9e56ca238)

AlexNet - Val Acc
![val_epoch_acc (4)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/3f415c99-481c-41a2-a979-840c948f553b)

AlexNet - Train Loss
![train_epoch_loss (6)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/a3ff8571-3215-43b3-a870-1a92e6299955)

AlexNet - Val Loss
![val_epoch_loss (4)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/5ffcbf6a-21b4-4967-83da-4ef4e58f5eca)


## VGG19
VGG19 - Train Acc
![train_epoch_acc (13)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/39bd2410-0627-47c2-9e87-acfa9c43315a)

VGG19 - Val Acc
![val_epoch_acc (9)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/c575ddc6-fd23-4029-8eac-df7939b27e72)

VGG19 - Train Loss
![train_epoch_loss (11)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/2b4a7e3e-1489-4860-9e43-6654ac1a222e)

VGG19 - Val Loss
![val_epoch_loss (9)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/6c9db832-2be8-4320-be81-5f13a66c3d71)

## Efficientnet

Efficientnet - Train Acc
![train_epoch_acc (9)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/5556959c-526b-47ed-848d-7f72eb0e1d3d)

Efficientnet - Val Acc
![val_epoch_acc (5)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/17296764-886c-4b90-a611-ccbc4bc92e29)

Efficientnet - Train Loss
![train_epoch_loss (7)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/aa1d47e9-d016-426e-be60-ba3c9202b947)

Efficientnet - Val Loss
![val_epoch_loss (5)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/d975e0ea-17b0-480d-bbf7-10181e13fa20)


## Googlenet

Googlenet - Train Acc
![train_epoch_acc (11)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/6c1982a5-d4ac-4467-9551-8efbf09b4032)

Googlenet - Val Acc
![val_epoch_acc (7)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/72c79211-6b04-49ee-a50f-43c0f7a26c52)

Googlenet - Train Loss
![train_epoch_loss (9)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/b0cf3537-5f0f-49d1-9fae-a406a9fdfe1b)

Googlenet - Val Loss
![val_epoch_loss (7)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/a96ff112-1daf-4377-82b0-223eae2339b1)

## Resnet18

Resnet18 - Train Acc
![train_epoch_acc (12)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/b077d046-95fe-4e4b-bddf-1e204bb94fb1)

Resnet18 - Val Acc
![val_epoch_acc (8)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/ff9ce621-a1c9-4d0c-a7f1-79cac711ee61)

Resnet18 - Train Loss
![train_epoch_loss (10)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/5d5d46a8-438e-4381-9473-87e1c9bd8f60)

Resnet18 - Val Loss
![val_epoch_loss (8)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/096c10eb-e3b6-4bf4-8e4e-c87bcea0c32e)


# Próximos passos

As etapas seguintes são:

- Definir uma rede a ser utilizada para a classificação de silhuetas e refinar atributos [learning rate, épocas etc] (até 26/05)
- Separação de imagens reais do dataset MPII e aplicação na rede treinada como fine tunning (até 09/06)
- Aplicação do segundo método no dataset COCO para comparar com a rede treinada por fine tunning (até 20/06)
- Refinamento e documentação (até 23/06)

## Referências

OCHuman(Occluded Human) Dataset Api https://github.com/liruilong940607/OCHumanApi

ONU, População Mundial deve chegar a 9,7 bilhões de pessoas em 2050. 2019. Disponível em: <https://brasil.un.org/pt-br/83427-populacao-mundial-deve-chegar-97-bilhoes-de-pessoas-em-2050-diz-relatorio-da-onu>. Acesso em: 22 mai. 2023
