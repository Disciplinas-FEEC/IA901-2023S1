# Classificação de melanoma em imagens de lesões de pele
# Melanoma classification in skin lesions images

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*, 
oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC). 


 |Nome  | RA | Curso|
 |--|--|--|
 | Johsac Isbac Gomez Sanchez  | 216401  | Doutorado em Engenharia Elétrica|
 | Robson Assis Colares  | 264369  | Doutorado em Engenharia Elétrica |
 | Suellen Sena da Silva  | 177261  | Mestrado em Engenharia da Computação|


## Descrição do Projeto

O objetivo do projeto é desenvolver um sistema para classificação de lesões de pele entre malignas e benignas com o uso de arquiteturas de redes neurais convolucionais. O estudo visa fornecer uma ferramenta eficiente para ajudar na detecção precoce de tumores malignos, contribuindo para o diagnóstico médico e reduzindo a taxa de falsos negativos (ou seja, classificar como benignas lesões que na verdade são malignas). Adicionalmente, garantir que o classificador tenha a sensibilidade (recall) alta também é de extrema importância para o projeto, dado que o tratamento precoce pode ser mais benéfico ao paciente do que não diagnosticá-lo e o tratamento ser tardio. 

<p align="center">
  <img src="assets/Tabela_confusao.png">
</p>

**Taxa de falso negativo:** 

$$P(\hat{f}(x)=\text{Benigno} | f(x)=\text{Maligno})=\frac{FN}{FN+VN}$$

**Recall:**
$$P(\hat{f}(x)=\text{Maligno} | f(x)=\text{Maligno})=\frac{VN}{FN+VN}$$

Dessa forma, o contexto gerador do projeto consiste no desafio de validar uma arquitetura que consiga classificar lesões de pele em imagens médicas. Com uma base de dados de 33.007 imagens, das quais apenas 582 são de tumores malignos, o projeto enfrenta o desafio de lidar com um conjunto de dados altamente desequilibrado. A classificação precisa dessas imagens é essencial para identificar corretamente os casos malignos e benignos, a fim de fornecer  diagnóstico e tomada de decisões quanto ao tratamento tratamento adequados. É interessante apontar que a estimativa é de que médicos experientes reconheçam 70% dos casos de lesões benignas, apenas com inspeção visual [7,8].

Portanto, a motivação para esse projeto é a importância da detecção precoce de lesões de pele malignas, pois possuem maior probabilidade de serem tratadas com sucesso se diagnosticado em estágios iniciais. A utilização de arquiteturas de redes neurais convolucionais, combinada com técnicas avançadas de processamento de imagem, permite uma análise mais precisa e automatizada das lesões, podendo reduzir a taxa de falsos negativos. Isso pode auxiliar médicos e especialistas a tomarem decisões mais assertivas, agilizando o processo de diagnóstico e melhorando os resultados dos pacientes.

**Qual problema vocês pretendem solucionar?**

O problema que buscamos resolver é o erro de classificação de lesões malignas classificadas como benignas. Tal erro pode levar a um atraso no diagnóstico e tratamento adequado, o que é fundamental para a sobrevida de paciente. Ao desenvolver um sistema de classificação mais preciso, buscamos identificar corretamente os casos de melanoma, o que permitirá a detecção precoce e o tratamento oportuno. 

**Qual a relevância do problema e o impacto da solução do mesmo?**

O câncer de pele é uma das formas mais comuns de câncer em todo o mundo, e a detecção precoce pode gerar um impacto positivo em taxas de mortalidade associadas a lesões malignas de pele. A solução desse problema, por meio do desenvolvimento de um sistema de classificação automatizado, possui certamente um impacto significativo na área médica. Primeiramente, proporciona uma ferramenta automatizada e precisa para auxiliar os médicos no diagnóstico de lesões de pele, aumentando a eficiência e reduzindo a possibilidade de erros humanos. Além disso, ao diminuir a taxa de falsos negativos, o sistema permite uma triagem mais eficiente, identificando corretamente os casos malignos que requerem atenção e tratamento imediato. Essa solução também pode contribuir para a redução dos custos de saúde, uma vez que a detecção precoce e correta pode evitar tratamentos desnecessários e mais invasivos.

# Metodologia 

