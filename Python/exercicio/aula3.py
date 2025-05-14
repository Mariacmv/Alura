#fazer doctring para a função de alternar_estado_restaurante()
import os #para utilizar funções do sistema operacional

#definindo as listas que serão utilizadas ao longo do programa
restaurantes = ['Pizzaria', 'Hamburgueria'] 


def exibir_nome_programa():
    '''Função que exibe o nome estilizado do programa ao executá-lo
    Contém um print com a logo
    '''
    print("""𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤""")

def exibirOpcoes():
    '''Função que exibe na tela opções de funcionalidades ao usuário
    Funcionalidades/Opções:
    - Cadastro de restaurante
    - Listar os restaurantes cadastrados
    - Ativar os restaurantes cadastrados
    - Sair do programa
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

#definindo uma função
def finalizar_app():
    '''Função que exibe o subtitulo de finalizar app através da função exibir_subtitulo
    '''
    exibir_subtitulo('Finalizar app')

def exibir_subtitulo(texto):
    '''Função que exibe o subtítulo em uma página decorrente da funcionalidade de tal tela
    - Limpa a tela
    - Imprime o subtítulo que é passado como parâmetro
    - Pula uma linha
    '''
    os.system('cls') #o comando é : os.system
    print(texto)
    print('\n')
    
def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()
    
def opcao_invalida(): #criando uma função para casos de erro
    print('Opção inválida\n')
    voltar_menu()

def listar_restaurantes():
    '''Função que lista os restaurantes cadastrados
    - Imprime o subtítulo 
    - Percorre a lista de restaurantes cadastrados
    - Imprime cada restaurante cadastrado
    - Volta ao menu através da função volta_menu()
    '''
    exibir_subtitulo('Listando Restaurantes')
    
    for restaurante in restaurantes: #estrutura que percorre a lista 
        print(f'- {restaurante}') #imprimirá cada restaurante
    
    voltar_menu()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante''' #isso é uma docstring, que serve para documentação do código
    '''Inputs:
       -Nome do restaurante
       -Categoria

       Outputs
       -Adiciona um novo restaurante à lista de restaurantes
    ''' 
    #utilizando uma lista para armazenar as informações do resturante
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante) #adiciono a linha. Chamo o nome dela e utilizo a função append que adiciona um elemento ao final da lista e passo como parâmetro o que quero armazenar na lista
    print(f'O restaurante: {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def escolher_opcao():
    '''Função que vai fazer o usuário escolher uma opção do menu
    - Tenta fazer o usuário escolher uma opção
    - Se não consegue, apresenta um erro de entrada
    '''
    try: #para exceções
        opcao_escolhida = int(input('Escolha uma opção: ')) #precisa transformar em inteiro por causa por padrão é string e no if está como int

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app() #utilizando função para facilitar
        else:
            opcao_invalida()
    except: #aqui entra a exceção, oq não entrar no padrão, no esperado
        opcao_invalida()

def main():
    '''Função que organiza e agrupa as outras funções do programa
    - Limpa a tela
    - Chama a função que exibe o nome do programa
    - Chama a função que exibe opções de escolha
    - Chama a função que permite o usuário escolher a opção
    '''
    os.system('cls')
    exibir_nome_programa()
    exibirOpcoes()
    escolher_opcao()

if __name__ == '__main__': #consigo dividir o arquivo em partes para facilitar
    main() #preciso criar uma função principal que contém as outras funções do programa
    

#Loop while
 #É usado quando a qunatidade de iterações é desconhecida
 #Estrutura:
   #while condição:
        #o que será repetido
