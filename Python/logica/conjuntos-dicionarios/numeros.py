equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

tarefas = equipe_a.union(equipe_b)

tarefa_remover = input("Digite a tarefa que deseja remover: ").lower()

tarefas.discard(tarefa_remover)

print(equipe_a, '\n', equipe_b)

#não está certo