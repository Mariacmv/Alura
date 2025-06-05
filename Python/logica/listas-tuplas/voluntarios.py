nomes = []

while True:
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
    if nome == 'sair':
        break
    nomes.append(nome)
    
print(f'Voluntários: {nomes}')
