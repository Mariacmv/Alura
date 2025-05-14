from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio #importando a classe cardápio

class Restaurante: #uma classe define um estrutura modelo, um molde
    '''Representa um restaurante e suas características'''
    restaurantes = [] #é um atributo da classe Restaurante
    
    def __init__(self, nome, categoria): #função que serve como construtor. parâmetro self faz referência ao objeto que está sendo instanciado
        '''Construtor da classe restaurante que apresenta:
            - atributos privados
            - lista com cada avaliação
            - adicionando um objeto à lista de restaurantes'''
        self._nome = nome.title() #só a primeira letra maiúscula
        self._categoria = categoria.upper() #toda as letras ficam maiúsculas
        self._status = False #ao passar os atributos como self eles DEVEM ser passados como parâmetro
        self._cardapio = [] #começa como uma lista vazia
        self._avaliacao = [] #defino no construtor de restaurante porque estaria integrado ao restaurante? (sim, fazendo com que cada restaurante tenha sua avaliação) Armazenado como lista porque será mais de uma informação? (sim)
        Restaurante.restaurantes.append(self) #toda vez que criar um objeto eu o adiciono à lista
    
    def __str__(self): #método especial que transforma em string 
        '''Apresenta o nome e a categoria de um restaurante'''
        return f'{self._nome} | {self._categoria}' #self.o que quero exibir, o return que faz a devolução

    def listar_restaurantes(): #consigo determinar que é um método próprio porque não tem __a__
        '''Apresenta ao ser chamado o(s) nome(s) do(s) restaurante(s), bem como a categoria, a avaliação e o status dele'''
        print(f"{'Nome do restaurante'.ljust(46)} | {'Categoria'.ljust(36)} | {'Avaliação'.ljust(25)} | {'Status'}") #coloca entre chaves para manter o espaçamento definido abaixo
        for restaurante in Restaurante.restaurantes:
            print(f'Nome do restaurante: {restaurante._nome.ljust(25)} | Categoria: {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes)} | Status: {restaurante.status}') #pegando da lista, por isso não utiliza o self. Para imprimir não utiliza o _status porque se refere ao atributo não à propriedade status. Pra imprimir a média tem que transformar em string por quê? Porque ljust só funciona com strings

    @property
    def status(self): #pra definir se 
        '''Define o status do restaurante como V ou X'''
        return '✓' if self._status else '✗'
        
    def alternar_estado(self): #método para os objetos
        '''Alterna o status do restaurante'''
        self._status = not self._status
        
    def receber_avaliacao(self, cliente, nota): #self significa o próprio objeto. Aqui em avaliação acontece a composição
        '''Recebe a avaliação do cliente que possui uma condição de ser entre 0 e 5 apenas'''
        if (0<= nota <=5):
            avaliacao = Avaliacao(cliente, nota) #por que criar um objeto aqui? Porque encapsula as informações em um objeto, tornando mais fácil uma modificação futura. Porque é uma composição
            self._avaliacao.append(avaliacao)

    @property #para eu poder ler essas informações
    def media_avaliacoes(self):
        '''Realiza o cálculo da média de avaliação de cada restaurante da lista'''
        if not self._avaliacao: #se o restaurante não tiver nenhuma avaliação
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #percorre todas as avaliações e pega só a nota, no final, soma todas as notas
        quantidade_notas = len(self._avaliacao) #pra fazer o cálculo preciso ter todas as notas então vou pegar todas as notas armazenadas
        media = round(soma_das_notas/quantidade_notas, 1) #nas regras de negócio do app diz que cada nota só mostrará até uma casa decimal, para isso existe a função round que recebe o que será arredondado, até quantas casas decimais
        return media
    
    
    # def adiciona_bebida_no_cardapio(self, bebida):
    #     self._cardapio.append(bebida) #adiciona a bebida ao cardapio
    
    # def adiciona_prato_no_cardapio(self, prato):
    #     self._cardapio.append(prato)
    
    #refatorando as funções de adicionar itens ao cardápio:
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): #verifica se é uma instância de tal classe ou se for derivada da classe
            self._cardapio.append(item) #adiciona o item ao cardápio

    @property
    def exibir_cardapio(self): #self apenas porque só quero ler
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1): #função que enumera. 'start=1' é porque começa do 0, então é melhor começar do 1
            if hasattr(item, 'descricao'): #se tiver o atributo   
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'#mostro o item
                print(mensagem_prato) 
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'#mostro o item
                print(mensagem_bebida)
        
        
        
        
        
        
        
#Instanciando uma classe: criando um objeto
# restaurante_praca = Restaurante('praça', 'Gourmet') #variável do tipo Restaurante
# restaurante_praca.alternar_estado()
# restaurante_pizza = Restaurante('pizza express', 'Italiana')

# restaurantes = [restaurante_praca, restaurante_pizza]
# # print(restaurantes)

# restaurante_praca.nome = 'Praça'
# restaurante_praca.categoria = 'Gourmet'

# #Para imprimir um objeto é necessário utilizar a função dir
# print(dir(restaurante_praca))

# Restaurante.listar_restaurantes()









# class Musica:
#     nome = ''
#     artista = ''
#     duracao = float
    
# faixa1 = Musica('Still with you', 'Jungkook', 3)
# faixa2 = Musica('Magic Shop', 'BTS', 3,50)
# faixa3 = Musica('Michael Jordan', 'Neffex', 2,95)
 
# #OU

# faixa1 = Musica()
# faixa1.nome('Still with you')
# faixa1.artista('Jungkoook')
# faixa1.duracao(300)

# faixa2 = Musica()
# faixa2.nome('Magic Shop')
# faixa2.artista('BTS')
# faixa2.duracao(350)

# faixa3 = Musica()
# faixa3.nome('Michael Jordan')
# faixa3.artista('Neffex')
# faixa3.duracao(295)

# class Musica(self, nome, artista, duracao):
#     self.nome = nome
#     self.artista = artista
#     self.duracao = duracao
    
# faixa1 = Musica('Soap', 'Melanie Martinez', 310)