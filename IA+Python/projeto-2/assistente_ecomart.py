from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_persona import *
from selecionar_documento import *
import json
from tools_ecomart import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4-1106-preview" #modelo que permite carregar arquivos
contexto = carrega('dados/ecomart.txt')

#cria a lista para acessar os arquivos
def criar_lista_ids():
    lista_ids_arquivos = []
    file_dados = cliente.files.create(
        file=open("dados/dados_ecomart.txt", "rb"), #método open está no helper
        purpose="assistants"
    )
    lista_ids_arquivos.append(file_dados.id)
    
    file_politicas = cliente.files.create(
        file=open("dados/politicas_ecomart.txt", "rb"),
        purpose="assistants"
    )
    lista_ids_arquivos.append(file_politicas.id)
    
    file_produtos = cliente.files.create(
        file=open("dados/produtos_ecomart.txt", "rb"),
        purpose="assistants"
    )
    lista_ids_arquivos.append(file_produtos.id)
    
    return lista_ids_arquivos

#pegar o arquivo json; caso não exista criar ele (arquivo de metadados)
def pegar_json():
    filename = "assistentes.json"
    
    if not os.path.exists(filename): #caso o caminho não exista
        thread_id = criar_thread()
        file_id_list = criar_lista_ids()
        assistant_id = criar_assistente(file_id_list)
        data = { #corpo do arquivo json
            "assistant_id":assistant_id.id,
            "thread_id":thread_id.id,
            "file_ids":file_id_list
        }
        
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Arquivo 'assistentes.json' criado com sucesso.")
        
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Arquivo 'assistentes.json' não encontrado.")
        
def criar_thread():
    return cliente.beta.threads.create()

def criar_assistente(file_ids=[]): #passa uma lista vazia caso não queira passar dados fixos
    #Criando um assistente através do python
    assistente = cliente.beta.assistants.create( #é cliente porque vai utilizar os recursos da openai que estão em beta no modo assistente. Utiliza o método create para criar
        name="Atendente EcoMart",
        instructions= f"""
            Você é um chatbot de atendimento a clientes de um e-commerce.
            Você não deve responder perguntas que não sejam dados do ecommerce informado!
            Além disso, adote a persona abaixo para responder ao cliente.
            
        """,
        model=modelo,
        tools = minhas_tools,
        file_ids = file_ids
    )
    return assistente

#ele gera um id para cada assistente gerado
# print(assistente.id) 

# #Cria uma thread para salvar o histórico da conversa
# thread = cliente.beta.threads.create( 
#     messages=[
#         {
#             "role":"user",
#             "content":"Liste os produtos"
#         }
#     ]
# )

# cliente.beta.threads.messages.create( #adiciona a mensagem do usuário à conversa para contextualizar o modelo
#     thread_id=thread.id,
#     role="user",
#     content= " da categoria moda sustentável"
# )

# run = cliente.beta.threads.runs.create( #executa as threads
#     thread_id=thread.id, #passa a thread
#     assistant_id=assistente.id #e o assistente como parâmetros
# )

# while run.starts != "completed":
#     #time.sleep(1) #para evitar sobrecarregar
#     run = cliente.beta.threads.runs.retrieve( 
#         thread_id=thread.id,
#         run_id=run.id #recebe o id da execução 
#     )
    
# historico = cliente.beta.threads.messages.list(thread_id=thread.id).data #acessa uma camada de dados com uma lista de threads que contém as conversas

# for mensagem in reversed(historico): #acessa em ordem reversa
#     print(f"role: {mensagem.role}\nConteúdo:  {mensagem.content[0].text.value}") #acessa o conteúdo textual da mensagem