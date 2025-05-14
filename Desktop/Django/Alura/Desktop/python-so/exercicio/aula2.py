import os #para utilizar funções do sistema operacional

#definindo as listas que serão utilizadas ao longo do programa
restaurantes = [] 


#definindo as listas que serão utilizadas ao longo do programa
restaurantes = [] 


def exibir_nome_programa():
    print("""𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤""")

def exibirOpcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

#definindo uma função
def finalizar_app():
    os.system('cls') #o comando é: os.system
    print('Finalizando o app\n')

def opcao_invalida(): #criando uma função para casos de erro
    print('Opção inválida\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    #utilizando uma lista para armazenar as informações do resturante
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante) #adiciono a linha. Chamo o nome dela e utilizo a função append que adiciona um elemento ao final da lista e passo como parâmetro o que quero armazenar na lista
    print(f'O restaurante: {nome_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida(): #criando uma função para casos de erro
    print('Opção inválida\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    #utilizando uma lista para armazenar as informações do resturante
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante) #adiciono a linha. Chamo o nome dela e utilizo a função append que adiciona um elemento ao final da lista e passo como parâmetro o que quero armazenar na lista
    print(f'O restaurante: {nome_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try: #para exceções
        opcao_escolhida = int(input('Escolha uma opção: ')) #precisa transformar em inteiro por causa por padrão é string e no if está como int
    try: #para exceções
        opcao_escolhida = int(input('Escolha uma opção: ')) #precisa transformar em inteiro por causa por padrão é string e no if está como int

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app() #utilizando função para facilitar
        else:
            opcao_invalida()
    except: #aqui entra a exceção, oq não entrar no padrão, no esperado
        opcao_invalida()
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app() #utilizando função para facilitar
        else:
            opcao_invalida()
    except: #aqui entra a exceção, oq não entrar no padrão, no esperado
        opcao_invalida()

def main():
    os.system('cls')
    os.system('cls')
    exibir_nome_programa()
    exibirOpcoes()
    escolher_opcao()

if __name__ == '__main__': #consigo dividir o arquivo em partes para facilitar
    main() #preciso criar uma função principal que contém as outras funções do programa
    


#Para versatilizar ainda mais e tornar o código menos complexo, existe
#a função match() que é basicamente um switch
#Estrutura do match():
# match expressao:
#     case padrao_1:
#         código a ser executado
#     case padrao_2:
#         código a ser executado
#     case _:
#         código a ser executado caso os outros padrões não forem atendidos

#TUPLAS X LISTAS
# Listas são definidas através de colchetes 
    # Exemplo: lista = [1,2,3]
# Tuplas são definidas através de parênteses
    # Exemplo: tupla = (1,2,3)
#Listas são mutáveis podendo utilizar funções como: append(), remove(), pop() e insert()
#Já tuplas são imutáveis
#Sobre o uso de cada uma: listas são ideais para atividades que serão modificadas ao longo do tempo
    # Exemplo:
    # Criando uma lista de compras
        # lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

        # # Adicionando um item à lista
        # lista_de_compras.append("Ovos")

        # # Removendo um item da lista
        # lista_de_compras.remove("Banana")

        # # Exibindo a lista
        # print("Lista de Compras:")
        # for item in lista_de_compras:
        #     print("- " + item)
#Tuplas são ideais para constantes, para informações que permanecem as mesmas ao longo do tempo
    # Exemplo:
    # Definindo uma tupla de coordenadas geográficas
        # coordenadas_gps = (40.7128, -74.0060)

        # # Exibindo as coordenadas
        # print("Coordenadas GPS:")
        # print("Latitude:", coordenadas_gps[0])
        # print("Longitude:", coordenadas_gps[1])
        
        
#VER MAIS EM:
#https://www.alura.com.br/artigos/conhecendo-as-tuplas-no-python
#E:
#https://docs.python.org/pt-br/3/tutorial/datastructures.html#tuples-and-sequences
