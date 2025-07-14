produtos = {}

contador = 1
while contador < 4:
    nome = input("Digite o nome do produto: ")
    quant = int(input("Digite a quantidade: "))
    produtos[nome] = quant    
    contador += 1
    
print(f'Dicionário de produtos: {produtos}')
    

