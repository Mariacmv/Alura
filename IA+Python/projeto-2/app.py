from flask import Flask,render_template, request, Response
from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_persona import *
from selecionar_documento import *
from vision_ecomart import analisar_imagem
import uuid #para a manipulação de imagens

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4-1106-preview" #para o uso de imagens

app = Flask(__name__)
app.secret_key = 'maria' #no curso é 'alura'

assistente = pegar_json()
thread_id = assistente["thread_id"]
assistente_id = assistente["assistant_id"]
file_ids = assistente["file_ids"]

STATUS_COMPLETED = "completed"
STATUS_REQUIRES_ACTION = "requires_action"

caminho_imagem_enviada = None
UPLOAD_FOLDER = 'dados'

def bot(prompt): #resposta do chatbot
    global caminho_imagem_enviada 
    maximo_tentativas = 1 #para cada interação com o usuário
    repeticao = 0
    personalidade = personas[selecionar_persona(prompt)] #definindo a personalidade
    contexto = selecionar_contexto(prompt) #define um contexto
    documento_selecionado = selecionar_documento(contexto) #seleciona o documento de acordo com o contexto identificado
    while True: #uso do try=except para evitar exceções interromperem a execução correta
        try:
            prompt_do_sistema = f"""
            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do e-commerce informado!
            Você deve gerar respostas utilizando o contexto abaixo:
            Você deve adotar a persona abaixo.
            # Contexto
            {documento_selecionado}
            #Persona
            {personalidade}
            """
            response = cliente.chat.completions.create(
                messages=[
                        {
                                "role": "system",
                                "content": prompt_do_sistema
                        },
                        {
                                "role": "user",
                                "content": prompt
                        }
                ],
                temperature=1,
                max_tokens=300,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                model = modelo)
            return response
        except Exception as erro:
                repeticao += 1
                if repeticao >= maximo_tentativas:
                        return "Erro no GPT: %s" % erro
                print('Erro de comunicação com OpenAI:', erro)
                sleep(1)

@app.route('/upload_imagem', methods=['POST'])
def upload_imagem():
    global caminho_imagem_enviada
    if 'imagem' in request.files:
        imagem_enviada = request.files['imagem']
        

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    texto_resposta = resposta.choices[0].message.content
    return texto_resposta

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
    
            
            
        
