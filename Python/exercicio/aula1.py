print("""𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤""") #aspas triplas servem para escrever várias linhas sem precisar de \n

# #Exemplo: print("""Olá
# Eu quero jogar
# Monal""")

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n') #print exibe informação

opcao_escolhida = input('Escolha uma opção: ') #pede uma entrada do usuário e precisa armazenar numa variável para salvar a escolha
# print('Você escolheu a opção', opcao_escolhida)

#formatação f string: interpolar a variável com uma string
print(f'Você escolheu a opção: {opcao_escolhida}')
