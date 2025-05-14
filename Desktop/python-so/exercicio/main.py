#8:
# Crie um arquivo chamado main.py, importe a classe Livro e, no 
# arquivo main.py, instancie dois objetos da classe Livro e exiba a 
# mensagem formatada utilizando o método str.
from exercícios5 import Livro

livro_novo = Livro('O Hobbit', 'J.R.R.Tolkien', 2019)
livro_novo2 = Livro('A gata viu a morte', 'Dolores Mitchens', 2023)

print(livro_novo) #não chama o __str__ porque ele serve apenas para formatar
print(livro_novo2)
