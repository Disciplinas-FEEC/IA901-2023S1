### Dados finais usados para a modelagem

Quatro conjunto de dados foram adotados na modelagem:
- Imagens RGB (pasta "Dados_filtrados"), filtradas do conjunto original do dataset "NTUT 4K Drone Photo Dataset for Human Detection". Conjunto completo disponível em: https://drive.google.com/drive/folders/1whsJovK-29ZBCNZhqMQ-Ihot55qsegCe?usp=sharing;
- Imagens em níveis de cinza (definidas após a filtragem dos dados originais em função dos labels "walk", "riding", "sit" e "stand"). Conjunto completo disponível em: <https://drive.google.com/drive/folders/1-0ampfZunDklLZBQg2RVy9EQ9BAnzFJ7?usp=share_link>;
- Imagens resultantes da filtragem espacial adotando o Filtro de Sobel (definidas após a filtragem dos dados originais em função dos labels "walk", "riding", "sit" e "stand"). Conjunto completo disponível em: <https://drive.google.com/drive/folders/1tNVJLCYaUojwDgW0lghAYnrlVFRyueSj?usp=sharing>;
- Imagens resultantes da filtragem espacial adotando o Filtro de Prewitt (definidas após a filtragem dos dados originais em função dos labels "walk", "riding", "sit" e "stand"). Conjunto completo disponível em: <https://drive.google.com/drive/folders/1t1M_E_MC0-GXDTVXmc7rqrvA84rdOYvX?usp=sharing>.

A estrutura em que os arquivos são salvos é ilustrada nas pastas anexas. Em cada uma das pastas de dados ("NC", "Filtro_Sobel" e "Filtro_Prewitt"), há três pastas:
- Teste: contém uma pasta com as imagens do conjunto de Teste ("images") e o arquivo "label_test.txt";
- train: contém uma pasta com as imagens do conjunto de treino ("images"), uma pasta com os arquivos de texto correspondentes aos labels individualizados de cada imagem ("labels") e o arquivo "label_train.txt"; 
- val: contém uma pasta com as imagens do conjunto de validação ("images"), uma pasta com os arquivos de texto correspondentes aos labels individualizados de cada imagem ("labels") e o arquivo "label_val.txt".

Aqui são inseridos somente 5 imagens e 5 arquivos de rótulos em cada pasta, para fins de ilustração dos dados adotados na modelagem do projeto.

**Nota:** além dos três conjuntos ilustrados pelas pastas anexas, há também o conjunto de imagens RBG (pasta "Dados_filtrados", incluída na pasta "/data/interim/", por ter sido um dado intermediário para geração dos demais dados finais apresentados nesse sub-item). Ressalta-se que as imagens RGB - filtradas dos dados originais - também compõe um conjunto adotado para a modelagem final. 
