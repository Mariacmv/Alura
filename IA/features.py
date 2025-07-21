from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor

# Carregar dataset
X, y = fetch_california_housing(return_X_y=True)

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Definir hiperparâmetros para otimização
param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

#max_depth -> profundidade máxima da árvore de decisão
#'min_samples_split' -> nº mínimo de amostras para dividir um nó
#'min_samples_leaf' -> nº mínimo de amostras por folha

# Aplicar GridSearch para encontrar os melhores hiperparâmetros
grid_search = GridSearchCV(DecisionTreeRegressor(), param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)

#GridSearch -> realiza buscas combinando todos os valores de hiperparâmetros
# Métrica de avaliação -> erro quadrático médio negativo

print(f"Melhores parâmetros: {grid_search.best_params_}")