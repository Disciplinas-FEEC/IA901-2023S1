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
O projeto é composto por três vertentes distintas de desenvolvimento, as quais trabalham em conjunto para fornecer informações relevantes para o projeto como um todo.

A primeira vertente está relacionada ao tratamento dos dados. Nessa etapa, os dados coletados serão analisados, limpos e preparados para serem utilizados nas próximas fases do projeto.

A segunda vertente envolve o processamento desses dados com o objetivo de extrair características relevantes. Essas características serão utilizadas posteriormente em um algoritmo de classificação conhecido como KNN (K-Nearest Neighbors), que tem como propósito identificar padrões e tomar decisões com base na proximidade dos dados analisados.

A última vertente concentra-se no desenvolvimento de uma CNN (Convolutional Neural Network) utilizando a arquitetura MobileNet. Essa CNN será responsável por classificar as diferentes poses de Yoga. Essa etapa é crucial para comparar os resultados obtidos pela KNN e avaliar a eficácia do modelo de classificação.

**Pré-processamento**:

Verificar a existência de contaminação entre os dados separados para teste, validação e treinamento atravez da utilização da metrica de similariedade SSIM: 

    1- Adimensionalizar as imagens para um tamanho padrão (120x120)
    2- Aplicar uma comparação de uma imagem com as demais e analisa a similaridade usando SSIM.
    3- Remover os dados contaminados e reestruturar as pastas com os dados.

Verificar a existencia de imagens corrompidas ou em formatos diferentes de RGB:

    1- Adicionar processo de verificação de todas as imagem corrompida ou diferente de RGB, analisando a quantidade de canais da imagem e se ela consegue ser lida.

Resultados preliminares encontrados:  

     O método se mostrou eficiente para detectar contaminação presente nos datasets, assim como eliminou imagens corrompidas e imagens diferentes de RGB. 

**Processamento:**

Aplica metodos de processamento de imagens que permitam a extração de caracteristicas que serão usadas na KNN:

   1-  Redimensionar as imagens para (300x300) para que todas tenham o mesmo tamanho. 

   2-  Aplicar filtro para remoção de ruídos, que podem estragar a detecção das poses de Yog:

        
        a- Filtro Bilateral (Um filtro bilateral é um filtro de suavização não linear, com preservação de bordas e redução de ruído para imagens);

        b- Adicionar um filtro Gaussiano (O filtro gaussiano reduz o ruído presente nos dados ao suavizar a imagem. Ele atenua as variações abruptas de intensidade dos pixels, e é capaz de preservar as bordas presentes na imagem). 

    3- Converter as imagens para para escala de cinza para poder aplicar metodos de limiarização e detecção de borda.

    4- Realizar a limiarização na imagem em escala de cinza (Varios metodos são aplicados para verificar qual fornece melhor resultados):

        a- Aplicar OTSU (Tecnica que busc automaticamente o valor de limiar ideal para separar os pixels em duas classes: foreground e background); 

        b- Aplicando Adaptive Mean (técnica de segmentação de imagens em que o valor de limiar é calculado localmente com base na média dos valores de intensidade dos pixels em uma vizinhança ao redor de cada pixe);

        c- Aplicar Watershed (Permite realizar uma segmentação precisa dos objetos presentes na imagem);

        d- Aplicar Histogram-based segmentation (técnica que envolve segmentar uma imagem com base na distribuição das intensidades de pixel em seu histograma. Ela opera analisando o histograma para identificar picos, vales ou outras características que podem ser usadas para diferenciar regiões ou objetos de interesse);

        Os métodos foram aplicados e com base nos resultados, percebeu-se que não foi possivel separar totalmente o fundo da imagem das pessoas fazendo Yoga. Estes métodos continuam sendo analizados e estudados no projeto pelo grupo.

    5- Aplicar Cany o qual é um metodo de detecção de borda conhecido e de facil implementação pela biblioteca OpenCV:

    6- Aplicar métodos para limpar a imagem como transformadas de abertura junto a gradiente morfológico, em busca de eliminar resquicios do plano de fundo em algumas imagens:

    7- Extrair o esqueleto da imagem para então poder extrair caracteristicas importantes que serão usadas na KNN, neste passo serão estudados dois metodos: 

        a- Usar Zhang-Suen;

        b- Thin.

    8- Definir descritores que serão extraídos: distâncias e ângulos entre os pontos do esqueleto. Neste processo será usados tecnicas para extrair pontos chave do esqueleto da imagem:

        a- Aplicar SIFT;
        
        b- Aplicar SURF;
        
        c- aplciar FAST.

    9- Treinar uuma KNN para detectar as classes com base nas caracteristicas levantadas anteriormente:

        a- KNN é um algoritmo de classificação baseado em instâncias e pode ser aplicado diretamente para classificar diferentes movimentos da pessoa. Dado um vetor com as posições espaciais da pessoa em uma imagem, o KNN pode comparar a posição da pessoa com os vizinhos mais próximos e atribuir uma classe correspondente ao movimento com base na maioria dos movimentos dos vizinhos mais próximos.


**Desenvolvimento da CNN:** 

    1- Aplicar somente uma CNN (MobileNet) com ajustes nos hiperparâmetros e fazendo somente uma normalização é um ajuste do tamanho dos dados de entrada.

        a- Rede desenvolvida atualmente com Acuracia de 93% e loss de 0.2, apenas com mudanças nos hiperparâmetros.


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
