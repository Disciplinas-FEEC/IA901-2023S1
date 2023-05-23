# `<Identificação de Ocorrências de Tumor em Imagens de Células e Tecidos
# `<Identification of Tumor Occurrences in Cell and Tissue Images`


## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*,
oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em trios.
> |Nome  | RA | Curso|
> |--|--|--|
> | Eduardo Parducci  | 170272  | Graduação em Eng. de Computação|
> | Gianni Shigeru Setoue Liveraro | 265945 | Doutorado em Física Aplicada|
> | Pedro Rodrigues Corrêa  | 243236  | Graduação em Física|


## Descrição do Projeto

O câncer é um dos acometimentos mais letais e prevalentes na população mundial, sendo um termo comum que engloba mais de 100 doenças que ocorrem em diferentes órgãos do corpo humano (próstata, pulmão, boca, pele, cólon e etc). A principal característica do câncer é o crescimento desenfreado de células anormais, que eventualmente podem formar tumores e se espalhar para outros órgãos gerando complicações, processo conhecido como metástase [2].
A principal causa para o surgimento desta doença é a mutação de células comuns, que são alterações na estrutura do DNA contido no núcleo. Existem diversos fatores de risco que podem propiciar a ocorrência destas mutações, como o consumo de substâncias tóxicas ou exposição a fontes de radiação, por exemplo - contudo, este é um fenômeno que também pode ter causas internas, podendo ocorrer em indivíduos por fatores hereditários e imunológicos. 
Todos os anos, milhares de pessoas são acometidas pelo câncer no Brasil e no mundo, e muitas vidas ainda são perdidas. Uma das formas mais eficazes de tratamento (que pode envolver práticas de radioterapia ou quimioterapia) consiste no diagnóstico precoce, momento ao qual a doença ainda está nos primeiros estágios de desenvolvimento e não gerou complicações para o paciente. Nesta fase, maiores são as chances de sucesso no tratamento e de sobrevivência a longo prazo. O diagnóstico precoce pode ocorrer não apenas por exames de rotina, mas também com abordagens que envolvam procedimentos de biópsia, em que partes do tecido na região acometida pelo câncer são analisadas em microscopia.  É nesse cenário que a capacidade de desenvolver algoritmos capazes de analisar imagens de células em lâminas de tecidos e identificar células cancerígenas se torna extremamente valiosa.
As lâminas de tecidos contêm informações visuais sobre as células e suas características morfológicas. No entanto, a análise manual dessas imagens requer um tempo significativo e está sujeita a variações e erros humanos. Ao desenvolver algoritmos de análise de imagens, é possível automatizar e agilizar o processo de detecção de células cancerígenas, melhorando a tomada de decisão dos médicos e levando a práticas mais personalizadas no tratamento de cada paciente [3].
Perante o exposto, este projeto consiste em aplicar técnicas de aprendizado de máquina para classificar imagens de lâminas de tecidos de diferentes órgãos. Serão feitas duas classificações: a primeira irá separar as imagens com presença ou não de tumor no tecido a partir da análise de células neoplásicas, que podem estar presentes (indicação de tumor) ou não; a segunda classificação é do tipo de tecido representado pela imagem da lâmina de microscopia entre dezenove classes distintas. Para o primeiro tipo de classificação, serão utilizadas máscaras com a segmentação das células neoplásicas, as quais extraímos a classe binária da imagem (0: não possui célula neoplásica, 1: possui célula neoplásica).
Finalmente, como objetivo secundário do projeto, buscaremos comparar a performance de classificação de duas abordagens. A primeira consiste no uso de um modelo de Deep Learning, o qual fará a extração de atributos automaticamente e, posteriormente, a classificação das imagens; enquanto a segunda envolve extração manual de atributos e a classificação das imagens com algoritmos tradicionais de Machine Learning. 

# Metodologia
Para o desenvolvimento do projeto, utilizamos o dataset 'PanNuke', disponibilizado no site Kaggle. Mais informações sobre as imagens podem ser vistas a seguir.

## Bases de Dados e Evolução

Resumo sobre a base: 
O dataset 'PanNuke' consiste em 7901 imagens RGB com dimensões (256, 256, 3) de rotuladas em 19 tipos de tecido humano. Para cada imagem RGB, estão associadas 7 máscaras de segmentação de núcleos celulares também rotuladas. Tanto as imagens dos tecidos quanto as máscaras estão no formato .npy. Os tipos de tecido são Breast, Colon, Lung, Kidney, Prostate, Bladder, Ovarian, Esophagus, Pancreatic, Thyroid, Skin, Adrenal Gland, Cervix, Bile Duct, Testis, Head Neck, Liver, Stomach, Uterus. As máscaras, por sua vez, são imagens de seis bandas. Cada banda carrega a informação da segmentação de algum elemento específico na imagem:

0: Células neoplásicas;
1: Inflamatórias;
2: Células do tecido conectivo/mole;
3: Células mortas;
4: Epiteliais;
6: Background. 

Alguns exemplos podem ser vistos abaixo, assim como a distribuição das imagens.
<p align="left">
    <img src="projetos/Classificação de Ocorrências de Câncer em Imagens de Celulas e Tecidos/assets/exemplos dataset.png" height="350">
</p>

# Ferramentas
> Ferramentas e/ou bibliotecas já utilizadas e/ou ainda a serem utilizadas (com base na visão atual do grupo sobre o projeto).

# Workflow
> Use uma ferramenta que permita desenhar o workflow e salvá-lo como uma imagem (Draw.io, por exemplo). Insira a imagem nessa seção.
> Você pode optar por usar um gerenciador de workflow (Sacred, Pachyderm, etc) e nesse caso use o gerenciador para gerar uma figura para você.
> Lembre-se que o objetivo de desenhar o workflow é ajudar a quem quiser reproduzir seus experimentos.

# Experimentos e Resultados preliminares
> Descreva de forma sucinta e organizada os experimentos realizados
> Para cada experimento, apresente os principais resultados obtidos
> Aponte os problemas encontrados nas soluções testadas até aqui

# Próximos passos
> Liste as próximas etapas planejadas para conclusão do projeto, com uma estimativa de tempo para cada etapa

## Referências (ATUALIZAR SE NECESSÁRIO)
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.
