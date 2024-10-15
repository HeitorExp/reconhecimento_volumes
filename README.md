# Projeto de Classificação de Imagens com SciKit-Learn

#### *Este projeto tem como objetivo classificar imagens de caixas de frutas, distinguindo entre as categorias "vazio" e "cheio".*

---

### **Objetivos**

- Classificar as caixas de frutas em dois grupos: "vazio" e "cheio" utilizando aprendizado de máquina.
- Explorar e utilizar bibliotecas da linguagem Python aplicadas a projetos de visão computacional.

---

### **Bibliotecas Utilizadas**

#### **1. OS**
- A biblioteca **OS** foi utilizada para organizar e manipular os arquivos nos diretórios adequados.

#### **2. skimage.io (imread)**
- **imread** da biblioteca `skimage.io` foi usada para carregar as imagens a partir de arquivos.

#### **3. skimage.transform (resize)**
- **resize** foi utilizada para redimensionar as imagens para um tamanho padronizado de 64x64 pixels.

#### **4. numpy**
- A biblioteca **numpy** foi utilizada para manipulação e criação de arrays com os dados das imagens, permitindo o processamento eficiente.

#### **5. sklearn.model_selection (train_test_split)**
- **train_test_split** foi utilizada para dividir o conjunto de dados em treinamento e teste de maneira aleatória e estratificada, garantindo que ambos os conjuntos representem proporcionalmente as categorias.

#### **6. sklearn.model_selection (GridSearchCV)**
- **GridSearchCV** foi utilizada para realizar a busca pelos melhores hiperparâmetros do modelo de Suporte a Vetores (SVM), testando diversas combinações de parâmetros.

#### **7. sklearn.svm (SVC)**
- **SVC** foi utilizado para implementar as Máquinas de Vetores de Suporte (SVM) como o classificador principal do projeto.

#### **8. sklearn.metrics (accuracy_score)**
- **accuracy_score** foi utilizada para avaliar a precisão do modelo com base nas previsões feitas no conjunto de teste.

#### **9. sklearn.metrics (classification_report e confusion_matrix)**
- **classification_report** foi utilizada para gerar um relatório detalhado de desempenho do classificador em termos de precisão, recall e F1-score.
- **confusion_matrix** foi utilizada para calcular e visualizar a matriz de confusão do classificador.

#### **10. seaborn**
- A biblioteca **seaborn** foi utilizada para a visualização da matriz de confusão, com o objetivo de facilitar a interpretação dos resultados do classificador.

#### **11. pandas**
- A biblioteca **pandas** foi utilizada para salvar o relatório de classificação em um formato tabular (CSV).

#### **12. pickle**
- **pickle** foi utilizada para salvar o modelo treinado em um arquivo para uso futuro, permitindo a reutilização do classificador sem a necessidade de treinar novamente.

---

### **Organização do Projeto**

- **dados/**: Pasta que contém as subpastas de imagens "vazio" e "cheio", com as imagens que serão utilizadas no projeto.
- **resultados/**: Pasta onde serão salvos os resultados do modelo, incluindo o classificador treinado (`model.p`), a matriz de confusão (`matriz_confusao.png`), e o relatório de classificação (`relatorio_classificacao.csv`).

---

### **Execução do Projeto**

1. Coloque as imagens nas respectivas pastas dentro de `dados/`, separando as imagens de caixas vazias na subpasta "vazio" e as de caixas cheias na subpasta "cheio".
2. Execute o script de classificação, que realizará as seguintes etapas:
   - Carregar e processar as imagens.
   - Dividir o conjunto de dados em treino e teste.
   - Treinar um modelo SVM com ajuste de hiperparâmetros via `GridSearchCV`.
   - Avaliar o modelo e gerar a matriz de confusão e o relatório de classificação.
3. Os resultados serão salvos na pasta `resultados/` para posterior análise.

---

### **Instruções Finais**

- Certifique-se de que a estrutura do diretório esteja correta antes de rodar o código.
- O modelo gerado pode ser reutilizado posteriormente, carregando o arquivo `model.p` da pasta `resultados/`.
- Todos os resultados relevantes (matriz de confusão e relatório de classificação) estarão disponíveis para consulta e uso na pasta `resultados/`.

---

### **Observações Finais**

Este projeto é uma demonstração de uso de técnicas básicas de classificação de imagens com SciKit-Learn, aplicando SVM e explorando bibliotecas fundamentais para visão computacional. Para melhores resultados, recomenda-se a futura utilização de redes neurais convolucionais (CNNs) em projetos maiores e mais complexos.

