pedidos = input("Digite os pedidos: ").split(', ')

print(f'Pedidos feitos (separados por vírgula): {pedidos}')

pedidos.pop()

print(f'Pedidos finais: {pedidos}')