*1. Pré-processamento de dados:*
Durante o treinamento de redes neurais convolucionais (CNNs), é comum realizar um pré-processamento adequado nos dados de entrada para atender aos requisitos da rede e otimizar o treinamento. Neste contexto, um exemplo de pré-processamento aplicado é a redimensionamento das imagens para um tamanho específico, como 224x224 pixels, utilizando interpolação bilinear. Essa etapa é necessária para atender às demandas de entrada de redes pré-treinadas, como a ResNet50.

Além disso, é importante organizar os dados de maneira adequada para facilitar a leitura durante o treinamento. Para isso, a classe DataLoader do pacote TensorFlow é comumente utilizada. Essa classe oferece recursos para carregar e pré-processar os dados de forma eficiente, otimizando o processo de treinamento da rede.Para o estudo, os dados foram organizados seguindo os requisitos da classe DataLoader. O conjunto de dados foi dividido em duas partes: 20% foi reservado para validação e o restante foi utilizado para treinamento. No entanto, devido à necessidade de garantir que os pacientes não se repitam entre os conjuntos, as porcentagens foram ajustadas levemente.

Outro passo essencial no pré-processamento é a padronização dos pixels das imagens. Nesse caso, os valores dos pixels foram normalizados para que estejam no intervalo entre -1 e 1. Essa normalização é importante para manter a escala dos pixels consistente, facilitando o treinamento de redes complexas. Além disso, ajuda a reduzir a influência de outliers e melhora a capacidade do modelo de generalizar para novos exemplos.

Além dessas etapas, foram adotadas estratégias de amostragem para lidar com possíveis desequilíbrios de classes nos dados. Essas estratégias incluíram downsampling da classe majoritária, oversampling da classe minoritária e a combinação de ambas. Essas abordagens foram testadas para avaliar seus efeitos nas arquiteturas de rede neural em análise.

Em resumo, o pré-processamento de dados para o treinamento de redes neurais convolucionais envolve várias etapas, como redimensionamento, padronização dos pixels e estratégias de amostragem. Essas etapas visam preparar os dados de forma adequada, melhorar a capacidade de generalização do modelo e otimizar o processo de treinamento.

*2. Data augmentation:*  

A avaliação inicial de lesões de pele é realizada levando em conta características visíveis a olho nu, bem como características ampliadas por meio de técnicas de dermatoscopia e coleta do material para avaliação anatomopatológica. Alguns dos principais aspectos considerados são a assimetria da lesão, bordas irregulares ou mal definidas, lesões com múltiplas cores e lesões com diâmetro maior, que podem indicar malignidade. A seguir, seguem imagens do conjunto que exemplificam a dificuldade em diferenciar as lesões apenas através de sua aparência.

<p align="center">
  <img src="assets/lesions.jpg" width="650" height="310">
</p>

Dessa forma, estudos que avaliam técnicas de aumentação de dados com foco em lesões de pele foram considerados. Essas transformações são fundamentais para diminuir influência da cor de pele e ruídos na discriminação do modelo. Além de filtros, foram testada técnicas que possuem função que diminuir a aparência de pelos na imagem, sem comprometer as lesões, garantindo que o modelo não associe essas características com as diferentes classes. Nas próximas seções serão definidos quais transformações apresentaram os melhores resultados. Abaixo estão algumas transformações que foram consideradas para a aumentação de dados:

- *Ben Graham* 

<p align="center">
  <img src="assets/ben_graham.jpg">
</p>

- *Hair remove*

<p align="center">
  <img src="assets/hair_remove.jpg"  width="510" height="250">
</p>

Alternativamente, foram consideradas as seguintes transformações nas imagens com o objetivo de torná-las menos heterogêneas [1]:

- *width_shift_range* e *height_shift_range*: desloca horizontalmente e verticalmente, respectivamente, por uma fração da largura ou altura da imagem original, auxiliando o modelo a aprender a reconhecer objetos em diferentes posições.

- *shear_range*: aplica um cisalhamento aleatório na imagem, distorcendo-a ao longo do eixo horizontal, podendo ser útil para ensinar o modelo a lidar com objetos inclinados.

- *zoom_range*: aplica um zoom aleatório na imagem, ampliando-a ou reduzindo-a, com objetivo de treinar o modelo a aprender a reconhecer objetos em diferentes escalas.

- *brightness_range*: ajusta aleatoriamente o brilho das imagens, aumentando ou diminuindo seus valores de pixel. Isso pode ajudar o modelo a ser mais robusto em relação a variações de iluminação.

