"""
Simular um chat onde o usuário pode conversar com a IA sobre o mesmo 
tema por várias rodadas.
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
modelo = "gpt-4"
cliente = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))  # chave da API definida no .env

prompt_system = """Você é um assistente técnico que ajuda estudantes a planejar seus projetos acadêmicos.
Dê respostas práticas e diretas, sem enrolação em bullet-points enumerados."""

prompt_user = input("Digite o tema do seu projeto ou 'sair' para parar: ")

if prompt_user.lower() == "sair":
    print("Ok, até mais!")
    exit()

messages = [
    {"role": "system", "content": prompt_system},
    {"role": "user", "content": f"Quero fazer um projeto sobre {prompt_user}. Por onde começo?"}
]

# Primeira resposta da IA
resposta = cliente.chat.completions.create( # requisição principal para a ia
    messages=messages,
    model=modelo
)
resposta_ia = resposta.choices[0].message.content
print("IA:", resposta_ia)
messages.append({"role": "assistant", "content": resposta_ia})

# Loop de conversa contínua
while True:
    pergunta = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")
    if pergunta.lower() == "sair":
        print("Ok, até mais!")
        break

    messages.append({"role": "user", "content": pergunta})

    resposta = cliente.chat.completions.create(
        messages=messages,
        model=modelo
    )

    resposta_ia = resposta.choices[0].message.content
    print("IA:", resposta_ia)

    messages.append({"role": "assistant", "content": resposta_ia})
