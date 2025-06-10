n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3)/3

if media >= 7:
    print(media)
    print("Aprovado(a)")
elif 5 <= media < 7:
    print(media)
    print("Recuperação")
else:
    print(media)
    print("Reprovado(a)") 