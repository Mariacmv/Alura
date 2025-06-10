despesas = float(input("Digite o total de despesas do mês (R$): "))

if despesas > 3000:
    print("Atenção! Você ultrapassou o limite do orçamento.")
else:
    print("Você está dentro do limite do orçamento.")