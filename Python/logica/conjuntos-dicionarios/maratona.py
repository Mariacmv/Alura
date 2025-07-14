participantes = { 

    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35 

} 

print(f"Nomes dos participantes: {', '.join(participantes.keys())}")
print(f"Idades dos participantes: {', '.join(str(idade) for idade in participantes.values())}")

for nome, idade in participantes.items():
    print(f'- {nome}: {idade} anos')