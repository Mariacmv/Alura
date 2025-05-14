# 1 - Solicite ao usuário que insira um número e, em seguida, use uma
# estrutura if else para determinar se o número é par ou ímpar.

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma 
# estrutura if elif else para classificar a idade em categorias de 
# acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.
# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if
# else para verificar se o nome de usuário e a senha fornecidos 
# correspondem aos valores esperados determinados por você.

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer
# e utilize uma estrutura if elif else para determinar em qual 
# quadrante do plano cartesiano o ponto se encontra de acordo com as
# seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.


# 1:
numero = int(input('Digite um número: '))
numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('O número {} é par'.format(numero))
elif numero % 2 != 0:
    print('O número {} é ímpar' .format(numero))
else:
    print('Opção inválida')

# 2:
idade = int(input('Digite sua idade: '))
idade = int(input('Digite sua idade: '))

if 0 <= idade <= 12:
    print('Você é uma criança')
elif 13 <= idade <= 18:
    print('Você é um adolescente')
elif idade > 18:
    print('Você é um adulto')
else: 
    print('Opção inválida')

# 3:
nome = input('Digite seu nome: ')
senha = input('Digite uma senha: ')
nome = input('Digite seu nome: ')
senha = input('Digite uma senha: ')

if (nome == 'Maria Clara' or nome == 'Maria') and (senha == 'monal'): #para cada condição é necessário comparar com a variável diretamente

    print('Bem vindo(a) {}'.format(nome))
else: 
    print('Acesso negado')

# 4:
x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))

if (x > 0) and (y > 0):
    print('O ponto está no primeiro quadrante')
elif (x < 0) and (y > 0):
    print('O ponto está no segundo quadrante')
elif (x < 0) and (y < 0):
    print('O ponto está no terceiro quadrante')
elif (x > 0) and (y < 0):
    print('O ponto está no quarto quadrante')
else:
    print('O ponto está no eixo ou origem')
