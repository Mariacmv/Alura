# #1:
# # Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus
# # atributos.
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro('SUV', 'Preto', 2020)
# #(V)

# #2:
# # Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores 
# # aos seus atributos.
class Restaurante:
    def __init__(self, nome, categoria, ativo, avaliacao, localizacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.avaliacao = avaliacao
        self.localizacao = localizacao

restaurante1 = Restaurante('Sushi Loko', 'Japonês', True, 3, 'Taguatinga Sul')
# #Pequena correção, definir nos parâmetros o que já for fixo, exemplo: ativo=False

# #3:
# # Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie
# # uma instância utilizando o construtor.

# #4:
# # Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e 
# # a categoria. Exiba essa mensagem para uma instância de restaurante.
class Restaurante:
    def __init__(self, nome, categoria, ativo=False, avaliacao, localizacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacao = avaliacao
        self.localizacao = localizacao
    def __str__(self):
        return f'Nome restaurante: {self.nome} Categoria: {self.categoria}'

# #5:
# # Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos 
# # através de um método construtor.
class Cliente:
    def __init__(self, nome, telefone, email, forma_pagamento):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.forma_pagamento = forma_pagamento
        
cliente1 = Cliente('Maria', '6199999999', 'maria@gmail.com', 'dinheiro em espécie')
cliente2 = Cliente('Frederico', '6188888888', 'fred@gmail.com', 'cheque')
cliente3 = Cliente('Magda', '61555555555', 'magda@gmail.com', 'cartão de débito')
# #Para passar parâmetros padrão só define aspas para string e 0 para números quando quero deixar o código mais flexível 

class Pessoa:
    def __init__(self, nome = '', idade = 0, profissao = ''): #quando inicio um atributo com '' quer dizer que receberá uma string
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return(f'{self.nome}, {self.idade}, {self.profissao}')
    
    def aniversario(self):
        print('Após fazer aniversário')
        self.idade += 1
        
    @property
    def saudacao(self): #por que utilizar porperty? Não entendi muito bem
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}'
        else:
            return f'Olá, sou {self.nome}!'
        
pessoa1 = Pessoa(nome = 'Maria', idade = 20, profissao = 'Estudante')
print(pessoa1.saudacao)
print(pessoa1)
pessoa1.aniversario()
print(pessoa1)
