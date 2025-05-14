# Exercício 1:
# Crie uma classe Pessoa que tenha um atributo privado _idade. A 
# classe deve ter um método @property para obter o valor da idade e 
# um método @idade.setter para alterar a idade. Implemente o método
# __str__ para imprimir a idade da pessoa.

# class Pessoa:
#     idade = 0
#     def __init__(self, idade):
#         self._idade = idade
        
#     @property #para que funcione completamente é necessário tornar os atributos utilizados privados
#     def obter_idade(self):
#         return self._idade #acessa o valor de forma controlada
    
#     @obter_idade.setter #para alterar o valor do property
#     def altera_idade(self, idade_alterada):
#         self._idade = idade_alterada
    
#     def __str__(self): #não precisa passar outros atributos
#         return f'A idade da pessoa é: {self._idade}' #acessa o atributo privado
    
# pessoa1 = Pessoa(20)
# pessoa1.obter_idade = 25
# print(pessoa1.obter_idade)

# Exercício 2:
# Crie uma classe Carro com os seguintes atributos: modelo e ano. 
# Crie um método de classe @classmethod chamado criar_carro_ano_atual
# que cria um carro com o modelo passado como parâmetro e o ano igual
# ao ano atual. Imprima as informações do carro criado.

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def criar_carro_ano_atual(cls, modelo, ano=2025):
        cls.modelo = modelo
        cls.ano = ano
        
    def __str__(self):
        return f'Modelo do carro: {self.modelo}'
    
carro1 = Carro('SUV', 2025)
print(carro1)

# Exercício 3:
# Crie uma classe Livro com os atributos titulo e autor. Adicione um
# atributo de classe #quantidade_livros que armazena a quantidade 
# total de livros criados. Cada vez que um novo livro for criado, o 
# valor desse atributo de classe deve ser incrementado. Crie um 
# método de classe para obter o total de livros criados e um método 
# de instância que retorna o título e autor do livro.

# Exercício 4:
# Crie uma classe ContaBancaria com os atributos titular e saldo. 
# Crie um método de instância chamado depositar para adicionar um 
# valor ao saldo. Além disso, crie um método @property que retorna 
# uma descrição do saldo como um valor formatado (ex: "R$ 1000,00").
# O saldo deve ser armazenado como um atributo privado. Implemente 
# também um método __str__ para mostrar o titular e o saldo.

# Exercício 5:
# Crie uma classe Produto com o atributo preco. Crie um método 
# @property chamado preco_com_desconto, que aplica um desconto de 10%
# ao preço e retorna o valor com desconto. Crie um método @preco_com_
# desconto.setter que permita alterar o valor do desconto 
# (em porcentagem).
