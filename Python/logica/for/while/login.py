nome = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

while len(nome) < 5 or len(senha) < 8:
    if len(nome) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres.')
    if len(senha) < 8:
        print('A senha deve ter pelo menos 8 caracteres.')
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    
print('Cadastro realizado com sucesso!')