lista1 = input("Digite as permissões principais: ").strip().lower().split(', ')
lista2 = input("Digite as permissões solicitadas: ").strip().lower().split(', ')

# list(lista1)
# list(lista2)

# print(f'\nPermissões principais: {lista1}')
# print(f'Permissões solicitadas: {lista2}\n')

# for elemento in lista1:
#     if (elemento in lista1) == (elemento in lista2):
#         pertencem = print(f'As permissões solicitadas fazem parte das permissões principais. ')
#     else:
#         Npertencem = print(f'As permissões solicitadas não fazem parte das permissões principais.')
    
for i in range(len(lista1)):  

    lista1[i] = lista1[i].strip() 

for i in range(len(lista2)):  

    lista2[i] = lista2[i].strip() 

eh_subconjunto = lista2.issubset(lista1) 

if eh_subconjunto:  

    print("As permissões solicitadas fazem parte das permissões principais.")  

else:  

    print("As permissões solicitadas não fazem parte das permissões principais.") 