# def filtro(numeros):
#     return numeros % 2 == 0

# numeros = input("Digite os números separados por espaço: ")
# resultado = filter(filtro, numeros)
# int(resultado)
# print(f'Números pares: {resultado}')


numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 