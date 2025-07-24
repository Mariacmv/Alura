# Código que lê um arquivo csv e devolve uma resposta do gpt de acordo com os dados e o prompt definido:
# O perfil de compra de cada cliente em 3 palavras

#Define as biblioteca necessárias
from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken                     #pip install tiktoken

#Carrega as chaves e define o modelo
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

#Define o codificador de acordo com o modelo
codificador = tiktoken.encoding_for_model(modelo)

#carrega um arquivo com os dados (para verificar se é possível utilizar o modelo definido)
def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e: #o que é IOError?
        print(f"Erro: {e}")

prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

#passa o caminho do arquivo para a função que lê o arquivo
prompt_usuario = carrega("dados\lista_de_compras_100_clientes.csv") 

#verifica se o conjunto do prompt do sistema e do usuário sejam adequados
lista_de_tokens = codificador.encode(prompt_sistema + prompt_usuario)
numero_de_tokens = len(lista_de_tokens)
print(f"Número de tokens na entrada: {numero_de_tokens}")
tamanho_esperado_saida = 2048

#para utilizar o melhor modelo de acordo com os dados - tokens identificados
if numero_de_tokens >= 4096 - tamanho_esperado_saida:
    modelo = "gpt-4-1106-preview"

print(f"Modelo escolhido: {modelo}")

lista_mensagens = [
        {
            "role": "system",
            "content": prompt_sistema
        },
        {
            "role": "user",
            "content": prompt_usuario
        }
    ]

resposta = client.chat.completions.create(
    messages = lista_mensagens,
    model=modelo
)

print(resposta.choices[0].message.content)