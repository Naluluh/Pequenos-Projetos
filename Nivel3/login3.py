logs = {}

def cadastrar():
    nome = str(input("Insira o nome: "))
    senha = str(input("Insira a senha: "))
    logs[nome] = senha

def login():
    print("Entre com seu login")
    nomeL = str(input("Nome: "))
    senhaL = str(input("Senha: "))
    if nomeL in logs and logs[nomeL] == senhaL:
        print("Login efetuado com sucesso.")
    else:
        print("Login ou senha incorretos.")


while True:
    menu = int(input("Escolha:\n1 - Cadastrar login\n2 - Fazer login\n3 - Sair\n"))
    if menu == 1 or menu == 2 or menu == 3:
        match menu:
            case 1:
                cadastrar()
            case 2:
                login()
            case 3:
                print("Saindo...")
                break
    else:
        print("Opção inválida. Encerrando...")
        break