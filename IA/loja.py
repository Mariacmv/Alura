# Este código representa uma rede bayesiana simples 
# Representa um exemplo baseado em experiências anteriores 


# Rede Bayesiana
probabilidades = {
    "HistoricoCompras": {0: 0.7, 1: 0.3},  # 0: Não tem histórico, 1: Tem histórico
    "TempoNoSite": {0: 0.6, 1: 0.4},       # 0: Pouco tempo, 1: Muito tempo
    "ClicouEmPromocao": {0: 0.8, 1: 0.2},  # 0: Não clicou, 1: Clicou
    "Compra": { #variável-alvo: mapeia todas as combinações possíveis
        (0, 0, 0): 0.1,  # Não tem histórico, pouco tempo, não clicou
        (0, 0, 1): 0.3,  # Não tem histórico, pouco tempo, clicou
        (0, 1, 0): 0.2,  # Não tem histórico, muito tempo, não clicou
        (0, 1, 1): 0.6,  # Não tem histórico, muito tempo, clicou
        (1, 0, 0): 0.4,  # Tem histórico, pouco tempo, não clicou
        (1, 0, 1): 0.7,  # Tem histórico, pouco tempo, clicou
        (1, 1, 0): 0.8,  # Tem histórico, muito tempo, não clicou
        (1, 1, 1): 0.9   # Tem histórico, muito tempo, clicou
    }
}

# Cenário de teste: define um cenário específico
evidencias = { #fatores que determinam se um evento ocorrerá ou não
    'HistoricoCompras': 1, #tem histórico de compras
    'TempoNoSite': 0, #tem pouco tempo no site
    'ClicouEmPromocao': 1 #clicou em promoção
}

def calcular_probabilidade_compra(evidencias): #pega as evidências definidas e procura no dicionário
    historico = evidencias["HistoricoCompras"] #variável recebe valores de HistoricoCompras do dicionário evidencias
    tempo = evidencias["TempoNoSite"]
    promocao = evidencias["ClicouEmPromocao"]
    
    prob_compra = probabilidades["Compra"][(historico, tempo, promocao)]
    prob_nao_compra = 1 - prob_compra
    
    return {"Comprar": prob_compra, "Não Comprar": prob_nao_compra}

resultados = calcular_probabilidade_compra(evidencias)
print("Probabilidades de Compra: ")
for resultado, probabilidade in resultados.items():
    print(f"{resultado}: {probabilidade:.2f}")
    