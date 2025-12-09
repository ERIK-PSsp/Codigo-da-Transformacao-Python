# -------------------------
# Função: Lista de compras
# -------------------------
def lista_de_compras():
    lista = []
    
    print("Bem-vindo à sua Lista de Compras!")

    while True:
        print("\n--- LISTA DE COMPRAS ---")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Ver lista")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            item = input("Digite o item para adicionar: ")
            lista.append(item)
            print(f"'{item}' foi adicionado.")

        elif opcao == "2":
            item = input("Digite o item para remover: ")
            if item in lista:
                lista.remove(item)
                print(f"'{item}' removido.")
            else:
                print("Item não encontrado.")

        elif opcao == "3":
            print("\nLista atual:")
            if not lista:
                print("A lista está vazia.")
            else:
                for i, item in enumerate(lista, start=1):
                    print(f"{i}. {item}")

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ------------------------------------
# Função: Dicionário com dados de aluno
# ------------------------------------
def dados_aluno():
    aluno = {}
    
    print("Bem-vindo ao cadastro de dados do aluno!")

    while True:
        print("\n--- DADOS DO ALUNO ---")
        print("1 - Adicionar dados")
        print("2 - Excluir dados")
        print("3 - Mostrar dados atuais")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            idade = input("Idade: ")
            notas = input("Notas (separe por vírgula): ")

            aluno["nome"] = nome
            aluno["idade"] = idade
            aluno["notas"] = [float(n) for n in notas.split(",")]

            print("Dados adicionados com sucesso!")

        elif opcao == "2":
            aluno.clear()
            print("Todos os dados foram excluídos.")

        elif opcao == "3":
            if aluno:
                print("\nDados atuais do aluno:")
                print("Nome:", aluno["nome"])
                print("Idade:", aluno["idade"])
                print("Notas:", aluno["notas"])
            else:
                print("Nenhum dado cadastrado.")

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ----------------------------------------------
# Função: Separar números pares e ímpares
# ----------------------------------------------
def separar_pares_impares():
    print("\n--- SEPARAR PARES E ÍMPARES ---")
    print("digite números para separar em pares e ímpares. O resultado será exibido ao final, quando você digitar 'sair'.")

    numeros = []
    while True:
        entrada = input("Digite um número (ou 'sair' para terminar): ")

        if entrada.lower() == "sair":
            break

        if entrada.isdigit():
            numeros.append(int(entrada))
        else:
            print("Digite apenas números ou 'sair'.")

    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]

    print("\nNúmeros pares:", pares)
    print("Números ímpares:", impares)


# -------------------------
# Menu principal do programa
# -------------------------
while True:
    print("\n==== MENU PRINCIPAL ====")
    print("1 - Lista de compras")
    print("2 - Dados do aluno")
    print("3 - Separar números pares e ímpares")
    print("0 - Encerrar programa")

    escolha = input("Escolha uma função: ")

    if escolha == "1":
        lista_de_compras()

    elif escolha == "2":
        dados_aluno()

    elif escolha == "3":
        separar_pares_impares()

    elif escolha == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida! Tente novamente.")
