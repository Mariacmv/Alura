lista1 = input("Ana, digite a lista: ").lower().split()
lista2 = input("Laura, digite a lista: ").lower().split()

LISTA1 = set(lista1)
LISTA2 = set(lista2)

print(f"\nLista de Ana: {LISTA1}")
print(f'Lista de Laura: {LISTA2}\n')
''
print(f'Itens em ambas as listas: {LISTA1.intersection(LISTA2)}\n')

print(f'Itens exclusivos de Laura: {LISTA2.difference(LISTA1)}\n')
print(f'Itens exclusivos de Ana: {LISTA1.difference(LISTA2)}')
