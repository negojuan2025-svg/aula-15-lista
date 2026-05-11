tarefas = []

while True:
    tarefa = input("Digite uma tarefa (ou 'fim' para encerrar): ")
    if tarefa.lower() == "fim":
        break
    tarefas.append(tarefa)

print("\n--- Suas Tarefas ---")
for t in tarefas:
    print(f"[ ] {t}")