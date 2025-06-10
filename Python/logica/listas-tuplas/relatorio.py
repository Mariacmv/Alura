estoque1 = ('maçã', 'banana')
estoque2 = (1,2)

estoqueFinal = estoque1 + estoque2

print(f'Estoque combinado: {estoqueFinal}')

#OU

estoque1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))
estoque_combinado = estoque1 + estoque2  
print(f"Estoque combinado:\n{estoque_combinado}")