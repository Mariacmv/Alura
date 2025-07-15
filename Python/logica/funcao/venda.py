numeros = input("Digite os valores das vendas: ").split(" ")
soma = 0

for numero in numeros:
    resultado = int(numero)
    soma += resultado

print(f'O total de vendas foi: {soma}')
