#5:
# Crie um arquivo chamado biblioteca.py e importe a classe Livro 
# neste arquivo.
from exercícios5 import Livro

#6:
# No arquivo biblioteca.py, empreste o livro chamando o método 
# emprestar e imprima se o livro está disponível ou não após o 
# empréstimo.
livro1 = Livro('É assim que acaba', 'Colleen Hoover', 2016)
livro2 = Livro('Verity', 'Colleen Hoover', 2020)
livro3 = Livro('Imperfeitos', 'Christina Lauren', 2022)

Livro.livros = [livro1, livro2, livro3]

livro1.emprestar()
#print(livro1.emprestar())

#7:
# No arquivo biblioteca.py, utilize o método estático 
# verificar_disponibilidade para obter a lista de livros disponíveis 
# publicados em um ano específico.
livros_disponiveis_2020 = Livro.verificar_disponibilidade(2020) #armazeno a informação que retorna uma lista

for livro in livros_disponiveis_2020:
    print(livro)
