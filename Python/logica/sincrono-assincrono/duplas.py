# Corrotinas são funções que podem ser pausadas e retomadas depois

import asyncio 
async def baixar_dados(): #corrotina 1
       print("Iniciando download...") 
       await asyncio.sleep(2) 
print("Download concluído!") 
async def analisar_dados(): #corrotina 2
       print("Iniciando análise de dados...") 
       await asyncio.sleep(3) 
       print("Análise de dados concluída!") 
async def main(): #corrotina 3
       await asyncio.gather(baixar_dados(), analisar_dados()) #para executar simultaneamente, recebe tarefas e aguarda a execução de todas

asyncio.run(main()) #sempre utiliza run para executar uma corrotina