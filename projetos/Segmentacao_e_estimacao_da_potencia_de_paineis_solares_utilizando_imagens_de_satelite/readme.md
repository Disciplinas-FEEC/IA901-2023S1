# `Segmentação e estimação da Potência de painéis solares utilizando imagens de satélite`
# <sub> `Solar panels segmentation and power estimation using satellite imagery`

This readme has the project description in English as well :sunglasses:

## Apresentação <br /> <sub> Presentation </sub>


O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*, 
oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

<sub> This project was developed in the post-graduate class *IA901 - Image Processing and Pattern Recognition*, offered in the first semester of 2023 at the University of Campinas (UNICAMP), supervised by Prof. Letícia Rittner, Ph.D., from the Department of Computer Engineering and Automation (DCA) of the School of Electrical and Computer Engineering (FEEC). </sub>

<!---
Incluir nome RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em trios.
-->

Grupo <br /> <sub> Group: </sub>
|Nome <br /><sub> Name </sub>            | RA      | Curso  <br /><sub> Course </sub>                                                                             |
|----------------------------------------|---------|--------------------------------------------------------------------------------------------------------------|
| Juan Carlos Cortez Aucapiña            | 265568  | Doutorado em Engenharia Elétrica (Energia) <br /><sub> Ph.D. Student of Electrical Engineering (Energy)</sub>|
| Luiza Higino Silva Santos              | 264535  | Doutorado em Engenharia Elétrica (Energia) <br /><sub> Ph.D. Student of Electrical Engineering (Energy)</sub>|
| Sérgio Augusto de Almeida Christoforo  | 249522  | Mestrado em Engenharia Elétrica (Energia)  <br /><sub> M.Sc. Student of Electrical Engineering (Energy)</sub>|


## Descrição do Projeto  <br /> <sub> Project Description </sub>
<!---
> Descrição do objetivo principal do projeto, incluindo contexto gerador, motivação.
> Qual problema vocês pretendem solucionar?
> Qual a relevância do problema e o impacto da solução do mesmo?
-->
 
A modernização dos sistemas elétricos é decorrente do desenvolvimento tecnológico, causado principalmente pela busca de fontes de energia renováveis. Com isso, nos últimos anos, houve um aumento considerável no uso de recursos distribuídos de energia, como geração solar fotovoltaica. A geração fotovoltaica é a mais difundida nas residências de todo o mundo, pelo seu caráter renovável e pelo baixo custo de aquisição, quando comparada com outras fontes renováveis. 
 
Uma vez que a modernização dos sistemas elétricos de potência permite que seus usuários tenham agora um papel ativo, injetando potência no sistema, é de extrema importância para as empresas distribuidoras de energia acompanharem a adoção destas tecnologias, para o planejamento de melhorias e expansão. A geração fotovoltaica é, em sua maioria, instalada no telhados de casas ou com médias/grandes usinas. Sendo o sol a fonte de energia, imagens de satélite permitem saber onde estão estes painéis fotovoltaicos.
 
Dessa forma, pretende-se, neste projeto, segmentar painéis solares em imagens de satélite utilizando técnicas de análise de imagem e reconhecimento de padrões. Em seguida, pretende-se estimar a geração do sistema em questão, utilizando redes neurais. 

<sub> Modernizing electrical systems results from technological development, primarily driven by the pursuit of renewable energy sources. As a result, there has been a significant increase in the use of distributed energy resources, such as solar photovoltaic generation. Photovoltaic generation is the most widespread in residential areas worldwide due to its renewable nature and low acquisition cost compared to other renewable sources.
</br>
Given that the modernization of power systems allows users to play an active role by injecting power into the system, energy distribution companies must monitor the adoption of these technologies for planning improvements and expansions. Photovoltaic generation is mainly installed on rooftops or in medium/large-scale solar farms. Since the sun is the energy source, satellite images can provide information on the locations of these photovoltaic panels.
</br>
Therefore, this project aims to segment solar panels in satellite images using image analysis and pattern recognition techniques. Subsequently, the aim is to estimate the system's generation using neural networks.
</sub>
 
# Metodologia  <br /> <sub> Methodology </sub>
<!---
> Proposta de metodologia incluindo especificação de quais técnicas pretende-se explorar. Espera-se que nesta entrega você já seja capaz de descrever de maneira mais específica (do que na Entrega 1) quais as técnicas a serem empregadas em cada etapa do projeto.
-->
 
A metodologia do projeto adotada até agora (22 de maio de 2023) contou com o uso de um dataset anotado disponibilizado num artigo científico, e com redes convolucionais (U-Net, Resnet) para segmentação dos painéis solares. As redes convolucionais são utilizadas para aprenderem os filtros que resultem na segmentação desejada. 

Assim, uma mini U-Net foi treinada do zero e seu desempenho foi avaliado para o dataset do Google. Por outro lado, uma Resnet 50 já treinada teve apenas um processo de fine-tunning com a base do Google para segmentar os painéis solares. A Resnet50 foi testada com as imagens do IGN também.