- *fill_mode*: o parâmetro determina como os pixels são preenchidos quando ocorre um deslocamento ou distorção da imagem. O valor 'nearest' preenche os pixels ausentes com o valor do pixel mais próximo.

As tranformações geraram  o seguinte resultado: 


<p align="center">
  <img src="assets/top_augmentation.jpg"  width="400" height="350">
</p>

*3. Avaliação e validação:*

Para viabilizar a possibilidade de avaliar o desempenho das redes treinadas o conjunto de dados foi divido entre treinamento e validação. A escolha de não utilizar parte do conjunto como teste parte do princípio de que os dados já são extremamente desbalanceados, portanto, informações da classe de malignos seria perdida para o treinamento. Entretanto, existem mais conjuntos públicos com imagens de lesões com o mesmo objetivo de classificar câncer de pele, havendo possibilidade de conjuntos externos serem utilizados como teste futuramente. 

Todo o treinamento foi realizado configurando-se a rede para maximizar métricas de sensibilidade e área sob a curva (area under curve - AUC). Para avaliação pós treinamento, foi considerado a taxa de falsos negativos, além da matriz de confusão. 

*4. Requisitos para treinamento*
A aquisição de recursos computacionais foi necessária devido ao tempo consumido nos treinamentos sem GPU (e mesmo à impossibilidade de trabalhar com o conjunto de dados inteiro), optou-se pela aquisição de recursos computacionais esporádicos via Google Colab.

*5. Metodologia Simple-Complex:*

Foi avaliado simultaneamente arquiteturas complexas e consolidadas como Resnet50, MobileNet, EfficientNet e modelos mais simples (começando com pouca profundidade e pequena quantidade de filtros), afim de realizar a tarefa com o menor custo computacional possível e possibilitar mais abordagens de pré-processamento.

## Bases de Dados e Evolução

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
SIIM-ISIC Melanoma Classification | https://www.kaggle.com/competitions/siim-isic-melanoma-classification/data |  O conjunto possui imagens de lesões de pele, tanto de lesões benignas quanto malignas.

A base possui 33007 imagens do tipo jpg, totalizando 20 GB de tamanho com anotações de identificador exclusivo da imagem, identificador único do paciente, sexo, idade aproximada do paciente no momento da imagem, localização do site com imagem, informações de diagnóstico detalhadas e indicador de malignidade da lesão. Para este projeto, serão utilizadas apenas as imagens jpg, totalizando 33007 arquivos.

Lesão | Frequencia | Proporção
----- | ----- | -----
Benigno | 32427 |  98%
Maligno | 580 |  2%

Não houve necessidade de reanotação dos dados para o conjunto proposto. No entanto, a base possui 2056 pacientes distintos, onde muitos se repetem por possuir mais de uma lesão de pele. Ainda, é importante ressaltar que, para a separação dos conjuntos de treino e validação, garantiu-se que pacientes repetidos tivessem todas as suas imagens em apenas um dos conjuntos. Dessa forma, não há possibilidade de que a rede treinada confunda a classificação de lesões malignas ou benignas por reconhecer o padrão de pele do paciente nas fotos.


Estatísicas Qualitativas | Proporções
----- | ----- 
Sexo | 52% homens e 48% mulheres


Estatísticas quantitativas | Mínimo | Máximo | Média
----- | ----- | ----- | -----
Idade | 0 | 90 | 55

# Ferramentas
O projeto será realizado com o auxílio do Google Colab para treinamento das redes com GPUs adquiridas A100, V100 e T4. Ainda, bibliotecas como:
Keras e Tensorflow, pela facilidade de manuseio dos algoritmos de aprendizado de máquina e processamento de imagens;
OpenCV, para *data augmentation*;
Sklearn, para avaliar métricas de resultados dos classificadores;
OS e Shutil, para movimentação dos arquivos entre diretórios;
Numpy, para realização de cálculos diversos;
Matplotlib, utilizada para plotar gráficos variados; e
Draw.IO, para confecção do Workflow.

# Workflow

<p align="center">
  <img src="assets/workflow.png">
</p>

# Experimentos 

