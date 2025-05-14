import requests #utilizado para fazer requisições http de forma simplificada
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' #é um endpoint (é o endereço de uma API que retorna um arquivo JSON contendo dados de restaurantes). Um código json (parece um dicionário python dentro de uma lista) que contém dados de restaurantes
response = requests.get(url) #get (significa 'solicitar e recuperar dados') é um verbo do http para solicitar um recurso. O response é o que o programa vai receber do json. É o que faz requisição à API
print(response) #se devolver 200 quer dizer que a solicitação foi atendida com sucesso, independente da ação

#caso o arquivo esteja correto retorna os dados
if response.status_code == 200: #status_code -> representa o status do código que é retornado
    try:
        dados_json = response.json() #armazeno o resultado em uma variável de uma forma que o python entende, no caso dicionário ou lista
        #print(dados_json)
        
        dados_restaurante = {} #dicionário vazio para organizar os dados dos restaurantes
        for item in dados_json: #percorre a lista dos dados do json e pega o nome do restaurante apenas
            nome_do_restaurante = item['Company']
            if nome_do_restaurante not in dados_restaurante: #verificação para não duplicar
                dados_restaurante[nome_do_restaurante] = [] #crio uma lista, por exemplo, para armazenar os nomes
        
            dados_restaurante[nome_do_restaurante].append({
                "item":item['Item'],
                "price":item['price'],
                "description":item['description']
            })#para adicionar o item à lista criada
            
        for nome_do_restaurante, dados in dados_restaurante.items():
            nome_do_arquivo = f'{nome_do_restaurante}.json'
            with open(nome_do_arquivo, 'w') as arquivo_restaurante:
                #quero criar um json
                json.dump(dados, arquivo_restaurante,indent=4) #quero gerar um arquivo. Passo os dados que quero exibir, o nome do arquivo que estou trabalhando e um indent para deixar formatado
    except ValueError as e:
        print(f'Erro ao processar o JSON: {e}') 
else:
    print(f'O erro foi {response.status_code}') #retorna o tipo de erro
    
# print(dados_restaurante['McDonald’s'])
