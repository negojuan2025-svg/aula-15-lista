precos = []

for i in range(5):
    valor = float(input(f"Digite o {i+1}º preço: R$ "))
    precos.append(valor)

print(f"\nMaior preço: R$ {max(precos):.2f}")
print(f"Menor preço: R$ {min(precos):.2f}")