Os experimentos foram realizados através de diferentes arquiteturas, tamanhos de batch e transformações de *data augmentation*. Ainda, devido à quantidade de imagens, os testes foram realizados em um conjunto diminuído de dados, visando garantir que as primeiras aplicações iriam ocorrer corretamente ao longo de todo o fluxo de pré processamento, treinamento e validação dos resultados. Dessa forma, os experimentos baseados em batch tamanho 32, otimizadores Adam e SGD (*stochastic gradient descent*) e treinamentos de 20 épocas basearam-se da seguinte forma:

Experimento 1 - CNN simples com downsampling da classe majoritária e  <br>
----- 
Para a primeira etapa do projeto, 10% do conjunto de imagens benignas foram aleatoriamente selecionadas, visando facilitar os primeiros treinamentos e garantir o fluxo do que estava sendo desenvolvido e aplicado. Ainda, a aumentação de dados aplicada consiste em testar diferentes faixas de deslocamento horizontal e vertical, distorções de cisalhamento aleatórias nas imagens, zoom aleatório e ajustes de brilho e matiz. Por fim, uma rede desenvolvida do zero foi criada, consistindo em camadas convolucionais, normalização por batch, pooling global de média para extrair características da imagem e uma camada densa final para realizar a classificação das imagens. 

Os resultados de acurácia são significativos, porém ainda há o mesmo problema de todas as amostras da classe maligna ser classificada como benigna. 

<p align="center">
  <img src="assets/cnn1_downsampling.png">
</p>


**Taxa de falso negativo:** 

$$\frac{FN}{FN+VN}=\frac{118}{118+0}=1$$

Com a mesma rede implementada no exemplo anteior, foi realizado o treinamento conjunto de dados completo, considerando exatamente a mesma divisão entre treinamento e validação. Nesse cenário, 24402 imagens foram utilizadas no treinamento da rede e 8608 imagens foram usadas para validação. Também a título de comparação, todas as imagens foram inseridas na rede convolucional com dimensões 224 x 224 e com a aplicação das mesmas técnicas de data augmentation.

Os resultados do experimento anterior persistiram e um dos principais problemas foi o tempo despendido para treinamento da rede neural convolucional. Ainda, obsera-se que a diminuição do desbalanceamento não conduz a um resultado favorável de classificação da classe com menores amostras.

<p align="center">
  <img src="assets/cnn1_complete_data.png">
</p>

**Taxa de falso negativo:** 

$$\frac{FN}{FN+VN}=\frac{147}{147+0}=1$$

Experimento 2 - Resnet50 conjunto completo
----- 
Ao considerar que o principal objetivo é minimizar a taxa de falsos negativos, aplicou-se uma arquitetura mais complexa no conjunto, previamente treinada em imagens. A ResNet50 é uma arquitetura proposta em 2015 e ainda muito utilizada no contexto de imagens. Ela é conhecida por sua capacidade de treinar redes muito profundas com maior eficiência, superando o desafio de degradação do desempenho que ocorre ao aumentar a profundidade da rede. Ainda, a rede foi pré-treinada em um grande conjunto de dados chamado ImageNet, que contém mais de um milhão de imagens rotuladas em 1000 classes diferentes. Dessa forma, utilizar essa arquitetura permite aproveitar os recursos de alto nível aprendidos durante o treinamento para extrair características relevantes das imagens e aplicá-las a novas tarefas, como detecção de objetos, segmentação de imagens e muito mais. 

Embora de grande complexidade, os resultados apresentados a seguir demonstram a dificuldade de discriminar as lesões de pele entre malignas e benignas. Os ganhos foram de apenas 6 acertos na classe de lesões malignas e, consequentemente, a taxa de falsos negativos (predizer como begnigno, quando na verdade é maligno) foi de 96%.

<p align="center">
  <img src="assets/resnet50.png">
</p>

**Taxa de falso negativo:** 

$$\frac{FN}{FN+VN}=\frac{141}{141+6}=0.96$$

---

# Experimentos intermediários

Na etapa preliminar do projeto, o grupo enfrentou limitações de recursos e a rápida exaustão dos mesmos. Diante disso, foram consideradas alternativas que permitissem contornar essas restrições, optando por redes mais leves e eficientes para os próximos testes.

<p align="center">
  <img src="assets/top_accuracy.jpg" width="500" height="400">
</p>

*Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."* 

