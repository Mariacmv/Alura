# Passo 1: Importar as bibliotecas necessárias
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import pandas as pd

# Passo 2: Carregar e preparar o dataset Iris
dataset = load_iris()
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df['species'] = dataset.target

# Passo 3: Normalizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop(columns=['species']))

# Passo 4: Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, df['species'], test_size=0.3, random_state=42)

# Passo 5: Treinar e avaliar a Árvore de Decisão
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)
tree_accuracy = accuracy_score(y_test, tree_model.predict(X_test))
print(f"Acurácia da Árvore de Decisão: {tree_accuracy * 100:.2f}%")

# Passo 6: Treinar e avaliar o KNN
knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)
knn_accuracy = accuracy_score(y_test, knn_model.predict(X_test))
print(f"Acurácia do KNN: {knn_accuracy * 100:.2f}%")