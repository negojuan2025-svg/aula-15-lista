convidados = []

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º convidado: ")
    convidados.append(nome)

print("\n--- Lista de Convidados ---")
for convidado in convidados:
    print(f"- {convidado}")

print(f"\nTotal de convidados: {len(convidados)}")