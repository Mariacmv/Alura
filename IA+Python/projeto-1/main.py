from openai import OpenAI        #importa a biblioteca da ia
from dotenv import load_dotenv   #importa o dotenv que permite a comunicação com API (?) e o carrega
import os                        #importa o sistema operacional

load_dotenv() #ler as chaves de acesso com o dotenv
cliente = OpenAI(api_key=os.getenv("OPEN_AI_KEY")) #objeto que acessa a openai através do construtor openai e acessa a chave de acesso

resposta = cliente.chat.completions.create(
    messages=[ #lista com mensagens que são definidas por dicionários
        { #Mensagem 1
            "role":"system", #o papel do quê?
            "content":"Listar apenas os nomes dos produtos, sem a descrição" #o conteúdo da mensagem
        },
        { #Mensagem 2
            "role":"user",
            "content":"Liste 3 produtos sustentáveis"
        }
    ],
    model="gpt-4" #modelo utilizado
) #defino o objeto que define a resposta do gpt

#print(resposta) 
print(resposta.choices[0].message.content) #acessa a primeira resposta (choices é um subatributo) e o conteúdo da mensagem para tornar em texto limpo, não json