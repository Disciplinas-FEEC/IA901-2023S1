# Classificação de melanoma em imagens de lesões de pele
# Melanoma classification in skin lesions images

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*, 
oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em trios.
> |Nome  | RA | Curso|
> |--|--|--|
> | Johsac Isbac Gomez Sanchez  | 216401  | Doutorado em Engenharia Elétrica|
> | Robson Assis Colares  | 264369  | Doutorado em Engenharia Elétrica |
> | Suellen Sena da Silva  | 177261  | Mestrado em Engenharia da Computação|


## Descrição do Projeto
**Descrição do objetivo principal do projeto, incluindo contexto gerador, motivação.**

O principal objetivo do nosso projeto é desenvolver um modelo CNN que seja capaz de classificar lesões cutâneas de melanoma, a fim de reduzir a taxa de falsos negativos na classificação de imagens de lesões cutâneas malignas dadas lesões benignas. Temos um banco de dados de 33.126 imagens onde 32.542 são lesões benignas e 584 imagens são lesões malignas, um banco de dados bastante desbalanceado, sendo um desafio treinar o conjunto de dados, dado o alto viés que apresenta no tamanho da amostra em suas categorias.


**Qual problema vocês pretendem solucionar?**

O problema que pretendemos resolver é o erro de classificação dos melanomas malignos como benignos. Isso pode levar a um atraso no diagnóstico e tratamento adequados, o que é fundamental para a saúde e a vida dos pacientes. Ao desenvolver um sistema de classificação mais preciso, buscamos identificar corretamente os casos de melanoma maligno, o que permitirá a detecção precoce e o tratamento oportuno.


**Qual a relevância do problema e o impacto da solução do mesmo?**

A relevância desse problema reside na alta taxa de mortalidade associada ao melanoma maligno. Se conseguirmos melhorar a precisão da classificação e reduzir os falsos negativos, poderemos identificar mais pacientes com melanoma maligno em estágio inicial, aumentando suas chances de sobrevivência e melhorando sua qualidade de vida. A solução proposta teria um impacto significativo na detecção e tratamento do melanoma maligno, beneficiando um grande número de pessoas e potencialmente salvando vidas.


# Metodologia
> Proposta de metodologia incluindo especificação de quais técnicas pretende-se explorar. Espera-se que nesta entrega você já seja capaz de descrever de maneira mais específica (do que na Entrega 1) quais as técnicas a serem empregadas em cada etapa do projeto.

## Bases de Dados e Evolução
> Elencar bases de dados utilizadas no projeto.
> Para cada base, coloque uma mini-tabela no modelo a seguir e depois detalhamento sobre como ela foi analisada/usada, conforme exemplo a seguir.

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
SIIM-ISIC Melanoma Classification | https://www.kaggle.com/competitions/siim-isic-melanoma-classification/data |  O conjunto possui imagens de lesões de pele e 

> Faça uma descrição sobre o que concluiu sobre esta base. Sugere-se que respondam perguntas ou forneçam informações indicadas a seguir:
> * Qual o formato dessa base, tamanho, tipo de anotação?
A base possui 88251 imagens do tipo dicom, jpg e tfrecords, totalizando 116.16 GB de tamanho e anotações de identificador exclusivo da imagem, identificador único do paciente, sexo, idade aproximada do paciente no momento da imagem, localização do site com imagem, informações de diagnóstico detalhadas e indicador de malignidade da lesão na imagem.
> * Quais as transformações e tratamentos feitos? Limpeza, reanotação, etc.
> * Inclua um sumário com estatísticas descritivas da(s) base(s) de estudo.
> * Utilize tabelas e/ou gráficos que descrevam os aspectos principais da base que são relevantes para o projeto.

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
