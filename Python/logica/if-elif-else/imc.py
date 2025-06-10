peso = float(input("Digite seu peso (KG): "))
altura = float(input("Digite sua altura (M): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com peso normal.")
elif imc >= 25:
    print("Você está acima do peso.")