<sub>The methodology of the project adopted so far (as of May 22, 2023) involved the use of an annotated dataset provided in a scientific article and convolutional networks (U-Net, Resnet) for solar panel segmentation. Convolutional networks are used to learn filters that result in the desired segmentation. </br>Thus, a mini U-Net was trained from scratch, and its performance was evaluated on the Google dataset. On the other hand, a pre-trained Resnet 50 underwent a fine-tuning process using the Google dataset to segment the solar panels. The Resnet50 was also tested with the IGN images.</sub>
 
## Bases de Dados e Evolução  <br /> <sub> Databases and evolution </sub>
<!---
> Elencar bases de dados utilizadas no projeto.
> Para cada base, coloque uma mini-tabela no modelo a seguir e depois detalhamento sobre como ela foi analisada/usada, conforme exemplo a seguir.
-->
 
Base de Dados <br /><sub>Database</sub>| Endereço na Web <br /><sub>Link</sub> | Resumo descritivo <br /><sub>Descriptive Summary</sub>
----- | ----- | -----
Um conjunto de dados colaborativo de imagens aéreas com arranjos fotovoltaicos solares anotados e metadados de instalação</br><sub>A crowdsourced dataset of aerial images with annotated solar photovoltaic  arrays and installation metadata</sub> | https://zenodo.org/record/7358126#.ZDVdg3bMK39 | - Metadados de instalação para mais de 28.000 instalações </br> - Máscaras de segmentação para 13.000 instalações, incluindo 7.000 com anotações de dois provedores de imagem diferentes (Google e IGN) </br> - Metadados de instalação que correspondem à anotação para mais de 8.000 instalações </br> - As aplicações do conjunto de dados incluem a construção de registros de energia solar fotovoltaica completos, mapeamento robusto de instalações de energia solar e análise de conjuntos de dados colaborativos.</br><sub>- Installation metadata for more than 28000 installations </br> - Ground truth segmentation masks for 13000 installations, including 7000 with annotations for two different image providers (Google and IGN). </br> - Installation metadata that matches the annotation for more than 8000 installations. </br> - Dataset applications include end-to-end PV registry construction, robust PV installations mapping, and analysis of crowdsourced datasets.</sub>

Informações fornecidas pelo artigo de referência da base de dados </br>
<sub>Information provided in the reference article of the dataset.</sub>

### A crowdsourced dataset of aerial images with annotated solar photovoltaic  arrays and installation metadata  
<!---
> Faça uma descrição sobre o que concluiu sobre esta base. Sugere-se que respondam perguntas ou forneçam informações indicadas a seguir:
> * Qual o formato dessa base, tamanho, tipo de anotação?
> * Quais as transformações e tratamentos feitos? Limpeza, reanotação, etc.
> * Inclua um sumário com estatísticas descritivas da(s) base(s) de estudo.
> * Utilize tabelas e/ou gráficos que descrevam os aspectos principais da base que são relevantes para o projeto.
-->

A base de dados contém imagens de satélite do Google e do IGN, bem como uma planilha de metadados. Cada um dos provedores de imagens possui duas pastas denominadas 'img' e 'mask'. Na pasta 'img' há várias imagens de satélite, enquanto na pasta 'mask' há a segmentação realizada. Entretanto, há imagens sem painéis solares, e que não possuem máscara. 
</br> <sub>The database contains satellite images from both Google and IGN, as well as a metadata spreadsheet. Each of the image providers has two folders named 'img' and 'mask'. The 'img' folder contains several satellite images, while the 'mask' folder contains the corresponding segmentations. However, there are images without solar panels that do not have a mask. </sub>

Exemplos de imagem e máscara GOOGLE:</br>
![Imagem satélite Google](./data/raw/google/img/GBJXZ623CKGXDH.png)
![Imagem máscara Google](./data/raw/google/mask/GBJXZ623CKGXDH.png)

Exemplos de imagem e máscara IGN:</br>
![Imagem satélite IGN](./data/raw/ign/img/KDZUH41C9ZAKON.png)
![Imagem máscara IGN](./data/raw/ign/mask/KDZUH41C9ZAKON.png)

Além disso, há algumas imagens que apresentam erro:

![Imagem com erro Google](./data/raw/google/img/LYUJB6EC9XBZKI.png)
![Imagem com erro IGN](./data/raw/ign/img/BVSCV7297FJAON.png)


|Provedor de Imagem </br><sub></sub>Image Provider|Imagens </br><sub>Images</sub>|Observações</br><sub>Notes</sub>|
|------------------|-------|-----------|
|Google|Imagens de satélite: 28825 </br>Máscaras: 13303</br>Imagens com erro: 177</br><sub>Images: 28825 </br>Masks: 13303</br>Error Images: 177</sub>|Imagem aberta com PIL tipo 'P'</br><sub>Sattelite Images opened with PIL, type 'P'</sub>|
|IGN   |Imagens de satélite: 17334 </br>Máscaras: 7685</br>Imagens com erro: 95 </br><sub>Sattelite Images: 17334 </br>Masks: 7685</br>Error Images: 95 </sub>|Imagem aberta com PIL tipo 'RGBA'</br><sub> Images opened with PIL type 'RGBA'</sub>|

