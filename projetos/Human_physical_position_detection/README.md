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

Neste trabalho pretendemos comparar duas maneiras de abordar o problema. Primeiramente, através do dataset composto por silhueta de pessoas, treina-se diversas redes de classificação de imagem, tomando como base as melhores. Então, visto que estas imagens possuem carência de informações, um fine-tuning será realizado com um dataset menor com mais informações. Uma segunda via é explorar redes neurais que realizam segmentação de pessoas, para então criar a imagem já em silhueta, o que entrará direto na rede primeiramente treinada.

## Preparação do dataset

O dataset de silhuetas é composto por 4800 imagens e 4 labels. Cada label possui 1200 imagens e eles estão a primeiro momento separados apenas pelos labels, que são:

* Bending
* Lying
* Standing
* Sitting

Nele é possível definir o estado atual da pessoa, que em um contexto relacionado a entender como o idoso está e em caso de emergência, o sistema robótico tomar uma decisão, ter essa informação se torna essencial.

O primeiro passo para já trabalhar com este dataset, se deu na remoção da classe "bending", pois sua definição pode ser ambígua a pessoas em pé, principamente quando relacionado a idosos. O segundo passo, separa-se das imagens de maneira a poder utilizar o método utilizando dataloader, conforme apresentado em aula. Desta forma, a seguinte divisão foi definida:

* 60% para treinamento;
* 20% para validação;
* 20% para teste

Utilizando a função do pytorch que realiza uma separação aleatória dos dados, foi possível realizar a separação. Um notebook foi gerado apenas para esta etapa e as seeds inicialmente geradas com a divisão do dataset foi salva.

## Treinamento rede de silhuetas
A partir desta primeira base de dados irão ser propostas os treinamentos de algumas redes conhecidas em classificação de imagens.

* AlexNet
* VGG19
* Efficientnet-B0
* Efficientnet-B2
* Efficientnet_V2
* Googlenet
* Resnet18

Todas estas redes possuem histórico de terem sido utilizadas para classificar imagens com vários labels. Então a primeiro momento, é necessário alterar o layer de saída para que seja compatível com o problema atual, com 3 labels. Entretanto, após inícios dos testes, o grupo percebeu que se tornava inviável o teste de muitas redes, devido a limitação da memória computacional e de tempo. Visto isso, foi realizado um estudo correlacionando a relação de custo computacional e acurácia entregue, a partir disso o grupo conseguiu concluir que o uso da rede de modelo Efficientnet-B2 era o mais viável por entregar uma boa precisão com um baixo número de parametros, garantindo uma melhor qualidade na classificação sem atingir o limite da mémoria disponibilizada na GPU dos notebooks desenvolvidos.

## Fine-tuning

Devido a baixa complexidade do dataset adotado e que ao testar com imagens reais, a sua acurácia diminui, se faz necessário utilizar de técnicas que consigam utilizar as informações obtidas pelas redes com silhuetas e adicione informações de imagens reais. O fine-tuning propõe exatamente este ponto, pois de maneira bastante objetiva, pretende-se congelar as primeiras camadas da rede, responsáveis pela aquisição de features e então “retreinar” as últimas camadas com um learn rate maior visando então refinar a classificação para casos que não entrem com silhueta.

Para isso será utilizado um dataset menor composto de imagens com os mesmos labels da rede previamente treinada, com adição de um data augmentation para melhores resultados, e uma comparação do antes e depois do fine-tuning será apresentado.

## Segunda abordagem

