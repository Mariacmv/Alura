contagem = [10,9,8,7,6,5,4,3,2,1]

for item in contagem:
    if item % 2 == 0:
        print(f'Faltam apenas {item} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {item} segundos restantes.')
print('Aproveite a promoção agora!')
