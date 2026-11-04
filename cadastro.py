# Sistema de Cadastro de Clientes
clientes = []
print("=== CADASTRO DE CLIENTES ===")
def cadastrar_clientes():
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(cliente)
def menu():
    while True:
        print("\n1 - Cadastrar clientes")
        print("2 - Listar clientes")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_clientes()
        elif opcao == "2":
            listar_clientes()
        elif opcao =="3":
            print("Programa encerrado!")
            break
        else:
            print("Opção invalida!")
menu()
