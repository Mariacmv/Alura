import asyncio
 
async def tarefa(numero, tempo):
    await asyncio.sleep(tempo)
    print(f"Tarefa {numero} finalizada!")
 
async def main():
    tempos = [3, 5, 7]
    tarefas = [asyncio.create_task(tarefa(i+1, tempos[i])) for i in range(3)]
 
    while any(not t.done() for t in tarefas): #de onde veio 't'?
        status = ['Finalizado' if t.done() else 'Em andamento' for t in tarefas]
        print(f"Status das tarefas: {status}")
        await asyncio.sleep(1) 
 
    await asyncio.gather(*tarefas) #o que significa '*'
 
asyncio.run(main())