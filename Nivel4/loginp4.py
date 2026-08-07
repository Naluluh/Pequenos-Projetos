def cadastrar():
    nome = str(input("Insira o nome: "))
    with open("login4.txt", "r", encoding="utf-8") as lusuarios:
        linhas = lusuarios.readlines()
        s = linhas.count(f"Usuário: {nome}\n") 

        while s != 0:
            print("Login já existente. Tente novamente com um usuário disponível: ")
            nome = str(input("Insira o nome: "))
    senha = str(input("Insira a senha: "))
    print("Conta cadastrada com sucesso.")
            
    with open ("login4.txt", "a", encoding="utf-8") as lusuarios:
        lusuarios.write(f"Usuário: {nome}\nSenha: {senha}\n")
        lusuarios.write()
    s = 0

def login():
    p = 0
    print("Entre com seu login")
    nomeL = str(input("Nome: "))
    senhaL = str(input("Senha: "))
    with open("login4.txt", "r", encoding="utf-8") as lusuarios:
        linhas = lusuarios.readlines()

    for n in range (0, len(linhas), 3):
        if linhas[n] == f"Usuário: {nomeL}\n" and linhas[n+1] == f"Senha: {senhaL}\n":
            p = 1
        else:
            pass
    if p == 1:
        print("Login efetuado com sucesso.")
    else: 
        print("Login ou senha incorretos.")

def listar():
    with open("login4.txt", "r", encoding="utf-8") as lusuarios:
        linhas = lusuarios.readlines()

    for i in range(0, len(linhas), 3):
        print(f"Índice {i//3}")
        print(linhas[i], end="")
        print(linhas[i+1], end="")
        print()

def atualizar():
    with open("login4.txt", "r", encoding="utf-8") as lusuarios:
        linhas = lusuarios.readlines()
        quantidade = len(linhas)+1//3

    for i in range(0, len(linhas), 3):
        print(f"Índice {i//3}")
        print(linhas[i], end="")
        print(linhas[i+1], end="")
        print()

    mudar = int(input("Insira o índice que deseja que fazer a alteração: "))
    while mudar < 0 or mudar >= quantidade:
        mudar = int(input("Índice inválido. Insira novamente: "))
    ss = str(input(f"Insira a nova senha de {linhas[mudar*3]} "))
    linhas[(mudar*3)+1] = (f"Senha: {ss}\n")

    with open("login4.txt", "w", encoding="utf-8") as lusuarios:
        lusuarios.writelines(linhas)

    

def excluir():
    with open("login4.txt", "r", encoding="utf-8") as lusuarios:
        linhas = lusuarios.readlines()
        quantidade = len(linhas)+1 // 3
        
    for i in range(0, len(linhas), 3):
        print(f"Índice {i//3}")
        print(linhas[i], end="")
        print(linhas[i+1], end="")
        print()

    deleta = int(input("Insira o índice que deseja que excluir: "))
    while deleta < 0 or deleta >= quantidade:
        deleta = int(input("Índice inválido. Insira novamente: "))
    
    inicio = deleta*3
    del linhas[inicio:inicio + 3]

    with open ("login4.txt", "w", encoding="utf-8") as lusuarios:
        lusuarios.writelines(linhas)


while True:
    menu = int(input("Escolha:\n1 - Cadastrar login\n2 - Fazer login\n3 - Atualizar senha\n4 - Excluir usuário\n5 - Lista de contas\n6 - Sair\n"))
    if menu == 1 or menu == 2 or menu == 3 or menu == 4 or menu == 5 or menu == 6:
        match menu:
            case 1:
                cadastrar()
            case 2:
                login()
            case 3:
                atualizar()
            case 4: 
                excluir()
            case 5:
                listar()
            case 6:
                print("Saindo...")
                break
    else:
        print("Opção inválida. Tente novamente.")