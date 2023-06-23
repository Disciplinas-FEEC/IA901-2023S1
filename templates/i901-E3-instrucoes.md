# IA901 - Projeto - Entrega final (E3)

O objetivo do projeto final desta disciplina é fazer com que os alunos tentem resolver um problema real utilizando as técnicas discutidas ao longo da disciplina, tanto de processamento de imagens quanto de reconhecimento de padrões.

## Entrega Final

A entrega final do projeto consiste em duas etapas:
* Apresentação do Projeto a ser realizada em sala de aula no dia 27/06, em ordem de apresentação a ser comunicada no ambiente Classroom da disciplina. A apresentação valerá 2,0 pontos da nota final do projeto. 
* Atualização do repositório GitHub já criado anteriormente. A versão final do repositório será avaliada, valendo 6,0 pontos da nota final do projeto.

De maneira análoga à entrega E2, a atualização do repositório GitHub inclui:
* Atualização do arquivo README.md do projeto incluindo as seções do template abaixo.
* Após a finalização da edição do conteúdo da segunda entrega, atribuição da tag de release **2023.1_IA901_E3** no repositório de origem.
* **Pull request**  do projeto no  **branch  principal** até a data de entrega.

(As entregas E1 e E2 serão avaliadas conjuntamente e valerão 2,0 pontos da nota final do projeto.)

## Datas Importantes

* 27/06 (11:59) - Data limite para pull request do repositório do projeto (será considerada a última versão até essa data e horário).
* 27/06 (14:00) - Apresentação de grupos 
* 28/06 (14:00) - Entrega da avaliação por pares (vide outras informações abaixo).

Presença obrigatória de todos os membros do grupo na data de apresentação. 

## Instruções para a Apresentação

Diretrizes para apresentação (sugestões de tópicos):
* Deve recapitular, de maneira sintética, objetivo inicial do projeto
* Abordagem adotada
* Dificuldades enfrentadas
* Deve relatar possíveis mudanças de percurso
* Referenciais teóricos adotados
* Principais ferramentas utilizadas (incluir informações úteis para que outros possam utilizá-las)
* Resultados obtidos
* Discussão dos resultados
* Conclusões / Lições aprendidas
* Trabalhos futuros

Considerem no máximo 1 slide por minuto. Portanto, um apresentação de 10 minutos não deve ter mais de 10 slides.
## Avaliação

A avaliação do projeto final será realizada não apenas pelos professores da disciplina, mas também passará por etapa de avaliação por pares. Instruções serão fornecidas posteriormente no ambiente Classroom da Disciplina.

# Estrutura do Repositório
A fim de uniformizar os repositórios de projetos da disciplina, os diretórios de seu repositório deverão ser nomeados e utilizados segundo a estrutura sugerida em [Home - Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/), na seção "Directory structure".

Note que nem todos os diretórios ou arquivos serão necessários para todos os projetos. Foque em seguir o padrão para os diretórios que forem necessários. Não crie diretórios que não serão utilizados. Uma breve descrição dessa estrutura, com as pastas mais importantes é dada a seguir.

Seu repositório deverá obrigatoriamente conter o arquivo README.md, arquivo de documentação Markdown, que deverá conter a descrição do projeto conforme orientações a seguir.

~~~
├── README.md          <- apresentação do projeto
│
├── data
│   ├── external       <- dados de terceiros
│   ├── interim        <- dados intermediários, e.g., resultado de transformação
│   ├── processed      <- dados finais usados para a modelagem
│   └── raw            <- dados originais sem modificações
│
├── notebooks          <- Jupyter notebooks ou equivalentes
│
├── src                <- fonte em linguagem de programação ou sistema (e.g., Orange)
│   └── README.md      <- instruções básicas de instalação/execução
│
└── assets             <- mídias usadas no projeto
~~~

Na raiz deve haver um arquivo de nome `README.md` contendo a apresentação do projeto, como detalhado na seção seguinte.

## `data`

Dados utilizados no projeto respeitadas as possíveis implicações éticas, se você tiver licença para tal e se o volume for suportado pelo Github. Você pode optar por colocar um subconjunto ilustrativo dos dados.

Sempre que possível e permitido, é importante que sejam colocados apontadores para os dados originais para garantir a reprodutibilidade do processo. As bases originais devem ser colocadas na subpasta `raw`. Dados intermediários, tais como dados tratados, resumidos, etc. devem ser armazenados na pasta `interim`. Finalmente, coloque os dados finais que serviram de entrada para as suas análises na subpasta `processed`. Caso exista alguma limitação de armazenamento da base no Github, forneça links públicos para acesso aos dados.

## `notebooks`

Código do seu projeto que pode ser executado online sem instalação de software, tal como um notebook em Jupyter ou equivalente.

## `src`

Código em alguma linguagem ou projeto em Orange, Weka e similares.

Se for código em linguagem de programação, tente organizá-lo de forma que seja simples a sua execução por terceiros, por exemplo, acrescente as bibliotecas necessárias etc. Acrescente na raiz um arquivo `README.md` com as instruções básicas de instalação e execução.

## `assets`

Qualquer mídia usada no seu projeto: vídeo, ilustrações, arquivos PDF etc.

Note que nem todos os diretórios ou arquivos serão necessários para todos os projetos. Foque em seguir o padrão para os diretórios que forem necessários. Não crie diretórios que não serão utilizados.

Seu repositório deverá obrigatoriamente conter o arquivo README.md, arquivo de documentação Markdown, que deverá conter a descrição do projeto conforme o template fornecido (ia901-E3-template.md).


