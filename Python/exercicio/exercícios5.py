#1:
# Crie uma classe chamada Livro com um construtor que aceita os 
# parâmetros titulo, autor e ano_publicacao. Inicie um atributo 
# chamado disponivel como True por padrão.

class Livro:
    livros = [] #crio a lista que armazenará todos os livros criados fora do construtor
    def __init__(self, titulo = '', autor = '', ano_publicacao = 0, disponivel = True):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self.disponivel = disponivel #quando deixo um padrão nos parâmetros e defino aqui na chamada que recebe o parâmetro (recebe o parâmetro?) então pega o valor definido como padrão, certo? (sim)

        Livro.livros.append(self) #adiciono livros à lista criada para armazená-los
#2:
# Na classe Livro, adicione um método especial str que retorna uma 
# mensagem formatada com o título, autor e ano de publicação do livro. 
# Crie duas instâncias da classe Livro e imprima essas instâncias.

    def __str__(self):
        return f'Título: {self._titulo} | Autor: {self._autor} | Ano de publicação do livro: {self._ano_publicacao}'

# livro1 = Livro('É assim que acaba', 'Colleen Hoover', 2016)
# livro2 = Livro('Verity', 'Colleen Hoover', 2020)

# print(livro1,'\n',livro2)

#3:
# Adicione um método de instância chamado emprestar à classe Livro 
# que define o atributo disponivel como False. Crie uma instância da 
# classe, chame o método emprestar e imprima se o livro está 
# disponível ou não.

    def emprestar(self):
        self.disponivel = True
        return f'Disponibilidade: alugado'

# livro3 = Livro('Imperfeitos', 'Christina Lauren', 2022)
# print(livro3)
# print(livro3.emprestar())

#4:
# Adicione um método estático chamado verificar_disponibilidade à 
# classe Livro que recebe um ano como parâmetro e retorna uma lista 
# dos livros disponíveis publicados nesse ano.

    @staticmethod #preciso definir o método como estático
    def verificar_disponibilidade(ano): #método estático não utiliza self e deve ser chamado com a classe
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro.disponivel] #também considera se o livro está disponível ou não, para realmente verificar
        return livros_disponiveis
    
# Livro.livros = [livro1, livro2, livro3] #adicionando livros à lista que armazena livros

#5:
# Crie um arquivo chamado biblioteca.py e importe a classe Livro 
# neste arquivo. (V)

#6:
# No arquivo biblioteca.py, empreste o livro chamando o método 
# emprestar e imprima se o livro está disponível ou não após o 
# empréstimo. (V)

#7:
# No arquivo biblioteca.py, utilize o método estático 
# verificar_disponibilidade para obter a lista de livros disponíveis 
# publicados em um ano específico. (V)

#8:
# Crie um arquivo chamado main.py, importe a classe Livro e, no 
# arquivo main.py, instancie dois objetos da classe Livro e exiba a 
# mensagem formatada utilizando o método str.
