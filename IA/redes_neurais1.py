import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Fazer upload da imagem
uploaded = files.upload()
image_path = list(uploaded.keys())[0]

# Carregar a imagem em escala de cinza
imagem = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Mostrar a imagem original e a matriz correspondente
plt.figure(figsize=(10,4))

plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap="gray")
plt.title("Imagem em Tons de Cinza")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(imagem, cmap="gray")
plt.title("Matriz de Pixels")
for i in range(0, imagem.shape[0], 30):
    for j in range(0, imagem.shape[1], 30):
        plt.text(j, i, str(imagem[i, j]), color="red", fontsize=6, ha='center', va='center')

plt.show()