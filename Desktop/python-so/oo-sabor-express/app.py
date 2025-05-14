from modelos.restaurante import Restaurante #importa a classe restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
# restaurante_praca.adiciona_bebida_no_cardapio(bebida_suco)
# restaurante_praca.adiciona_prato_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(bebida_suco) #um método só
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    # print(bebida_suco)
    # print(prato_paozinho)
    restaurante_praca.exibir_cardapio #chamando o property

if __name__ == '__main__':
    main()
