#1:
# Crie uma classe chamada ContaBancaria com um construtor que aceita
# os parâmetros titular e saldo. Inicie o atributo ativo como False 
# por padrão.

class ContaBancaria:
    def __init__(self, titular='', saldo=0, ativo=False):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo #se passar um valor padrão nos parâmetros então não é necessário passar na inicialização

#2:
# Na classe ContaBancaria, adicione um método especial __str__ que 
# retorna uma mensagem formatada com o titular e o saldo da conta. 
# Crie duas instâncias da classe e imprima essas instâncias.

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: {self.saldo}'
    
# conta1 = ContaBancaria(titular = 'Maria', saldo = 3000) #não precisa passar o nome dos atributos
# print(conta1)
# conta2 = ContaBancaria(titular = 'Magda', saldo = 10000)
# print(conta2)

#3:
# Adicione um método de classe chamado ativar_conta à classe 
# ContaBancaria que define o atributo ativo como True. Crie uma 
# instância da classe, chame o método de classe e imprima o valor de 
# ativo.

    @classmethod
    def ativar_conta(cls):
        ativo = True
        if ativo == True:
            print('Conta ativa')
        else:
            print('Conta inativa')
        print(ativo)
conta1 = ContaBancaria()
conta1.ativar_conta()

#4:
# Refatore a classe ContaBancaria para utilizar a abordagem 
# "pythonica" na criação de atributos. Utilize propriedades, se 
# necessário. (EU NÃO SOUBE FAZER) (O QUE SIGNIFICA?)

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo

#5:
# Crie uma instância da classe e imprima o valor da propriedade 
# titular.
conta2 = ContaBancaria('Maria', 10000)
print(conta2.__str__()) #ou poderia fazer o print do zero como: print(f'Titular: {conta2.titular}')

#6:
# Crie uma classe chamada ClienteBanco com um construtor que aceita 5
# atributos. Instancie 3 objetos desta classe e atribua valores aos 
# seus atributos através do método construtor.

class ClienteBanco:
    saldo_total = 0 #atributo da classe
    def __init__(self, nome='', cpf='', saldo=0):
        self.nome = ''
        self.cpf = ''
        self.saldo = saldo
        
# cliente1 = ClienteBanco('Maria', '07444324131')
# cliente2 = ClienteBanco('Clara', '555555555')

#7:
# Crie um método de classe para a conta ClienteBanco.

    @classmethod
    def adicionar_saldo(cls, valor):
        cls.saldo_total += valor
        return cls.saldo_total
    
    def __str__(self):
        return f'Titular: {self.nome} | CPF: {self.cpf} | Saldo: {self.saldo}'

cliente3 = ContaBancaria('Mona', '333333333', 10000)
ClienteBanco.adicionar_saldo(10000)
print(f'{cliente3}')
print(f'Saldo total: {ClienteBanco.saldo_total}')
