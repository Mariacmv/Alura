# Passo 1: Importar as bibliotecas necessárias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Passo 2: Carregar o dataset Iris
iris = load_iris()
X = iris.data  # Características (comprimento e largura das pétalas e sépalas)
y = iris.target  # Rótulos (espécies das flores)

# Passo 3: Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Passo 4: Treinar o modelo
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Passo 5: Fazer previsões e avaliar o modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {accuracy * 100:.2f}%")