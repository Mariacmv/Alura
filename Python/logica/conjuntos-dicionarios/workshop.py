participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 

retirar = input("Digite o nome a ser retirado: ")

for valor in participantes:
    if retirar in participantes[valor]:  
        participantes[valor].remove(retirar)
        print(f'Participante {retirar} removido com sucesso')


print("Participantes atualizados:")
for workshop, nomes in participantes.items():
    print(f"{workshop}: {nomes}")

