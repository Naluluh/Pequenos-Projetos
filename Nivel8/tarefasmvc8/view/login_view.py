from controller.usuario_controller import User
from view.login_admin import admin_menu
from view.login_funcionario import funcionario_menu

def listagem():
    print("=== USUÁRIOS ===")
    lista = User.lista()
    print("-"*22)
    print(f"{'ID':<5}|{'USUÁRIO':<15}|")
    print("-"*22)
    for id, usuario, senha in lista:
        print(f"{id:<5}|{usuario:<15}|")
    print("-"*22)
    
def pagina_inicial():
    while True:
        menu = int(input("1 - Cadastrar usuário\n2 - Fazer login\n3 - Listar usuários\n4 - Excluir usuário\n5 - Alterar usuário\n6 - Sair\n"))
        e = [1,2,3,4,5,6]
        if menu in e:
            match menu:
                case 1:
                    print("=== CADASTRANDO USUÁRIO ===")
                    user = str(input("Usuário: "))
                    senha = str(input("Senha: "))
                    User.cadastro(user, senha)
                    print("Cadastro feito com sucesso.")

                case 2:
                    print("=== ENTRANDO NA CONTA ===")
                    user = str(input("Usuário: "))
                    senha = str(input("Senha: "))
                    login = User.autenticacao(user, senha)
                    if login[0] == True:
                        if login[1] == 'admin':
                            admin_menu(login)
                        else: 
                            funcionario_menu(login)
                    else:
                        print("Usuário ou senha incorretos.")

                case 3:
                    listagem()

                case 4:
                    listagem()
                    id = int(input("ID: "))
                    User.exclusao(id)
                    print(f"Usuário (id: {id}) excluído com sucesso.")

                case 5:
                    listagem()
                    id = int(input("ID: "))
                    usuario = str(input("Usuário: "))
                    senha = str(input("Senha: "))
                    User.alteracao(id, usuario, senha)
                    print(f"Conta alterada com sucesso.")

                case 6:
                    print("Encerrando o programa...")
                    break
        else:
            print("Opção inválida. Tente novamente.")        