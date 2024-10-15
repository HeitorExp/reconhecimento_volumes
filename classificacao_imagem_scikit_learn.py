import os
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from skimage.io import imread
from skimage.transform import resize

# Preparação dos dados
input_dir = 'dados'
categorias = ['vazio', 'cheio']

data = []
labels = []

# Pré-processamento das imagens
for categoria_idx, categoria in enumerate(categorias):
    categoria_path = os.path.join(input_dir, categoria)
    
    if not os.path.exists(categoria_path):
        raise ValueError(f"Diretório {categoria_path} não encontrado!")
    
    for file in os.listdir(categoria_path):
        caminho_imagem = os.path.join(input_dir, categoria, file)
        imagem = imread(caminho_imagem)
        imagem = resize(imagem, (64, 64)) / 255.0
        data.append(imagem.flatten())
        labels.append(categoria_idx)

data = np.asarray(data)
labels = np.asarray(labels)

# Separação dos dados em treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(
    data, labels, test_size=0.2, shuffle=True, stratify=labels, random_state=42
)

# Treinamento do classificador
classificador = SVC()
parametros = [{'gamma': [0.01, 0.001, 0.0001], 'C': [1, 10, 100, 1000]}]

grid_search = GridSearchCV(classificador, parametros, cv=5)
grid_search.fit(x_treino, y_treino)

# Avaliação do melhor estimador
melhor_estimador = grid_search.best_estimator_
previsao_y = melhor_estimador.predict(x_teste)

pontuacao = accuracy_score(previsao_y, y_teste)
print(f'{pontuacao * 100:.2f}% das imagens foram classificadas corretamente.')

# Relatório de Classificação e Matriz de Confusão
relatorio_classificacao = classification_report(y_teste, previsao_y, target_names=categorias, output_dict=True)
matriz_confusao = confusion_matrix(y_teste, previsao_y)

# Criar pasta 'resultado' se não existir
output_dir = 'resultado'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Salvar o modelo treinado
pickle.dump(melhor_estimador, open(os.path.join(output_dir, 'model.p'), 'wb'))

# Plotar e salvar a matriz de confusão como imagem
plt.figure(figsize=(6, 4))
sns.heatmap(matriz_confusao, annot=True, fmt="d", cmap='Blues', xticklabels=categorias, yticklabels=categorias)
plt.title('Matriz de Confusão')
plt.xlabel('Classe Predita')
plt.ylabel('Classe Verdadeira')
plt.savefig(os.path.join(output_dir, 'matriz_confusao.png'))  # Salvar o plot da matriz de confusão
plt.close()  # Fechar a figura para evitar sobreposição de plots futuros

# Salvar o relatório de classificação como CSV
df_relatorio = pd.DataFrame(relatorio_classificacao).transpose()
df_relatorio.to_csv(os.path.join(output_dir, 'relatorio_classificacao.csv'), index=True)

print("Modelo, matriz de confusão e relatório de classificação salvos na pasta 'resultados'.")