Uma abordagem secundária que trabalha com a imagem diretamente, e ao utilizar uma rede de segmentação de objetos, no caso seres humanos que irá gerar a silhueta e então entrará direto na rede de silhuetas que foi treinada no passo anterior.
A rede a ser utilizada é a [Mask R-CNN](https://github.com/matterport/Mask_RCNN), baseada FPN (Feature pyramid network) e Resnet01 a ser utilizada no desafio COCO (Common Objects in Context). Essa rede então irá encontrar objetos em uma imagem, definirá bounding boxes e a partir delas irá gerar máscaras correspondentes a silhueta do objeto. As imagens utilizadas serão as mesmas aplicadas na rede com finetuning, visando uma comparação com as mesmas imagens.

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

Dataset com imagens de poses humanas exercendo 410 atividades diferentes, em .jpg, no tamanho total de 25000 imagens. O dataset conta com anotação em label em arquivo .mat, porém, além do fato de que não será selecionado todo, ele passará por um processo de reanotação para atender aos labels do dataset citado anteriormente para ser inserido numa rede treinada, sendo aplicado como um fine tuning. 

A primeiro momento o grupo tentou utilizar as anotações que vinham associadas ao dataset, entretanto ao utilizá-lo foi possível perceber que nem todas as imagens possuem labels, só as que são usadas para treino no desafio. Desta forma então, de maneira manual foi realizada a separação das imagens, gerando um dataset com 340 imagens, sendo 112 deitados, 115 sentados e 113 em pé. Por fim, para separar as imagens em teste, treino e validação, utilizou-se a proporção de 70% para treino, 15% para validação e 15% para teste, utilizando o notebook "splitdataset_finetuning".

### COCO

![COCO](https://github.com/liruilong940607/OCHumanApi/raw/master/figures/dataset.jpg)

Este dataset é focado em seres humanos com partes do corpo ocultas, anotadas com bound-box, pose humana, modelo articulado e máscara. Composto por  13360 diferentes posições humanas em 5081 imagens. Este dataset foi utilizado para treinar a rede de segmentação, responsável por gerar silhuetas humanas a partir das imagens reais.

# Ferramentas

Ferramentas | Endereço na Web | Resumo descritivo
----- | ----- | -----
Draw.io | https://app.diagrams.net/ | Desenho de arquitetura e Workflow
Google Colab | https://colab.research.google.com/ | Notebooks para implementação de código
Google Drive | https://drive.google.com/ | Repositório de Dados e Imagens
GitHub | https://github.com/ | Repositório de Código
Neptune.ai | https://neptune.ai/ | Experiment tracker and model registry

# Workflow


![IA901a-Workflow (4)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/2c1ee0df-6712-43aa-830e-9f5eacf6c490)


# Experimentos e Resultados 

Como informado anteriormente, foram selecionadas 7 redes conhecidas para serem treinadas e determinar qual ferramenta seria ideal para a classificação das imagens de silhuetas. Apesar da Alexnet possuir melhores resultados nos primeiros registros, ela foi a rede que foi mais treinada durante nossos experimentos, devido ao fato de que ela era a primeira a ser treinada e no meio do processo o notebook atingia seu limite de memória, acarretando na falta de treino das redes seguintes. Devido a esse fato, ficou claro que há uma necessidade de focar somente em uma rede, e dar preferência a redes mais leves como as convolucionais, para evitar problemas de processamento futuros.

Como informado anteriormente, a rede utilizada para treino foi a Efficientnet-B2 e seu desempenho foi muito bom com a rede de silhuetas, a tal ponto que sua precisão com o dataset causou um overfitting, e seus resultados em testes apontava uma precisão de mais de 90%.

A aplicação dessa rede em imagens com maior informação, e sem processamento, apontou resultados muito baixos, chegando a 27% de precisão e levemente melhorado com processamento de normalização, chegando ao máximo de 45%.

Após a aplicação do fine tuning os resultados apresentaram melhoras com aumentando de até no máximo 75% de precisão, enquanto que para a aplicação do dataset de imagens segmentadas que aplicam a máscara citada na segunda abordagem, os resultados foram próximos com valores levemente estáveis no nível de 66%.

## Efficient_B2

Train Accuracy

![train_epoch_acc (15)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/b2e15b27-23cb-4e13-9637-cc0754f315f2)

Val Accuracy
![val_epoch_acc (10)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/da729945-cd01-42cf-8a9b-f59e21de62c9)

Train Loss
![train_epoch_loss (12)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/498c50f6-f513-4a2a-992d-d549ae34df33)

Val Loss
![val_epoch_loss (10)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/4b72047a-1cb4-43c6-8def-33f7da18212f)

## Fine Tuning vs Efficientnet-B2 

Train Accuracy
![train_epoch_acc (15)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/2e0fdc05-ea8c-4874-9f7b-699166ffb6b4)

Val Accuracy
![val_epoch_acc (10)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/45a1c8eb-ba72-40b6-99f5-442fb83b0840)

Train Loss
![train_epoch_loss (12)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/cb19535b-4985-4e89-87fe-73afce34b01e)

Val Loss
![val_epoch_loss (10)](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/15105b42-4a55-4037-a8a6-435bbf118c19)

Com uma breve análise na matriz confusão, como já se tinha definido quanto a retirada da classe "bending" para evitar muito equivoco por parte da rede, foi perceptível que não havia muita confusão entre as posições lying e standing, o que se acredita que a posição da câmera em relação às pessoas nas imagens possibilitaram que a rede conseguisse diferenciar bem as posições, considerando que é comum que a imagens de pessoas em pé estejam na vertical e a de pessoas deitadas na horizontal. Um ponto de vista diferente referente a confusão das pessoas sentadas, que foi mais aparente acreditando-se pelo fato de algumas fotos estarem com as pessoas bem próximas ou sem estar com o corpo inteiro exposto.

## Matriz Confusão MPII com Fine Tuning
![cf_MPII_ft](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/8d4ab38c-dc11-4f80-be1b-283b963d544c)

## Matriz Confusão MPII Sem Fine Tuning
![cf_MPII_no_ft](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/01a4a8d1-4178-4d46-845d-538ef6d9d0ea)

## Matriz Confusão Coco sem Fine Tuning
![cf_coco_no_ft](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/9c57e5df-d4b7-4028-ad5a-9259589e63c4)

## Matriz Confusão Human Silhouettes sem Fine Tuning
![cf_human_silhouettes_no_ft](https://github.com/OctavioGuaschi/IA901-2023S1/assets/1149623/00ecbcca-7557-4031-96de-145ef72623c9)

## Discussão

Apesar de tamanha precisão, a rede treinada foi aplicada em um dataset com imagens com maiores informações e o resultado perceptível era de que ela não trazia bons resultados com imagens em outros contextos, no caso de imagens sem segmentação. Com a aplicação de um novo dataset com imagens com mais informações para fine tuning, foi possível ver que o processo trouxe uma melhora para o reconhecimento das classes (posições humanas) nas imagens reais sem segmentação, e por uma questão de comparação foram aplicadas as imagens segmentadas com a rede de máscara da segunda abordagem na rede treinada sem fine tuning, e ambos resultados deram valores próximos a 60%, podendo especular que são métodos que possuem boas propostas como solução para uma maior pluralidade no reconhecimento de posições.

As matrizes confusões apontam uma maior dificuldade de distinguir posições de sentado com as outras, possivelmente por poder ser considerada um meio termo, tornando assim evidente que a rede tem a necessidade de reconhecer melhor esse padrão para poder saber diferenciar.

## Conclusão

O trabalho proposto visou o desenvolvimento de uma rede baseada em machine learning, utilizando redes convolucionais, para identificação da posição de seres humanos com o intuito de ser aplicado em robôs assistivos. Datasets específicos dessas posições não existem no meio de casa, pois normalmente são classificados em das mais diversas atividades e filtrar todo um dataset se torna inviável pelo custo de tempo que tem. Os métodos apresentados trouxeram um ganho de performance, pois mesmo utilizando uma baixa quantidade de imagens reais, foi possível obter uma acurácia aceitável. Mas não se pode concluir muito apenas levando em consideração a acurácia, por isso fazendo o contrário, a partir de imagens reais foram geradas as silhuetas e jogadas na rede antes do fine tunning, obtendo um resultado similar a rede com fine tunning. A grande diferença é que a rede de segmentação é muito mais complexa e seu treinamento muito mais "pesado" quando comparado ao método apresentado pelo grupo. 

Outro ponto interessante, está diretamente relacionado na análise da matriz de confusão que mostra que as imagens reais e suas silhuetas podem ser ambíguas, ou por não apresentarem o corpo completo do indíviduo, ou pela imagem estar em uma perspectiva diferente o que dificulta a estimação da rede. Esta análise comprova o problema abordado, onde muitas imagens "enganam" e fazem as redes se confundir. Para o grupo então, solucionar o problema da falta de dataset com especifidade do tema abordado com fine tunning foi interessante para entender esse novo conceito, como também ao aplicar técnicas de data augmentation, mesmo tendo poucas imagens é possível dar uma robustez a rede e treinar a rede com imagens que se diferem em leves aspectos.

## Trabalhos Futuros

Com a introdução da proposta quanto à possibilidade de uso do reconhecimento de imagens para robótica assistiva, este mesmo trabalho pode ser vinculado com protótipos robóticos para reconhecimento de condições de pessoas carentes de atenção, como idosos e pessoas com deficiência. Com isso, a análise da posição de pessoas pode ser um procedimento para detectar possíveis situações de emergência como desmaios e acidentes domésticos.

## Referências

OCHuman(Occluded Human) Dataset Api https://github.com/liruilong940607/OCHumanApi

ONU, População Mundial deve chegar a 9,7 bilhões de pessoas em 2050. 2019. Disponível em: <https://brasil.un.org/pt-br/83427-populacao-mundial-deve-chegar-97-bilhoes-de-pessoas-em-2050-diz-relatorio-da-onu>. Acesso em: 22 mai. 2023

Pytorch FineTuning Tutorial https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html

Efficientnet Source Code https://pytorch.org/vision/main/_modules/torchvision/models/efficientnet.html#EfficientNet_B2_Weights
