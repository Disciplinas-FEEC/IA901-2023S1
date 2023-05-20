## Dados originais

Os dados originais adotados no projeto foram adquiridos no Kaggle: <https://www.kaggle.com/datasets/kuantinglai/ntut-4k-drone-photo-dataset-for-human-detection> (base de dados: "NTUT 4K Drone Photo Dataset for Human Detection", com 29 GB). 

Além do acesso aos dados pelo Kaggle, a base de dados encontra-se disponível no drive: <https://drive.google.com/drive/folders/1c-TxV5he38STwtrhZNkPhrAsrB0unwNQ?usp=sharing>.

A base de dados é composta de três pastas: 

- "labels": contém quatro arquivos .csv referentes aos rótulos das imagens de treino, as quais estão subdividas em quatro pastas (cada ".csv" corresponde a um pasta do conjunto de treino);
- "ntut_drone_test": contém uma pasta de mesmo nome ("ntut_drone_test") e, dentro dessa, quatro pastas (Drone_004, Drone_014, Drone_024, Drone_050). Em cada uma dessas quatro pastas, há uma pasta nomeada como "vott-csv-export", na qual encontram-se o arquivo ".csv" correspondente aos rótulos das imagens e as respectivas imagens do conjunto de teste (em ".jpg"):
    
    - "Drone_004" (pasta completa disponível em https://drive.google.com/drive/folders/1yL9y080MCR12vZOQzTUNOSUz_p6B47fD?usp=sharing) possui 507 imagens;
    - "Drone_014" (pasta completa disponível em https://drive.google.com/drive/folders/1W_S_tHORenzmCCC5u0oHQwZqb9vvDrRW?usp=sharing) possui 720 imagens;
    - "Drone_024" (pasta completa disponível em https://drive.google.com/drive/folders/1Jl7Oa9ZrNhQ3e-MOWDCD9GK3ACVidnqE?usp=sharing) possui 287 imagens;
    - "Drone_050" (pasta completa disponível em https://drive.google.com/drive/folders/1BacZCOY9AQ0uk99bMnHrXHhavbg9FDLP?usp=sharing) possui 425 imagens.
    
- "ntut_drone_train": contém uma pasta de mesmo nome ("ntut_drone_train") e, dentro dessa, quatro pastas (Drone_005, Drone_023, Drone_031, Drone_049). Em cada uma dessas quatro pastas, há uma pasta nomeada como "vott-csv-export", na qual encontram-se o arquivo ".csv" correspondente aos rótulos das imagens e as respectivas imagens do conjunto de treino (em ".jpg"):
 
    - "Drone_005" (pasta completa disponível em https://drive.google.com/drive/folders/1b6Rnt7J2nULxquMwQw1CO-nMC7czZC9j?usp=sharing) possui 740 imagens;
    - "Drone_023" (pasta completa disponível em https://drive.google.com/drive/folders/14GcQ6dVoD7fop3bIiDqfY2MkbA-Y9Kmo?usp=sharing) possui 549 imagens;
    - "Drone_031" (pasta completa disponível em https://drive.google.com/drive/folders/1obfzrORKB0iQjdg9ZI7K2R0jPlBJ6BJ0?usp=sharing) possui 485 imagens;
    - "Drone_049" (pasta completa disponível em https://drive.google.com/drive/folders/1EALhILYNHqVygu7mNSEpLosD0w2VXkF1?usp=sharing) possui 382 imagens.

A pasta "Dataset_NTUT_4K_drone" é um subconjunto ilustrativo dos dados originais, em que se pode visualizar a estrutura em que estão armazenados os dados (dentro de cada pasta, mantiveram-se somente 5 imagens para fins de ilustração e o arquivo com os respectivos labels (.csv)).
