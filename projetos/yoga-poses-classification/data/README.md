# Instruções

Esta pasta contém 10 imagens de exemplos em cada um conjunto de dados.
Para ter acesso a todas as amostras para executar os notebooks, é necessário acessar a seguinte página no Google Drive: https://drive.google.com/drive/folders/1pdxEsoIo1RZMyLKJ9xRbV57lykxoIslV?usp=sharing

Após acessar o link, é necessário adicionar um atalho dessa pasta ao "Meu Drive", conforme mostrado abaixo:

![add_driver_1](../assets/add_folder_driver_1.png)

![add_driver_2](../assets/add_folder_driver_2.png)


# Organização da pasta
A pasta "data" é organizada da seguinte forma:

~~~
├── data
    ├── processed      <- dados finais processados (saída do notebook data_augmentation_train.ipynb)
    ├── interim        <- dados intermediários
        ├── filtered   <- dados filtrados (saída do notebook pre-processing.ipynb)
        ├── normalized <- dados normalizados (saída do notebook normalizing.ipynb)
        └── balanced   <- dados com classes balanceadas (saída do notebook class_balacing.ipynb)
    ├── raw            <- dados originais sem modificações
    └── README.md      <- instruções da pasta
~~~