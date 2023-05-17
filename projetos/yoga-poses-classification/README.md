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

Trabalhos anteriores de classificação de posturas de yoga utilizam deep learning [1], [2]. Já outros utilizam técnicas de machine learning para extrair atributos relacionados a ângulos e distância entre pontos do esqueleto [3], [4]. Nesse contexto, o objetivo deste trabalho é realizar um estudo comparativo entre o desempenho de uma CNN e uma KNN com atributos extraídos por meio de processamento de imagem para classificar 5 posturas de Yoga. A partir de processamento de imagem, com a aplicação de filtros, detecção de bordas, detecção de esqueletos, criação de descritores, a KNN será treinada com alguns atributos extraídos das imagens e, a partir das métricas de avaliação, o seu desempenho será comparado com o de uma CNN.

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

        Os metosdos foram aplicados e com base nos resultados, percebeu-se que não foi possivel separar totalmente o fundo da imagem das pessoas fazendo Yoga. Estes metodos continuam sendo analizados e estudados no projeto pelo grupo.

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