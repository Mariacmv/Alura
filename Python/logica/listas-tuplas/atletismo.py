lista = ['Ana', 'João', 'Pedro']

nome_errado = input('Digite o nome errado: ')
if nome_errado in lista:
    posicao = lista.index(nome_errado)

    nome_certo = input('Digite o nome correto: ')
    lista.remove(nome_errado)
    lista.insert(posicao, nome_certo)
    print(lista)
else:
    print('O nome não está na lista')