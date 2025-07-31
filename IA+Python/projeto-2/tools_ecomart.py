#Documento para gerenciar as ferramentas utilizadas no projeto

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
modelo = "gpt-4-1106-preview"

#variável global que armazenará todas as ferramentas
minhas_tools = [
    {"type":"retrieval"}, #tipo: arquivo
    {"type":"function", # function para comunicação com a api da openai, mas também para conversar com apis de terceiros (no playground da openai é possível criar automaticamente)
            "function": {
                        "name": "validar_codigo_promocional",
                        "description": "Valide um código promocional com base nas diretrizes de Descontos e Promoções da empresa",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "codigo": {
                                                "type": "string",
                                                "description": "O código promocional, no formato, CUPOM_XX. Por exemplo: CUPOM_ECO",
                                        },
                                        "validade": {
                                                "type": "string",
                                                "description": f"A validade do cupom, caso seja válido e esteja associado as políticas. No formato DD/MM/YYYY.",
                                        },
                                },
                                "required": ["codigo", "validade"],
                        }
                        }
    }
]

def validar_codigo_promocional(argumentos): #recebe o retorno 'codigo' e 'validade' passado pela ia
    codigo = argumentos.get("codigo") #acessa a informação 
    validade = argumentos.get("validade")
    
    return f"""
        # Formato de Resposta
        {codigo} com validade: {validade}.
        Ainda, diga se é válido ou não para o usuário.
    """
    
#É recomendável sempre armazenar as functions em um dicionário
minhas_funcoes = { 
    "validar_codigo_promocional":validar_codigo_promocional,
} #e tem que passar para o app.py para ele identificar a nova function