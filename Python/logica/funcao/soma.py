def recursiva(n):
    if n == 1:
        return 1
    return n + recursiva(n-1)
    
n = int(input("Digite um número: "))
print(f"A soma de 1 a {n} é: {recursiva(n)}")

#NÃO ENTENDI