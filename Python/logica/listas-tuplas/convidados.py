lista_atual = ['Ana', 'Pedro', 'Carlos']

print(f'Lista atual: {lista_atual}')
novo_nome = input('Digite o nome do novo convidado:')
posicao = int(input('Digite a posição na qual deseja inserir o convidado: '))
lista_atual.insert(posicao-1, novo_nome)

print(f'Lista atual: {lista_atual}')

