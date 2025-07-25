from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
modelo = "gpt-4"

prompt_system = """
    Você é um assistente técnico que ajuda estudantes a planejar seus projetos acadêmicos.
    Dê respostas práticas e diretas, sem enrolação.
"""
prompt_user = """
    Quero fazer um projeto sobre CiberSegurança. Por onde eu começo?
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
        },
    ],
    model = modelo
)