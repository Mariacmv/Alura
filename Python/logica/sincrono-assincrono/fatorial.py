import asyncio
import math

numeros = [5, 3, 7, 4, 6]

async def calcular_fatorial(n):
    await asyncio.sleep(n) 
    print(f"Fatorial de {n} = {math.factorial(n)}")

async def main():
    tarefas = [asyncio.create_task(calcular_fatorial(n)) for n in numeros]
    await asyncio.gather(*tarefas)

asyncio.run(main())