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

# Preparação do dataset

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

ONU, População Mundial deve chegar a 9,7 bilhões de pessoas em 2050. 2019. Disponível em: <https://brasil.un.org/pt-br/83427-populacao-mundial-deve-chegar-97-bilhoes-de-pessoas-em-2050-diz-relatorio-da-onu>. Acesso em: 22 mai. 2023
