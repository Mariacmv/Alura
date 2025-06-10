equipea = input("Equipe A: ").lower().split(', ')
equipeb = input("Equipe B: ").lower().split(', ')

list(equipea)
list(equipeb)

print(equipea)
print(equipeb)

equipea.append(equipeb)

for elemento in equipea:
    if elemento in equipea:
        equipea.pop(elemento)

print(f'Depois de adicionar: {equipea}')