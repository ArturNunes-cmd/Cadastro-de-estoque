import pandas as pd
estoque = []

def mostrar_pilha(estoque):
    print("\n📦 ---- Pilha de produtos ---- 📦")
    for i, produto in enumerate(reversed(estoque), 1):
        print(f"{i} - Código: {produto[0]}, Descrição: {produto[1]}, Categoria: {produto[2]}, Unidade: {produto[3]}")


while True:
    print("\nMENU".center(15))
    print("1 - Cadastrar produto")
    print("2 - Exportar para Excel")
    print("3 - Sair")

    opcao = int(input("Digite a opção desejada:"))

    if opcao == 1:
        print("\nCadastrar produto")
        continuar = "S"
        while continuar == "S":
            codigo = int(input("Digite o código do produto:"))
            descricao = input("Digite a descrição do produto:").upper()
            categoria = input("Digite a categoria do produto(matéria-prima ou produto acabado):").upper()
            unidade = input("Digite a unidade de medida(Kg,g,uni):").upper()

            codigos_existentes = [produto[0] for produto in estoque]
            if codigo in codigos_existentes:
                print("Esse produto já foi cadastrado ⚠️⚠️!!")
            else:
                produto = [codigo, descricao, categoria, unidade]
                estoque.append(produto)
                print("Seu produto foi cadastrado com sucesso😊!")
                mostrar_pilha(estoque)
            
            continuar = input("Deseja adicionar outro produto(S/N): ").upper()
            if continuar == "N":
                break

    elif opcao == 2:
        print("\nExportar dados")
        if not estoque:
            print("Nenhum produto para exportar.")
        else:
            formato = input("Deseja exportar em Excel (digite 'excel') ou CSV (digite 'csv')? ").strip().lower()
            df = pd.DataFrame(estoque, columns=["Código", "Descrição do item", "Categoria", "Unidade"])

            if formato == "excel":
                df.to_excel("estoque.xlsx", index=False, )
                print("✅ Dados exportados para 'estoque.xlsx'.")
            elif formato == "csv":
                df.to_csv("estoque.csv", index=False, encoding='utf-8-sig') 
                print("✅ Dados exportados para 'estoque.csv'.")
            else:
                print("⚠️Formato inválido. Nenhum arquivo foi criado.")

    elif opcao == 3:
        print("\nSair")
        break
    else:
        print("Opção inválida! Tente novamente.")