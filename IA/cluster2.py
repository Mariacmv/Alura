from sklearn.datasets import load_iris
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Carregar o dataset Iris
iris = load_iris()
X = iris.data

# Normalizar os dados para melhorar a performance do clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Criar o dendrograma
plt.figure(figsize=(10, 5))
sch.dendrogram(sch.linkage(X_scaled, method='ward'))
plt.title("Dendrograma do Agrupamento Hierárquico")
plt.xlabel("Amostras")
plt.ylabel("Distância Euclidiana")
plt.show()