Foi observado que arquiteturas como EfficientNetB3 apresentam alta eficiência mesmo com um número inferior de parâmetros em comparação com a ResNet-50, Ainda, embora não listado no gráfico, a MobileNet possui as mesmas características e também foi considerada como uma rede promissora. Com base nessa constatação, os experimentos subsequentes levaram em consideração essas arquiteturas, bem como redes mais simples, a fim de avaliar seu desempenho. No entanto, mesmo com a escolha de redes mais leves, ainda era necessário lidar com a demanda de memória RAM para processar as imagens. Para contornar essa limitação, o grupo adquiriu unidades de computação do Google Colab, permitindo o acesso a GPUs mais potentes, como A100, V100 e T4, por períodos de tempo mais longos. Essa abordagem possibilitou realizar os experimentos de forma mais eficiente e obter resultados relevantes para o projeto, ainda que bom um conjunto reduzido de imagens.

Experimento 3 - CNN com ténicas de reamostragem

# Complexidade média 
Em vista da baixa performance de arquiteturas com CNN simples (poucas camadas e filtros), passou-se à exploração de arquiteturas mais complexas, porém com número de parâmetros ainda inferior às arquiteturas consideradas Estado da Arte, a fim de acelerar o processo de treinamento e testar técnicas de pré-processamento. Os modelos foram treinados por 100 épocas. Ainda, com o objetivo de obter mais informações acerca dos impactos do processamento e evitar maior variabilidade do modelo, o grupo optou por fixar o número de camadas nos testes intermediários e limitar a quantidade de filtros. A arquitetura utilizada é apresentada abaixo, consistindo de entrada, cinco camadas convolucionais [9] (todas com *batch normalization*) e duas camadas totalmente conectadas para classificação. A técnica de dropout é aplicada para regularização. 

<p align="center">
  <img src="assets/rede.JPG"  width="600" height="350">
</p>

A primeira configuração foi testada com 32, 32, 256, 256 e 512 filtros nas camadas convolucionais, e a segunda configuração foi testada com 64, 64, 128, 128, 256 filtros, respectivamente. O conjunto de dados da classe benigna foi subamostrada 14 vezes ou 2396 imagens, resultando em um conjunto de dados de treinamento com 2396 imagens benignas e 426 malignas (como no caso anterior).

Os resultados de acurácia são significativos, porém como esperado para problemas desbalanceados, ainda há o mesmo problema de todas as amostras da classe maligna ser classificada como benigna. A matriz de confusão foi semelhante para ambas as configurações.

Rede 1 - 32, 32, 256, 256 e 512 filtros; Rede 2 - 64, 64, 128, 128, 256 filtros
<p align="center">
  <img src="assets/rede1-2.png">
</p>

Como as CNNs simples não apresentaram bom desempenho na melhoria da taxa de falsos negativos, caracterizamos os efeitos das variadas técnicas de *augmentatio*n nas CNNs de menor e média complexidade, avaliando a AUC para dez épocas de treinamento. Em ordem de eficácia na melhoria do falso negativo, destacam-se as técnicas de *Height Shift Range*, *Width Shift Range* e *Zoom Range*. As outras técnicas aplicadas mostraram pouca ou nenhuma influência quando consideradas individualmente. Buscas mais detalhadas e com mais épocas podem ser feitas para avaliar o efeito das técnicas de pré-processamento em CNNs de baixa complexidade. Para efeitos de teste, mantivemos apenas o Height Shift Range como técnica de augmentation, já que seu resultado superou o resultado das outras técnicas. 

# Complexidade baixa

Por fim, passou-se à experimentação da última técnica: oversampling considerando todo o conjunto de dados de treinamento, ou seja: 23964 imagens. A reamostragem das imagems com lesões malignas foram realizadas aleatoriamente, até que as classes ficassem balanceadas. Novamente, os testes foram realizados a partir de uma configuração mais simples possível, composta por duas camadas convolucionais de filtros, e uma camada totalmente conectada de 100 neurônios. O resultado foi bastante surpreendente para 50 épocas, e acabou elegendo a técnica de oversampling, juntamente com normalização e técnicas de aumentação de dados, como a melhor metodologia aplicável a CNNs de baixa complexidade. Novamente devido à precariedade de recursos computacionais, este experimento com número grande de imagens foi executado por apenas 50 épocas.

<p align="center">
  <img src="assets/rede3.png">
</p>

$$\frac{FN}{FN+VN}=\frac{119}{119+28}=0.81$$

Experimento 4 - MobileNetV2
----- 

