# IA901 - Projeto - Segunsa Entrega (E2)

## Instruções Gerais

O objetivo do projeto final desta disciplina é fazer com que os alunos tentem resolver um problema real utilizando as técnicas discutidas ao longo da disciplina, tanto de processamento de imagens quanto de reconhecimento de padrões.

Para fazer esta entrega pelo github, siga as seguintes instruções atentamente:
 * Garanta que cada membro da equipe tenha uma conta github (serão monitoradas as contribuições de cada membro).
 * Faça fork deste repositório.
 * No seu fork, dentro da pasta de `projetos`, *crie uma nova pasta* com o *nome do seu projeto*.
 * Faça o commit dos arquivos associados a esta entrega, conforme descrito a seguir.
 * Quando tudo estiver pronto para entrega, crie uma tag de release no repositório identificada como `IA901_E2`.
 * Até a data de submissão estabelecida, crie um pull request para este repositório.



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

## `README.md`

Para a entrega E2, o README.md do repositório deve ser formatado [segundo o modelo disponibilizado neste link](https://github.com/Disciplinas-FEEC/ia901-2023S1/blob/main/templates/ia901-E2-template.md).

Caso não tenha experiência com edição em Markdown, vide referência: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).
Existem também múltiplas ferramentas para edição de Markdown como, por exemplo, [StackEdit](https://stackedit.io/).

## `data`

Dados utilizados no projeto respeitadas as possíveis implicações éticas, se você tiver licença para tal e se o volume for suportado pelo Github. Você pode optar por colocar um subconjunto ilustrativo dos dados.

É importante que sejam colocados os dados originais (se for possível) para garantir a reprodutibilidade do processo. Os originais são colocados na subpasta `raw` se forem produzidos pela equipe e na subpasta `external` se forem de terceiros. Também podem ser colocados aqui dados intermediários (por exemplo, dados tratados, resumidos etc.) na pasta `interim`. Finalmente, coloque os dados finais que serviram de entrada para as suas análises na subpasta `processed`.

## `notebooks`

Código do seu projeto que pode ser executado online sem instalação de software, tal como um notebook em Jupyter ou equivalente.

## `src`

Código em alguma linguagem ou projeto em Orange, Weka e similares.

Se for código em linguagem de programação, tente organizá-lo de forma que seja simples a sua execução por terceiros, por exemplo, acrescente as bibliotecas necessárias etc. Acrescente na raiz um arquivo `README.md` com as instruções básicas de instalação e execução.

## `assets`

Qualquer mídia usada no seu projeto: vídeo, ilustrações, arquivos PDF etc.

Note que nem todos os diretórios ou arquivos serão necessários para todos os projetos. Foque em seguir o padrão para os diretórios que forem necessários. Não crie diretórios que não serão utilizados.

Seu repositório deverá obrigatoriamente conter o arquivo README.md, arquivo de documentação Markdown, que deverá conter a descrição do projeto conforme orientações a seguir.


> Tudo o que aparecer neste modo de citação se refere a algo que deve ser substituído pelo indicado. 