#7:
# Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no 
# mesmo diretório que suas classes. (V)

#8:
# Importe e Instancie Objetos: No arquivo main.py, importe as classes 
# Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com 
# diferentes marcas, modelos, quantidade de portas e tipos.
from carro import Carro
from moto import Moto

def main():
    carro1 = Carro('BMW', 'X1', 4)
    moto1 = Moto('Honda', 'XR 300L Tornado', 'Casual')
    
#9:
# Exiba as Informações: Para cada instância, imprima no console as 
# informações utilizando o método str.
    print(carro1)
    print(moto1)
    