Também conhecida como uma arquitetura desenvolvida para aplicações de visão computacional em dispositivos com recursos computacionais limitados, a MobilNet foi projetada para alcançar um equilíbrio entre a precisão do modelo e a eficiência computacional. Para tanto, seu diferencial são camadas de convolução profunda separável em vez de convoluções padrão, considerando duas etapas: a primeira é uam convolução em que cada filtro opera em um canal de entrada, e a sgunda etapa é uma convolução ponto a ponto, onde um filtro linear é aplicado a cada para de características separadamente. Isso permite uma redução significativa no número de parâmetros e operações em comparação com as convoluções padrão, tornando a MobileNet mais leve e rápida.

Após diversos testes, os resultados aqui reportados foram obtidos através do treinamento com batch tamanho 64, peso das classes durante o treinamento, utilização da mesma técnica de *augmentation* anterior e aplicação de downsampling da classe majoritaria e  oversampling da classe minoritária. O melhor resultado encontrado foi a partir da seguintes definições:


Por fim, a técnica de oversampling da classe de malignos não apresentou resultados significativos, causando mais confusão no modelo para discriminar as classes corretamente. Portanto, apenas o downsampling foi considerado e o modelo foi treinado apenas com 5000 da classe de benignos. 

<p align="center">
  <img src="assets/mobilenet_100.png">
</p>

Embora a rede apresente resultados positivos para classificação de tumores malignos, o modelo aumentou a taxa de de falsos positivos, ou seja, classifica muitas lesões como malignas, quando na verdade são benignas. Em um contexto médico, é considerado principalmente se a conduta irá apresentar mais benefícios ou maleficios para o paciente. Como o tratamento de lesões consideradas malignas pode ser complexo e doloroso, não é interessante considerar os resultados do algoritmo. 

$$\frac{FN}{FN+VN}=\frac{116}{116+31}=0.79$$


Experimento 5 - EfficientNet B3
----- 

A EfficientNet caracteriza uma família de arquiteturas de redes neurais convolucionais projetada para alcançar um equilíbrio ideal entre precisão e eficiência computacional em tarefas de visão computacional. Essa família de redes foi desenvolvida por Mingxing Tan e Quoc V. Le, pesquisadores do Google, e sua primeira versão foi introduzida em 2019.

Baseada em um conceito chamado "escalabilidade composta" (compound scaling), a escala da rede é aumentada de forma proporcional em todas as dimensões relevantes, em vez de simplesmente aumentar a profundidade ou a largura. Isso é conseguido por meio de uma fórmula que define a relação entre as diferentes escalas, permitindo um aumento harmonioso e controlado da arquitetura. Além disso, o EfficientNet utiliza blocos residuais chamados de MBConv (Mobile Inverted Bottleneck Convolution). Esses blocos são projetados para serem computacionalmente eficientes, combinando convoluções de ponto de entrada (*input point-wise*) e convoluções de ponto de saída (*output point-wise*) com uma camada de convolução profunda no meio.

A partir de diferentes treinamentos, o melhor resultado para essa rede foi considerando downsampling do conjunto de benignos utilizados para treinamento, batch tamanho 64, otimizador Adam, learning rate = 0.001, agumentation proposto pela referência [1] e treinamento por 100 épocas, considerando os pesos das classes para tentativa de balancear os erros.

<p align="center">
  <img src="assets/efficientb3.png">
</p>

$$\frac{FN}{FN+VN}=\frac{86}{86+63}=0.58$$

Embora a taxa de falsos positivos seja a melhor entre todos os experimentos, é importante considerar que a taxa de falsos positivos também aumentou significativamente. Tal resultado exemplifica a dificuldade em discriminar as duas classes diferentes de lesões, mesmo com as técnicas de *augmentation* apropriadas para o contexto do projeto.


# Conclusões  

Ao longo dos experimentos preliminares até o resultado final deste projeto, nosso principal objetivo era reduzir a taxa de falsos negativos. Portanto, foi possível alcançar uma redução de 42% nessa taxa através da utilização da EfficientNet. Esse progresso é um reflexo dos aprendizados e melhorias contínuas realizadas ao longo do processo. Entretanto, é importante que exista um equilíbrio entre os error reportados pela rede escolhida. Embora haja sucesso em relação as taxas de falso negativos, o modelo apresentou falhas na proporção de falsos positivos, o que pode eleger preocupações desnecessárias ao médico e paciente. Portanto, o *trade off* entre ter um modelo com alta sensibilidade de diagnóstico para malignidade a custo de aumentar a taxa de falsos positivos é uma discussão complexa que deve ser considerada junto a profissionais da saúde.

