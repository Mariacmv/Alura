telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

def converte(telefones):
    return [int(telefone) for telefone in telefones] #converte cada item da lista para inteiro

def confere(telefones):
    for telefone in telefones:
        if type(telefone) != int: #seria melhor isinstance -> if not isinstance(telefone, int)
            print(f"{telefone} não é inteiro")
    print("Todos os números foram convertidos corretamente!")
    
resultado = converte(telefones)
confere(resultado)