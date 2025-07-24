import tiktoken

modelo = "gpt-4"
codificador = tiktoken.encoding_for_model(modelo)
lista_tokens = codificador.encode("Você é um categorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantidade de tokens: ", len(lista_tokens))
print(f"Custo para o modelo {modelo}: ${(len(lista_tokens)/1000) * 0.03}")

modelo = "gpt-3.5-turbo-1106"
codificador = tiktoken.encoding_for_model(modelo)
lista_tokens = codificador.encode("Você é um categorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantidade de tokens: ", len(lista_tokens))
print(f"Custo para o modelo {modelo}: ${(len(lista_tokens)/1000) * 0.03}")

print("O custo do GPT4 é de {0.03/0.001} maior que o do GPT 3.5-turbo") #em relação a mesma frase