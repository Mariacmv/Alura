atv1 = int(input("Informe os dias para a atividade A: "))
atv2 = int(input("Informe os dias para a atividade B: "))
atv3 = int(input("Informe os dias para a atividade C: "))

if (atv1 == 0 or atv1 % 2 != 0) or (atv2 == 0 or atv2 % 2 != 0) or (atv3 == 0 or atv3 % 2 != 0):
    print('Erro: os dias não podem ser negativos!')
else:
    total = atv1 + atv2 + atv3
    print(f'Total de dias para as atividades: {total}')
