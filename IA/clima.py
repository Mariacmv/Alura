import numpy as nm

estados = ['Ensolarado', 'Nublado', 'Chuvoso'] #estados do clima

transicao = [ #matriz de transição para cada estado
    (0.8,0.15,0.05), #ensolarado - nublado - chuvoso
    (0.2,0.6,0.2), #nublado - ensolarado - chuvoso
    (0.25,0.25,0.5)  #chuvoso - ensolarado - nublado
]

estado_inicial = "Chuvoso"
dias = 10

def pega_indice_estado(estado_inicial): #pega o índice do estado porque a matriz trabalha com posições
    return estados.index(estado_inicial)
    
def prever_estado(estado_inicial, dias):
    estado_atual = estado_inicial
    previsao = [estado_atual]
    
    for _ in range(dias - 1):
        indice_atual = pega_indice_estado(estado_atual) #pego o índice do estado atual
        proximo_estado = nm.random.choice(
            estados,
            p=transicao[indice_atual] #pega as probabilidades de transição do estado atual e escolhe aleatoriamente de acordo com as probabilidades
        )
        previsao.append(proximo_estado)
        estado_atual = proximo_estado
        
    return previsao

previsao = prever_estado(estado_inicial, dias)

print(F"Estado inicial: {estado_inicial}")
print("Previsão para os próximos dias: ")
for dia, estado in enumerate(previsao, start=1):
    print(f"Dia {dia}: {estado}")