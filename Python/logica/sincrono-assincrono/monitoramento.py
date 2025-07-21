import asyncio

arquivos = {
    "arquivo_1.txt": 30,
    "arquivo_2.txt": 45,
    "arquivo_3.txt": 20,
    "arquivo_4.txt": 10, 
    "arquivo_5.txt": 50,
}

VELOCIDADE_DOWNLOAD = 5 

async def baixar_arquivo(nome, tamanho):
    print(f"Iniciando download de {nome} (tamanho: {tamanho}MB)...")
    
    baixado = 0
    segundos = 0
    
    while baixado < tamanho:
        await asyncio.sleep(1)  
        baixado += VELOCIDADE_DOWNLOAD
        baixado = min(baixado, tamanho)
        segundos += 1
        print(f"[{segundos}s] {nome}: {baixado}MB baixados")

    print(f"{nome} concluído!\n")

async def main():
    tarefas = [asyncio.create_task(baixar_arquivo(nome, tamanho)) for nome, tamanho in arquivos.items()]
    await asyncio.gather(*tarefas)
    print("\nTodos os downloads foram finalizados!")

asyncio.run(main())