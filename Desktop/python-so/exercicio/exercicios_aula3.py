# projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

# for projeto in projetos:
#     try:
#         print(f"Projeto: {projeto}")
#     except TypeError:
#         print("Projeto não disponível")


# 1:
# Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = ['Maria', 'Clara', 'Monalisa', 'Rita']
lista3 = [2004, 2025]

# 2:
# Crie uma lista e utilize um loop for para percorrer todos os
# elementos da lista.

lista_nova = [1,2,3,4,5,6]
for i in lista_nova:
    print(i)

# 3:
# Utilize um loop for para calcular a soma dos números ímpares de
# 1 a 10.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for i in lista:
    if i % 2 != 0:
        soma += i

print(soma)

# 4:
# Utilize um loop for para imprimir os números de 1 a 10 em
# ordem decrescente.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10, 0, -1):
    print(i)

# 5:
# Solicite ao usuário um número e, em seguida, utilize um loop 
# for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input('Digite um número: '))
mult = 1

for i in range(1, 11):
    mult = numero * i
    print(mult)

# 6:
# Crie uma lista de números e utilize um loop for para calcular 
# a soma de todos os elementos. Utilize um bloco try-except para 
# lidar com possíveis exceções.
lista = [1,2,3,4,5,6,7,8,9,10]
soma = 0

try:
    for i in lista:
        soma += i
    print(soma)
except Exception as e:
    print(f'Erro ao calcular a soma: {e}')

# 7:
# Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, 
# caso a lista esteja vazia.
lista = [1,2,3,4,5,6]
media = 0

try:
    for i in lista:
        media += i
    media = media/len(lista)
    print(media)
except ZeroDivisionError:
    print('Não é possível dividir por 0, a lista está vazia')
except Exception as e:
    print('erro ao calcular a média')
