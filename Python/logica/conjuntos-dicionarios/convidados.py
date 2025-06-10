convidados = []

adiciona = input("Digite o nome do convidado: ")

while(adiciona != 'sair'):
    adiciona = input("Digite o nome do convidado: ")
    convidados.append(adiciona)
    if adiciona.lower() == 'sair':
        convidados.remove('sair')
print(f'A lista: {convidados}')