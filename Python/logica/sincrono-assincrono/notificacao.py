import asyncio

usuarios = [
    {"nome": "Ana", "vip": True, "notificacoes_ativadas": True},
    {"nome": "João", "vip": False, "notificacoes_ativadas": True},
    {"nome": "Carla", "vip": False, "notificacoes_ativadas": False},
]

async def enviar_notificacao(usuario):
    if not usuario["notificacoes_ativadas"]:
        print(f"{usuario['nome']} desativou as notificações. Nada foi enviado.")
        return
    
    if usuario["vip"]:
        print(f"Notificação VIP para {usuario['nome']} enviada!")
        return
    
    print(f"Notificação normal para {usuario['nome']} enviada!")

async def main():
    print("Enviando notificações...")
    tarefas = [asyncio.create_task(enviar_notificacao(u)) for u in usuarios]
    await asyncio.gather(*tarefas)
    print("Todas as notificações foram processadas!")

asyncio.run(main())