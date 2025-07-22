from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Criar um modelo CNN simples
modelo = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(64, 64, 3)),  # Camada convolucional
    MaxPooling2D(pool_size=(2,2)),  # Camada de pooling
    Flatten(),  # Achatar para camada densa
    Dense(128, activation='relu'),  # Camada totalmente conectada
    Dense(3, activation='softmax')  # Saída para 3 classes
])

modelo.summary()  # Exibe a arquitetura da rede