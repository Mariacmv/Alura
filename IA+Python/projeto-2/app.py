from flask import Flask,render_template, request, Response
from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_persona import *
from selecionar_documento import *
from assistente_ecomart import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

app = Flask(__name__)
app.secret_key = 'maria' #no curso é 'alura'

# assistente = criar_assistente()
# thread = criar_thread()
assistente = pegar_json()
thread_id = assistente["thread_id"]
assistente_id = assistente["assistant_id"]
file_ids = assistente["file_ids"]

#constantes para dizer o estado das functions
STATUS_COMPLETED = "completed"
STATUS_REQUIRES_ACTION = "requires_action"

def bot(prompt): #resposta do chatbot
    maximo_tentativas = 1 #para cada interação com o usuário
    repeticao = 0
    # personalidade = personas[selecionar_persona(prompt)] #definindo a personalidade
    # contexto = selecionar_contexto(prompt) #define um contexto
    # documento_selecionado = selecionar_documento(contexto) #seleciona o documento de acordo com o contexto identificado
    while True: #uso do try=except para evitar exceções interromperem a execução correta
        try:
    #         prompt_do_sistema = f"""
    #         Você é um chatbot de atendimento a clientes de um e-commerce. 
    #         Você não deve responder perguntas que não sejam dados do e-commerce informado!
    #         Você deve gerar respostas utilizando o contexto abaixo:
    #         Você deve adotar a persona abaixo.
    #         # Contexto
    #         {documento_selecionado}
    #         #Persona
    #         {personalidade}
    #         """
    #         response = cliente.chat.completions.create(
    #             messages=[
    #                     {
    #                             "role": "system",
    #                             "content": prompt_do_sistema
    #                     },
    #                     {
    #                             "role": "user",
    #                             "content": prompt
    #                     }
    #             ],
    #             temperature=1,
    #             max_tokens=300,
    #             top_p=1,
    #             frequency_penalty=0,
    #             presence_penalty=0,
    #             model = modelo)
    #         return response
            personalidade = personas[selecionar_persona(prompt)]
            
            cliente.beta.threads.messages.create(
                thread_id = thread_id,
                role = "user",
                content = f"""
                Assuma, de agora em diante, a personalidade abaixo.
                Ignore as personalidades anteriores.
                
                # Persona
                {personalidade}
                """,
                file_ids=file_ids #para visualizar os arquivos e escolher o mais apropriado
            )
            
            cliente.beta.threads.messages.create(
                thread_id = thread_id,
                role="user",
                content=prompt,
                file_ids=file_ids
            )
            
            run = cliente.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistente_id
            )
            
            while run.status != STATUS_COMPLETED:
                run = cliente.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id
            )
                
            #log de verificação do status do assistente
                print(f"Status: {run.status}")    
                
                #caso tenha acontecido um desvio de processo
                if run.status == STATUS_REQUIRES_ACTION: #significa que uma function foi chamada
                    tools_acionadas = run.required_action.submit_tool_outputs.tool_calls #verifica que existem ferramentas que realizam o trabalho requerido e as chama
                    respostas_tools_acionadas = [] #para cada ferramenta chamada retorna uma resposta
                    for uma_tool in tools_acionadas: #dentro das ferramentas escolhidas e adiciona à variável temporária tools_acionadas
                        nome_funcao = uma_tool.function.name #pega o nome da função
                        funcao_escolhida = minhas_funcoes[nome_funcao] #associa o nome da função ao método lá do dicionário criado para as functions
                        argumentos = json.loads(uma_tool.function.arguments) #pega o codigo e a validade - o que foi requerido na criação da function
                        print(argumentos)
                        resposta_funcao = funcao_escolhida(argumentos) 
                        
                        resposta_tools_acionadas.append({
                            "tool_call_id":uma_tool.id, #id da ferramenta
                            "output":resposta_funcao #informação da resposta gerada
                        }) #adiciona a resposta recebida para que mude o status
                        
                run = cliente.beta.threads.runs.submit_tool_output(
                    thread_id = thread_id,
                    run_id = run.id,
                    tool_outputs = respostas_tools_acionadas #todas as respostas
                ) #para enviar as respostas para as ferramentas
                
            historico = list(cliente.beta.threads.messages.list(thread_id=thread_id).data)
            resposta = historico[0]
            return resposta

        except Exception as erro:
                repeticao += 1
                if repeticao >= maximo_tentativas:
                        return "Erro no GPT: %s" % erro
                print('Erro de comunicação com OpenAI:', erro)
                sleep(1)

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    texto_resposta = resposta.choices[0].text.value #busca o valor dentro do atributo texto
    return texto_resposta

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
    
            
            
        
