from sklearn.cluster import AgglomerativeClustering

# Aplicar Hierarchical Clustering definindo 3 grupos
hc = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
clusters = hc.fit_predict(X_scaled)

# Visualizar os clusters
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.title("Agrupamento com Hierarchical Clustering")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()