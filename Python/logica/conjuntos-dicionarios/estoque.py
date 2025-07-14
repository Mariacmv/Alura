
estoque = { 

    "Caderno universitário": 50, 

    "Caneta azul": 120, 

    "Borracha branca": 30 

} 

produto = input("Nome do produto a ser atualizado: ")
quantidade = int(input("Nova quantidade: "))

if produto in estoque:
    estoque[produto] = quantidade
    print("Quantidade atualizada com sucesso!")
    print(estoque)
else:
    print("Produto não encontrado!")

    
    