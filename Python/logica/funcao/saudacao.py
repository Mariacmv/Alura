def saudacao(hora):
    if hora < 12:
        print("Bom dia")
    elif hora > 12 and hora < 19:
        print("Boa tarde")
    elif hora > 18:
        print("Boa noite")
    else:
        print("Horário inválido")
        
hora = int(input("Digite a hora atual (0-23): "))
saudacao(hora)