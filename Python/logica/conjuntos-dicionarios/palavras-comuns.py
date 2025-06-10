texto1 = input('Texto 1: ').lower().split() #split é a função que separa por palavras
texto2 = input('Texto 2: ').lower().split()

print(f'\nTexto 1: {texto1}')
print(f'Texto 2: {texto2}\n')

TEXTO1 = set(texto1)
TEXTO2 = set(texto2)
    
print(f'Palavras em comum: {TEXTO1.intersection(TEXTO2)}')
