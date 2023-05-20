# Classificação de Posturas de Yoga
# Yoga Pose Classification

## Apresentação
---
O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação IA901 - Processamento de Imagens e Reconhecimento de Padrões, oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).


Nome                           | RA     | Especialização
-------------------------------|--------|------------
Guilherme Urban Boscolo        | 155642 | Aluno Especial - Engenharia Elétrica
Sara Mirthis Dantas dos Santos | 224018 | Aluna Especial - Engenharia Elétrica
Yasmin Martins Perci           | 271281 | Aluna Especial - Engenharia Elétrica

## Descrição do Projeto

A classificação de posturas de yoga pode ser muito útil para instrutores, praticantes e para o desenvolvimento de aplicativos ou dispositivos de assistência. Além disso, esse classificador pode ser aprimorado para aplicações de monitoramento de progresso individual, correção de posturas inadequadas e, consequentemente, prevenção de lesões dos praticantes. 

Trabalhos anteriores de classificação de posturas de yoga utilizam deep learning [3], [6]. Já outros utilizam técnicas de machine learning para extrair atributos relacionados a ângulos e distância entre pontos do esqueleto [2], [5], [7], [12]. Nesse contexto, o objetivo deste trabalho é realizar um estudo comparativo entre o desempenho de uma CNN e uma KNN com atributos extraídos por meio de processamento de imagem para classificar 5 posturas de Yoga. A partir de processamento de imagem, com a aplicação de filtros, detecção de bordas, detecção de esqueletos, criação de descritores, a KNN será treinada com alguns atributos extraídos das imagens e, a partir das métricas de avaliação, o seu desempenho será comparado com o de uma CNN.

Portanto, a principal contribuição do trabalho é ressaltar a relevância do processamento de imagem, mesmo em um cenário dominado por técnicas de deep learning. Dessa forma, visa-se demonstrar que é possível obter resultados significativos usando algoritmos mais simples e clássicas, como KNN, quando associadas ao processamento de imagens. 

# Metodologia

O projeto é composto por três vertentes distintas de desenvolvimento, as quais trabalham em conjunto para fornecer informações relevantes como um todo.

A primeira vertente está relacionada ao tratamento dos dados. Nessa etapa, os dados coletados são analisados, limpos e preparados.

A segunda vertente envolve o processamento desses dados com o objetivo de extrair atributos importantes para a classificação. Esses atributos são utilizados em um algoritmo de classificação conhecido como KNN (K-Nearest Neighbors), que tem como propósito identificar as classes e classificar as diferentes poses de yoga.

A última vertente concentra-se no desenvolvimento de uma CNN (Convolutional Neural Network) utilizando a arquitetura MobileNet. Essa CNN é responsável por classificar as diferentes poses de Yoga. Essa etapa é crucial para comparar os resultados obtidos pela KNN e avaliar a eficácia do modelo de classificação.

**Pré-processamento**:

Ao trabalhar com dados de domínio público, é essencial realizar algumas etapas iniciais para garantir a integridade dos dados. Uma etapa crucial é verificar se há contaminação entre os conjuntos de dados e validar seus formatos. A presença de dados idênticos em diferentes conjuntos pode causar dificuldades no treinamento do modelo e levar a erros no processo de classificação.

Durante a etapa de pré-processamento, buscou-se analisar a existência de contaminação entre os dados presentes no dataset de treinamento e teste, disponibilizados pelo Kaggle, através da utilização da métrica de similaridade SSIM (Structural Similarity Index).

Outro problema existente nos datasets públicos é a variedade de dados em formatos diferentes e representados por diferentes canais, optou-se em utilizar imagens apenas no formato RGB no formato PNG.

Após o pré-processamento dos dados, separou-se o conjunto de treinamento do  Kaggle em treinamento e validação por meio da criação da pasta “VAL”, onde foram adicionadas as pastas e imagens das 5 posturas de yoga destinadas.

**Processamento:**

Nesta etapa, utilizou-se métodos de processamento de imagens para distinguir as pessoas do restante da imagem, separando-as do plano de fundo. Isso é essencial para isolar as regiões de interesse e facilitar a análise. Uma vez que as pessoas foram identificadas, aplicou-se métodos de extração de características para capturar informações relevantes que possibilitem a classificação das poses que cada pessoa está realizando. Essas características incluem posições das articulações, orientação corporal, ângulos dos membros e outros elementos.

A fim de facilitar o desenvolvimento desta etapa, foram subdivididas em cinco etapas principais: Remoção de ruídos das imagens, transformações para realce, segmentação, detecção de bordas e extração de características.

A primeira etapa envolve a remoção de ruídos das imagens. Isso é importante para eliminar interferências e imperfeições que possam prejudicar a detecção das pessoas nas imagens, para esse método optou-se por estudar quatro diferentes filtros, sendo eles média, gaussiana, bilateral e filtro morfológico ASF(abertura e fechamento), para então levantar qual deveria ser utilizado no projeto.

