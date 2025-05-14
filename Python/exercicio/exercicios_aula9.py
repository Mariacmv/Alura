#1:
# Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @abstractmethod
    def ligar(self):
        pass
#2:
# No mesmo arquivo, crie um construtor para a classe Veiculo que aceita
# os parâmetros marca e modelo.

#3:
# Crie uma nova classe chamada Carro que herda da classe Veiculo.
#from veiculo import Veiculo
class Carro(Veiculo):
    
#4:
# No construtor da classe Carro, utilize o método super() para chamar 
# o construtor da classe pai e atribua o atributo específico cor à 
# classe filha.
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
        
    def ligar(self): #precisa implementar a classe abstrata em todas as outras classes
        print(f'O carro {self.modelo} da marca {self.marca} está ligado')
        
    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.cor})'
