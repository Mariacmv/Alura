URL = input("Digite a URL para verificação: ")


if URL[:8] == 'https://' and URL[-4:] == '.com':
    print('URL válida!')
else:
    print('URL inválida!')
    
#OU

url = input("Digite a URL para validação: ") 
if url.startswith("https://") and url.endswith(".com"):
    print("URL válida!")
else:
    print("URL inválida!")
