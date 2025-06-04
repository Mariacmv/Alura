renda_mensal = float(input("Digite o valor da sua renda mensal: "))
parcela = float(input("Digite o valor da parcela desejada: "))

if (renda_mensal > 2000) and (parcela < (0.3*renda_mensal)):
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado: parcela acima de 30% da renda")