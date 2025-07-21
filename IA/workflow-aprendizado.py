import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Carregar o dataset Iris da biblioteca sklearn
dataset = datasets.load_iris()

# Converter para DataFrame do Pandas para facilitar a manipulação dos dados
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target  # Adicionar a coluna com as classes das flores

# Separar os atributos (X) e os rótulos (y)
X = df.iloc[:, :-1]  # Todas as colunas exceto a última
y = df['target']  # Última coluna, que contém as classes

# Dividir os dados em conjunto de treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar um modelo de Árvore de Decisão
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Fazer previsões nos dados de teste
y_pred = model.predict(X_test)

# Avaliar o desempenho do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy:.2f}')

# Aplicar validação cruzada para melhor avaliação do desempenho
cross_val_scores = cross_val_score(model, X, y, cv=5)
print(f'Acurácia média na validação cruzada: {cross_val_scores.mean():.2f}')

# Testar com uma nova amostra
nova_amostra = np.array([[5.1, 3.5, 1.4, 0.2]])  # Exemplo de medidas de uma flor
predicao = model.predict(nova_amostra)
print(f'Classe prevista para a nova amostra: {dataset.target_names[predicao[0]]}')