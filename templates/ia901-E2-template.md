# `Detecção de posição física humana`
# `<Project Title in in English>`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA901 - Processamento de Imagens e Reconhecimento de Padrões*, 
oferecida no primeiro semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em trios.
> |Nome  | RA | Curso|
> |--|--|--|
> | Octavio S Guaschi  | 218390  | Mestrado em Eng. Elétrica|
> | Breno Portela  | 253502  | Mestrado em Eng. Elétrica|
> | Cesar Bastos  | 264521  | Doutorado em Eng. Elétrica|


## Descrição do Projeto

O objetivo desse projeto é tratar fotos de pessoas em diferentes posições (Em pé, sentado, deitado), visando construir um modelo articulado da estrutura humana. Por conseguinte, esses dados serão inseridos em uma rede neural que irá avaliar a posição do indíviduo.

> Descrição do objetivo principal do projeto, incluindo contexto gerador, motivação.
> Qual problema vocês pretendem solucionar? 
> Qual a relevância do problema e o impacto da solução do mesmo?

Qual problema vocês pretendem solucionar? 
(form> Quais os principais desafios que o tema de projeto escolhido irá trazer para o grupo? )
Realizar segmentação das pessoas nas imagens e a diferenciação entre em pé e deitado.

# Metodologia
> Proposta de metodologia incluindo especificação de quais técnicas pretende-se explorar. Espera-se que nesta entrega você já seja capaz de descrever de maneira mais específica (do que na Entrega 1) quais as técnicas a serem empregadas em cada etapa do projeto.

Métodos visto em sala a serem utilizados - Limiarização, segmentação e redes neurais convolucionais.


Avaliação de resultados; qualitativo ou quantitativo. 
Avaliaremos com base em um baixo nível de falso positivo e falso negativo, sem priorizar um entre os dois, considerando a alta possibilidade de falsa detecção para posições de em pé e deitado, avaliando de forma mais quantitativa do que qualitativa, pois casos de falso positivo ou falsos negativos não são graves.

Métrica utilizada para avaliar os resultados quantitativamente - Acurácia, loss e matriz confusão.


## Bases de Dados e Evolução
> Elencar bases de dados utilizadas no projeto.
> Para cada base, coloque uma mini-tabela no modelo a seguir e depois detalhamento sobre como ela foi analisada/usada, conforme exemplo a seguir.

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Título da Base | http://base1.org/ | Breve resumo (duas ou três linhas) sobre a base.
Drive Projeto | https://drive.google.com/drive/folders/1zanWzsALmWM7ZpEFpN4s_mhRE8C3CFTW?usp=sharing | Drive com imagens RAW utilizadas no projeto

> Faça uma descrição sobre o que concluiu sobre esta base. Sugere-se que respondam perguntas ou forneçam informações indicadas a seguir:
> * Qual o formato dessa base, tamanho, tipo de anotação?
> * Quais as transformações e tratamentos feitos? Limpeza, reanotação, etc.
> * Inclua um sumário com estatísticas descritivas da(s) base(s) de estudo.
> * Utilize tabelas e/ou gráficos que descrevam os aspectos principais da base que são relevantes para o projeto.

# Ferramentas
> Ferramentas e/ou bibliotecas já utilizadas e/ou ainda a serem utilizadas (com base na visão atual do grupo sobre o projeto).

Ferramentas | Endereço na Web | Resumo descritivo
----- | ----- | -----
Draw.io | https://app.diagrams.net/ | Desenho de arquitetura e Workflow
Google Colab | https://colab.research.google.com/ | Notebooks para implementação de código
Google Drive | https://drive.google.com/ | Repositório de Dados e Imagens
GitHub | https://github.com/ | Repositório de Código
Neptune.ai | https://neptune.ai/ | Experiment tracker and model registry

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

http://human-pose.mpi-inf.mpg.de/#dataset

https://www.kaggle.com/datasets/deepshah16/silhouettes-of-human-posture)
