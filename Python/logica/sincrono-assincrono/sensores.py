import asyncio
import random

async def sensor_temperatura():
    while True:
        await asyncio.sleep(2)
        temp = random.randint(20, 30)
        print(f"[{2}s] Temperatura: {temp}°C")

async def sensor_umidade():
    while True:
        await asyncio.sleep(3)
        umidade = random.randint(50, 70)
        print(f"[{3}s] Umidade: {umidade}%")

async def sensor_qualidade_ar():
    while True:
        await asyncio.sleep(5)
        qualidade = random.choice(["Boa", "Regular", "Ruim"])
        print(f"[{5}s] Qualidade do ar: {qualidade}")

async def main():
    await asyncio.gather(sensor_temperatura(), sensor_umidade(), sensor_qualidade_ar())

asyncio.run(main())