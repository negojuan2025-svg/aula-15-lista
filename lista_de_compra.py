compras = []

while True:
    print("\n--- MENU DE COMPRAS ---")
    print("1 - Adicionar | 2 - Pesquisar | 3 - Remover | 4 - Alterar | 5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            item = input("Digite o produto (ou 'sair'): ").lower()
            if item == "sair": break
            compras.append(item)
    
    elif opcao == "2":
        busca = input("Pesquisar por: ").lower()
        if busca in compras:
            print(f"Produto encontrado: {busca}")
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        remover = input("Nome do produto para remover: ").lower()
        if remover in compras:
            compras.remove(remover)
            print("Produto encontrado e removido.")
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        # Ajustado para a lógica de "Alterar" (Substituir)
        antigo = input("Nome do produto que deseja alterar: ").lower()
        if antigo in compras:
            indice = compras.index(antigo)
            novo = input("Digite o novo nome do produto: ").lower()
            compras[indice] = novo
            print("Produto alterado com sucesso!")
        else:
            print("Produto não encontrado.")

    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida.")