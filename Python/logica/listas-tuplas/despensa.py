despensa = ['maçã']

item = input("Digite o item que você quer verificar: ")

if item in despensa:
    print(f'O item {item} está na despensa.')
else:
    print(f'O item {item} precisa ser comprado!')