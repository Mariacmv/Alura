from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_persona import *
from selecionar_documento import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"
contexto = carrega('dados/ecomart.txt')

#Criando um assistente através do python
assistente = cliente.beta.assistants.create( #é cliente porque vai utilizar os recursos da openai que estão em beta no modo assistente. Utiliza o método create para criar
    name="Atendente EcoMart",
    instructions= f"""
        Você é um chatbot de atendimento a clientes de um e-commerce.
        Você não deve responder perguntas que não sejam dados do ecommerce informado!
        Além disso, adote a persona abaixo para responder ao cliente.
        
        ##Contexto
        {contexto}
        
        ##Persona
        {personas["neutro"]}
    """,
    model=modelo
)

#ele gera um id para cada assistente gerado
# print(assistente.id) 

#Cria uma thread para salvar o histórico da conversa
thread = cliente.beta.threads.create( 
    messages=[
        {
            "role":"user",
            "content":"Liste os produtos"
        }
    ]
)

cliente.beta.threads.messages.create( #adiciona a mensagem do usuário à conversa para contextualizar o modelo
    thread_id=thread.id,
    role="user",
    content= " da categoria moda sustentável"
)

run = cliente.beta.threads.runs.create( #executa as threads
    thread_id=thread.id, #passa a thread
    assistant_id=assistente.id #e o assistente como parâmetros
)

while run.starts != "completed":
    #time.sleep(1) #para evitar sobrecarregar
    run = cliente.beta.threads.runs.retrieve( 
        thread_id=thread.id,
        run_id=run.id #recebe o id da execução 
    )
    
historico = cliente.beta.threads.messages.list(thread_id=thread.id).data #acessa uma camada de dados com uma lista de threads que contém as conversas

for mensagem in reversed(historico): #acessa em ordem reversa
    print(f"role: {mensagem.role}\nConteúdo:  {mensagem.content[0].text.value}") #acessa o conteúdo textual da mensagem