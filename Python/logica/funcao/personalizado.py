def gerador(porcentagem, compra):
    desconto = (compra / 100) * porcentagem
    resultado = compra - desconto
    print(f'Preço final com desconto: {resultado}')
    
porcentagem = float(input("Digite a porcentagem de desconto: "))
compra = float(input("Digite o valor da compra: "))

gerador(porcentagem, compra)

