class Restaurante: #uma classe define um estrutura modelo, um molde
    nome = ''
    categoria = ''
    status = False

#Instanciando uma classe: criando um objeto
restaurante_praca = Restaurante() #variável do tipo Restaurante
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]
# print(restaurantes)

restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

#Para imprimir um objeto é necessário utilizar a função dir
# print(dir(restaurante_praca))

#1: Atribua o valor 'Italiana' ao atributo categoria da instância 
# restaurante_praca da classe Restaurante
restaurante_praca.categoria = 'Italiana' #(V)

#2: Acesse o valor do atributo nome da instância restaurante_praca
# da classe Restaurante.
print(restaurante_praca.nome) #(V) ou: nome_do_restaurante = restaurante_praca.nome

#3: Verifique o valor inicial do atributo status para a instância
# restaurante_praca e exiba uma mensagem informando se o 
# restaurante está ativo ou inativo.
if (Restaurante.status == False):
    print('Status: Inativo')
elif (Restaurante.status == True):
    print('Status: Ativo')         #(V) ou: 
                                             # if restaurante_praca.ativo:
                                             #     print('O restaurante está ativo.')
                                             # else:
                                             #     print('O restaurante está inativo.')    
    
#4: Acesse o valor do atributo de classe categoria diretamente da
# classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria #para acessar o atributo não precisa de parênteses (V)

#5: Altere o valor do atributo nome para 'Bistrô'.
Restaurante.nome = 'Bistrô' #preciso mudar da instância, então: restaurante_praca.nome = 'Bistrô'

#6: Crie uma nova instância da classe Restaurante chamada 
# restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast 
# Food'.
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'  #(V)

#7: Verifique se a categoria da instância restaurante_pizza é 
# 'Fast Food'.
print(restaurante_pizza.categoria) #para verificar utiliza o if:
                                                                # if restaurante_pizza.categoria == 'Fast Food':
                                                                #     print('A categoria é Fast Food')
                                                                # else:
                                                                #     print('A categoria não é Fast Food')

#8: Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.status = True #(V)

#9: Imprima no console o nome e a categoria da instância 
# restaurante_praca.
print(restaurante_praca.nome, restaurante_praca.categoria) #(V)
#Porém é possível deixar mais amigável:
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
