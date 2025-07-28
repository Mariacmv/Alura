from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
modelo = "gpt-4"
cliente = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

prompt_system = """
    Você é um assistente técnico que ajuda estudantes a planejar seus projetos acadêmicos.
    Dê respostas práticas e diretas, sem enrolação em bullet-points enumerados.
"""
prompt_user = input("Digite o tema do seu projeto: ")

resposta = cliente.chat.completions.create(
    messages = [
        {
            "role":"system",
            "content":prompt_system    
        },
        {
            "role":"user",
            "content":prompt_user
        },
    ],
)

print(resposta.choices[0].message.content)