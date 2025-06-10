macas = int(input("Digite a quantidade de maçãs vendidas: "))
bananas = int(input("Digite a quantidade de bananas vendidas: "))

if macas > bananas:
    print("As maçãs tiveram mais vendas")
elif bananas > macas:
    print("As bananas tiveram mais vendas")
elif macas == bananas:
    print("Empate")