-----
# Trabalhos Futuros

Utilizar informações adicionais disponíveis nos conjuntos públicos de melanoma, como idade, sexo, localização da lesão e cor da pele, associado com as características da própria lesão, fornece mais contexto e informações relevantes para os algoritmos de classificação. Essas informações adicionais auxiliam a identificar padrões específicos relacionados a diferentes grupos demográficos ou características específicas dos pacientes. A abordagem de ensemble permite combinar as previsões e decisões dos diferentes modelos ou fontes de informação, o que leva a resultados mais satisfatórios e confiáveis, já que diferentes modelos podem capturar diferentes aspectos da complexidade do problema.

Alternativamente, ao considerar que redes neurais devem focar e destacar as partes mais importantes de uma imagem de entrada, foi avaliado o mecanismo de *Soft-Attention*, que permite que uma rede neural alcance esse objetivo. Estudos avaliam a eficácia do Soft-Attention em arquiteturas de redes neurais profundas. O objetivo central do Soft-Attention é aumentar o valor das características importantes e suprimir as características que introduzem ruído. Redes combinadas com a ténica alcançam uma precisão de 93,7% no conjunto de dados de melanomas ISIC-2017.

Por fim, arquitetura GANs (Generativas Adversariais) são utilizadas  para criar imagens sintéticas de lesões de pele com melanoma é estudada como estratégia promissora. GANs são modelos de aprendizado de máquina que consistem em duas redes neurais competindo entre si: o gerador e o discriminador. O gerador cria amostras sintéticas, enquanto o discriminador tenta distinguir entre amostras reais e sintéticas. Ao treinar essas redes em conjunto, o gerador aprende a produzir amostras cada vez mais realistas, enquanto o discriminador aprimora sua capacidade de distinguir entre amostras reais e sintéticas. Ao aplicar GANs para gerar imagens sintéticas de lesões de pele com melanoma, é possível explorar os padrões e características presentes nessas lesões e produzir imagens que se assemelhem às lesões reais. Isso pode ser valioso em várias áreas, como pesquisa médica, treinamento de algoritmos de diagnóstico por imagem e criação de conjuntos de dados de treinamento para modelos de aprendizado de máquina.

## Referências 
1. Perez, F. et al. Data augmentation for skin lesion analysis. Granada, Spain, September 16 and 20, 2018, Proceedings 5 (pp. 303-311). Springer International Publishing.
2. Ha, Qishen, Bo Liu, and Fuxu Liu. "Identifying melanoma images using efficientnet ensemble: Winning solution to the siim-isic melanoma classification challenge." arXiv preprint arXiv:2010.05351 (2020).
3. Zhang, Yiming, and Chong Wang. "SIIM-ISIC melanoma classification with DenseNet." 2021 IEEE 2nd International Conference on Big Data, Artificial Intelligence and Internet of Things Engineering (ICBAIE). IEEE, 2021.
4. Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks." International conference on machine learning. PMLR, 2019.
5. Ding, Jiaqi, et al. "Two-Stage Deep Neural Network via Ensemble Learning for Melanoma Classification." Frontiers in Bioengineering and Biotechnology 9 (2022): 1355.
6. Kanti Datta, Soumyya, et al. "Soft-Attention Improves Skin Cancer Classification Performance." arXiv e-prints (2021): arXiv-2105.
7. Dinnes, Jacqueline, et al. "Visual inspection for diagnosing cutaneous melanoma in adults." Cochrane Database of Systematic Reviews 2018.12 (1996).
8. UptoDate: https://www.uptodate.com/contents/melanoma-clinical-features-and-diagnosis
9. E. Nasr-Esfahani et al., "Melanoma detection by analysis of clinical images using convolutional neural network," 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), Orlando, FL, USA, 2016, pp. 1373-1376, doi: 10.1109/EMBC.2016.7590963.
10. A. Bissoto and S. Avila. "Improving Skin Lesion Analysis with Generative Adversarial Networks", in Anais Estendidos do XXXIII Conference on Graphics, Patterns and Images, Evento Online, 2020, pp. 70-76, doi: https://doi.org/10.5753/sibgrapi.est.2020.12986.

