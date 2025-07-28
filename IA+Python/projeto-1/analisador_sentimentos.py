from openai import OpenAI
from dotenv import load_dotenv
import os
import openai

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
modelo = "gpt-4"

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e: #tipo de erro de entrada e saída
        print(f"Erro: {e}")
        
def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo) #salva o conteúdo em um arquivo
    except IOError as e: #erro de entrada e saída
        print(f"Erro ao salvar arquivo: {e}")
        
def analisador_sentimentos(produto):
    prompt_sistema = f"""
        Você é um analisador de sentimentos de avaliações de produtos.
            Escreva um parágrafo com até 50 palavras resumindo as avaliações e 
            depois atribua qual o sentimento geral para o produto.
            Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

            # Formato de Saída

            Nome do Produto:
            Resumo das Avaliações:
            Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
            Ponto fortes: lista com três bullets
            Pontos fracos: lista com três bullet """
            
    prompt_usuario = carrega(f"./dados/avaliacoes-Maquiagem mineral.txt")
    print(f"Iniciou a análise de sentimentos do produto Maquiagem mineral")
    
    lista_mensagens = [
        {
            "role":"system",
            "content":prompt_sistema
        },
        {
            "role":"user",
            "content":prompt_usuario  
        }
    ]
    
    #caso seja colocado um modelo errado
    try:
        resposta = cliente.chat.completions.create(
            messages = lista_mensagens,
            model=modelo
        )
        
        texto_resposta = resposta.choices[0].message.content
        salva(f"./dados/analise-{produto}.txt", texto_resposta) #o '.' indica no diretório atual
    
    except openai.AuthenticationError as e:
        print(f"Erro de autenticação; {e}")
    except openai.APIError as e:
        print(f"Erro de API: {e}")
    
    
#análise em lote
lista_de_produtos = ['Maquiagem mineral']
for um_produto in lista_de_produtos:
    analisador_sentimentos(um_produto)