levantou-se um estudo do canal apropriado a ser trabalhado ( Matiz, saturação, níveis de cinza), com o intuito de melhorar os realces na imagem e facilitar o processo de segmentação das pessoas.

A etapa de segmentação é responsável por separar as pessoas do restante da imagem, isolando-as do plano de fundo e de outros objetos indesejáveis. Usou-se diferentes técnicas de segmentação. Entre as técnicas estão limiarização usando OTSU, Adaptive Mean, Watershed  e Histogram-based segmentation.

Após a segmentação, detectou-se as bordas das imagens, com o objetivo de identificar de forma mais precisa as bordas dos corpos das pessoas. Para isso, estudou-se o método Canny.

Avaliou-se qual caminho de técnicas fornece características relevantes para servirem de treinamento na KNN.

**Desenvolvimento da CNN:** 

Com o objetivo de criar um estudo comparativo entre os métodos de processamento de imagem e o uso de uma rede convolucional, desenvolveu-se uma CNN a partir do modelo MobileNet V2,onde ajustou-se apenas os hiperparâmetros após uma normalização dos dados. O modelo MobileNet V2 foi escolhido pela quantidade razoável de 2.230.277 parâmetros treinados, considerado adequado para o tamanho do dataset. Essa arquitetura de rede neural foi inicialmente adaptada para dispositivos móveis e ambientes com recursos restritos, diminuindo significativamente o número de operações e memória necessária, mantendo uma boa precisão.

Com relação ao processamento das imagens, realizou-se um redimensionamento para o tamanho (128,128) e uma normalização. Após realizar testes variando os hiperparâmetros da rede (optimizer, learning rate, número de épocas, tamanho do batch), alcançou-se um modelo com desempenho satisfatório.


## Bases de Dados e Evolução


# Ferramentas


# Workflow

# Experimentos e Resultados preliminares


# Próximos passos

# Referências

[1] ACHARYA, Akruti. Guide to Image Segmentation in Computer Vision: Best Practices. 2023. Disponível em: https://encord.com/blog/image-segmentation-for-computer-vision-best-practice-guide/. Acesso em: 10 maio 2023.

[2] AGRAWAL, Yash; SHAH, Yash; SHARMA, Abhishek. Implementation of machine learning technique for identification of yoga poses. In: 2020 IEEE 9th international conference on communication systems and network technologies (CSNT). IEEE, 2020. p. 40-43. https://doi.org/10.1109/CSNT48778.2020.9115758 

[3] ASHRAF, Faisal Bin et al. Yonet: A neural network for yoga pose classification. SN Computer Science, v. 4, n. 2, p. 198, 2023. https://doi.org/10.1007/s42979-022-01618-8 

[4] DEEPIKA, Yamuna. Python OpenCV – Pose Estimation. Disponível em: https://www.geeksforgeeks.org/python-opencv-pose-estimation/. Acesso em: 09 maio 2023.

[5] DESAI, Miral; MEWADA, Hiren. A novel approach for yoga pose estimation based on in-depth analysis of human body joint detection accuracy. PeerJ Computer Science, v. 9, p. e1152, 2023. https://peerj.com/articles/cs-1152/

[6] GARG, Shubham; SAXENA, Aman; GUPTA, Richa. Yoga pose classification: a CNN and MediaPipe inspired deep learning approach for real-world application. Journal of Ambient Intelligence and Humanized Computing, p. 1-12, 2022.https://doi.org/10.1007/s12652-022-03910-0

[7] PALANIMEERA, J.; PONMOZHI, K. Classification of yoga pose using machine learning techniques. Materials Today: Proceedings, v. 37, p. 2930-2933, 2021. https://doi.org/10.1016/j.matpr.2020.08.700  

[8] PEDRINI, Hélio; SCHWARTZ, William Robson. Análise de imagens digitais: princípios, algoritmos e aplicações. Cengage Learning, 2008.

[9] RAJENDRAN, Arun Kumar; SETHURAMAN, Sibi Chakkaravarthy. A Survey on Yogic Posture Recognition. IEEE Access, v. 11, p. 11183-11223, 2023.https://doi.org/10.1109/ACCESS.2023.3240769 

[10] SANDLER, Mark et al. Mobilenetv2: Inverted residuals and linear bottlenecks. In: Proceedings of the IEEE conference on computer vision and pattern recognition. 2018. p. 4510-4520. https://doi.org/10.48550/arXiv.1801.04381 

[11] WALIA, Mrinal Singh. Guide to Image Segmentation in Computer Vision: Best Practices. 2022. Disponível em: https://www.analyticsvidhya.com/blog/2022/01/a-comprehensive-guide-on-human-pose-estimation/. Acesso em: 10 maio 2023.

[12] WU, Yubin et al. A computer vision-based yoga pose grading approach using contrastive skeleton feature representations. In: Healthcare. MDPI, 2021. p. 36. https://doi.org/10.3390/healthcare10010036 
