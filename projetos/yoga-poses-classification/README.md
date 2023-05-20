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
O objetivo deste trabalho é realizar um estudo comparativo entre o desempenho de uma CNN e um algoritmo clássico para classificar posturas de Yoga. A partir de processamento de imagem, como aplicação de filtros, detecção de bordas, detecção de esqueletos, criação de descritores, entre outros, o modelo clássico será treinado com alguns atributos extraídos das imagens e, a partir das métricas de avaliação, o seu desempenho será comparado com o de uma CNN.


# Metodologia

O projeto é composto por três vertentes distintas de desenvolvimento, as quais trabalham em conjunto para fornecer informações relevantes como um todo.

A primeira vertente está relacionada ao tratamento dos dados. Nessa etapa, os dados coletados são analisados, limpos e preparados.

A segunda vertente envolve o processamento desses dados com o objetivo de extrair atributos importantes para a classificação. Esses atributos são utilizados em um algoritmo de classificação conhecido como KNN (K-Nearest Neighbors), que tem como propósito identificar as classes e classificar as diferentes poses de yoga.

A última vertente concentra-se no desenvolvimento de uma CNN (Convolutional Neural Network) utilizando a arquitetura MobileNet. Essa CNN é responsável por classificar as diferentes poses de Yoga. Essa etapa é crucial para comparar os resultados obtidos pela KNN e avaliar a eficácia do modelo de classificação.

**Pré-processamento**:

Ao trabalhar com dados de domínio público, é essencial realizar algumas etapas iniciais para garantir a integridade dos dados. Uma etapa crucial é verificar se há contaminação entre os conjuntos de dados e validar seus formatos. A presença de dados idênticos em diferentes conjuntos pode causar dificuldades no treinamento do modelo e levar a erros no processo de classificação.

Durante a etapa de pré-processamento, buscou-se analisar a existência de contaminação entre os dados presentes no dataset de treinamento e teste, disponibilizados pelo Kaggle, através da utilização da métrica de similaridade SSIM (Structural Similarity Index).

As imagens presentes nos datasets possuem tamanhos variados e através de uma inspeção visual de todos os dados, foi possível verificar que existem casos onde há contaminação, por diferenciação apenas do tamanho da imagem. Assim optou-se por primeiro padronizar todas as imagens nos dataset para o tamanho de (120x120), antes de se aplicar a métrica SSIM.  A métrica de similaridade compara características estruturais das imagens, levando em consideração elementos como texturas, contrastes e detalhes visuais. Ele calcula valores de similaridade que variam de -1 até 1.  

Outro problema existente nos datasets públicos é a variedade de dados em formatos diferentes e representados por diferentes canais, optou-se em utilizar imagens apenas no formato RGB no formato PNG, eliminando-se todo o restante.

Após o pré-processamento dos dados, separou-se o conjunto de treinamento do  Kaggle em treinamento e validação por meio da criação da pasta “VAL”, onde foram adicionadas as pastas e imagens das 5 posturas de yoga destinadas.

**Processamento:**

Nesta etapa, utilizou-se métodos de processamento de imagens para distinguir as pessoas do restante da imagem, separando-as do plano de fundo. Isso é essencial para isolar as regiões de interesse e facilitar a análise. Uma vez que as pessoas foram identificadas, aplicou-se métodos de extração de características para capturar informações relevantes que possibilitem a classificação das poses que cada pessoa está realizando. Essas características incluem posições das articulações, orientação corporal, ângulos dos membros e outros elementos.

A fim de facilitar o desenvolvimento desta etapa, foram subdivididas em cinco etapas principais: Remoção de ruídos das imagens, transformações para realce, segmentação, detecção de bordas e extração de características.

A primeira etapa envolve a remoção de ruídos das imagens. Isso é importante para eliminar interferências e imperfeições que possam prejudicar a detecção das pessoas nas imagens, para esse método optou-se por estudar quatro diferentes filtros, sendo eles (média, gaussiana, bilateral e filtro morfológico ASF(abertura e fechamento), para então levantar qual deveria ser utilizado no projeto.

levantou-se um estudo do canal apropriado a ser trabalhado ( Matiz, saturação, níveis de cinza), com o intuito de melhorar os realces na imagem e facilitar o processo de segmentação das pessoas.

A etapa de segmentação é responsável por separar as pessoas do restante da imagem, isolando-as do plano de fundo e de outros objetos indesejáveis. Usou-se diferentes técnicas de segmentação. Entre as técnicas estão limiarização usando OTSU, Adaptive Mean, Watershed  e Histogram-based segmentation.

Após a segmentação, detectou-se as bordas das imagens, com o objetivo de identificar de forma mais precisa as bordas dos corpos das pessoas. Para isso, estudou-se o método Canny.

Por fim, para a extração de características estudou-se métodos  como esqueleto associado a um SIFT que retorna as posições relativas da pessoa na imagem, ou código da cadeia, o qual é um método de descritor.

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