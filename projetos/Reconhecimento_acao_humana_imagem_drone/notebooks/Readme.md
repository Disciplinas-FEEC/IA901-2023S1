- **Creating labels.ipynb:** adotado para formatar os dados de acordo com a pipeline da Yolov7, isto é, formatação das labels por imagem e organização das pastas;
- **Dados.ipynb:** seleção e filtragem prévia dos dados, retirando as imagens com rótulos diferentes de 'walk','stand','sit' e 'riding', e separando o dataset nos conjuntos de treino, validação e teste;
- **Dados_balanceados.ipynb:** exclusão das imagens com amostras apenas da classe "walk" a fim de balancear o número de amostras de treino entre as classes;
- **DataAugmentation.ipynb:** aplicação de técnicas de *data augmentation* para aumentação dos dados de treino;
- **Inference notebook.ipynb:** inferência do modelo e avaliação dos resultados.
- **Pre_processing.ipynb:** aplica pré-processamentos nas imagens (conversão para níveis de cinza e filtragens no domínio espacial);
- **Testing_metrics:** extrai as métricas do modelo;
- **Training template.ipynb:** treinamento do modelo.

