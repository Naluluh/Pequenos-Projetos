from view.menu_admin import menu2
from view.menu_compra import compra
from controller.login_controller import UsuarioC

def menu():
    while True:
        menu1 = int(input("1 - Cadastrar conta\n2 - Fazer login\n3 - Listar usuários\n4 - Excluir usuário\n5 - Alterar conta\n6 - Sair\n"))
        e = [1,2,3,4,5,6]
        if menu1 in e:
            match menu1:
                case 1:
                    user = str(input("Usuário: "))
                    password = str(input("Senha: "))
                    UsuarioC.cadastrar(user, password)

                case 2:
                    user = str(input("Usuário: "))
                    password = str(input("Senha: "))
                    login = UsuarioC.autenticar(user, password)
                    if login[0] == True:
                        if login[1] == 'admin':
                            menu2()
                        else:
                            compra(login)

                case 3:
                    lista = UsuarioC.listar()
                    print("-" * 28)
                    print(f"{'ID':<6}|{'USUÁRIO':<20}|")
                    print("-" * 28)
                    for id, usuario, senha in lista:
                        print(f"{id:<6}|{usuario:<20}|")
                
                case 4:
                    lista = UsuarioC.listar()
                    for id, usuario, senha in lista:
                        print(f"{id} - {usuario}")
                    id = int(input("Índice: "))
                    UsuarioC.excluir(id)

                case 5:
                    lista = UsuarioC.listar()
                    for id, usuario, senha in lista:
                        print(f"{id} - {usuario}")
                    id = int(input("Índice: "))
                    user = str(input("Novo Usuário: "))
                    password = str(input("Nova Senha: "))
                    UsuarioC.alterar(id, user, password)

                case 6:
                    print("Encerrando programa...")
                    break   

        else:
            print("Opção inválida. Tente novamente.")         