Para utilização dos datasets para treino da rede convolucional, os conjuntos para treino, validação e teste foram divididos conforme imagens abaixo. Lembrando que nessa primeira etapa não estamos utilizando a base IGN.
</br><sub>For the training of the convolutional network using the datasets, the sets for training, validation, and testing were divided as shown in the images below. It is important to note that in this initial stage, we are not using the IGN dataset.</sub>

#### Google
![Google Dataset Segmentation](./assets/google.png)

#### IGN
![IGN Dataset Segmentation](./assets/ign.png)

# Ferramentas  <br /> <sub> Tools </sub>
<!---
> Ferramentas e/ou bibliotecas já utilizadas e/ou ainda a serem utilizadas (com base na visão atual do grupo sobre o projeto).
-->
- TensorFlow
- Sk Learn
- Matplotlib
- LucidChart (Workflow)
- ...

# Workflow 
<!---
> Use uma ferramenta que permita desenhar o workflow e salvá-lo como uma imagem (Draw.io, por exemplo). Insira a imagem nessa seção.
> Você pode optar por usar um gerenciador de workflow (Sacred, Pachyderm, etc) e nesse caso use o gerenciador para gerar uma figura para você.
> Lembre-se que o objetivo de desenhar o workflow é ajudar a quem quiser reproduzir seus experimentos. 
-->
![Workflow](./assets/workflow.svg)
# Experimentos e Resultados preliminares  <br /> <sub> Experiments and Preliminary Results </sub>
<!---
> Descreva de forma sucinta e organizada os experimentos realizados
> Para cada experimento, apresente os principais resultados obtidos
> Aponte os problemas encontrados nas soluções testadas até aqui
-->
Experimento <br /><sub>Experiment</sub>        | Resultados <br /><sub>Results</sub>             |
| -------------------------------------------- | ------------------------------------------------| 
| U-Net treinada do zero com imagens do Google |Params: 487 297  </br>Cross-entropy Binary Loss: Train - 0.0135 / Val - 0.016 </br> AVG DICE Score Test: 0.7672 |
| ResNet 50 fine-tunning com imagens do Google |Params: 20 676 545 </br>Cross-entropy Binary Loss: Train - 0.0078 / Val - 0.0092 </br>AVG DICE Score Test: 0.9330 </br> Base IGN - AVG DICE Score: 0.5888 |


# Próximos passos  <br /> <sub> Next steps </sub>
<!---
> Liste as próximas etapas planejadas para conclusão do projeto, com uma estimativa de tempo para cada etapa
-->
- [x] Entrega 1 - Formulário com informações gerais do projeto (Sérgio, Juan Carlos e Luiza)
- [x] Entrega 2: 
    - [x] Script 1: Identificação de imagens com erro e dados sobre o dataset 
    - [x] Script 2: para treinamento/teste das redes convolucionais para segmentação 
    - [x] Organização preliminar GitHub 
- [ ] Entrega 3: 
    - [ ] Rede convolucional para segmentação
        - [ ] Junção dos dois scripts da Entrega 2
        - [ ] Data-augmentation nas imagens de entrada para melhoria de resultados 
        - [ ] Otimização dos hiperparâmetros da rede convolucional (grid-search)
        - [ ] Pós-processamento da segmentação realizada
    - [ ] Treinamento e teste da rede neural para estimação da potência da geração fotovoltaica
        - [ ] Definição dos dados de entrada
        - [ ] Avaliação dos resultados
        - [ ] Otimização dos hiperparâmetros da rede neural 
    - [ ] Avaliações quantitativas (segmentação e estimação) e qualitativas (segmentação)
    - [ ] Nova atualização do Git (readme, workflow, notebooks) 
- [ ] Finalização do projeto :tada:

## Referências <br /> <sub> References </sub>
<!---
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.
-->

"A crowdsourced dataset of aerial images with annotated solar photovoltaic  arrays and installation metadata" - https://www.nature.com/articles/s41597-023-01951-4 


"Segmentation of Satellite Images of Solar Panels Using Fast Deep Learning Model" - https://www.ijrer.org/ijrer/index.php/ijrer/article/view/11607/pdf


"Estimation of rooftop solar energy generation using Satellite Image Segmentation" - https://ieeexplore.ieee.org/document/8971578 

"Panel Segmentation: A Python Package for Automated Solar Array Metadata Extraction Using Satellite Imagery" - https://ieeexplore.ieee.org/document/10008194 

"SolarFinder: Automatic Detection of Solar Photovoltaic Arrays" - https://ieeexplore.ieee.org/abstract/document/9111006?casa_token=BRGGve63_NgAAAAA:hV2kmVbSGPzD9zfckkhISndDHbweEyD1FR4axwkAbxfs6EhkRfY2yR5Y0expG1xTn7-3nbiymck 

"Multi-resolution dataset for photovoltaic panel segmentation from satellite and aerial imagery" - https://essd.copernicus.org/articles/13/5389/2021/ 
