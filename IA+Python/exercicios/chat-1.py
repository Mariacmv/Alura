from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

modelo = "gpt-4"

prompt_system = """
    Responda apenas com os nomes. Não adicione descrições nem comentários.
"""
prompt_user = """
    Quais nomes criativos você sugere para um cafeteria com tema vintage?
"""

resposta = cliente.chat.completions.create(
    messages = [
        {
            "role":"system",
            "content":prompt_system
        },
        {
            "role":"user",
            "content":prompt_user  
        }
    ],
    model = modelo,
)

print("Sugestões de nome para a cafeteria: ")
print(resposta.choices[0].message.content)