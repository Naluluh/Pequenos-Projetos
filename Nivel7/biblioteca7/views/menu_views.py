from controllers.usuario_controllers import Usuario_c
from controllers.livro_controllers import Livro_c  

def lista_user():
    lista = Usuario_c.listar()
    for id, usuario, senha in lista:
        print(f"{id} - {usuario}")

def lista_book():
    lista = Livro_c.listar()
    for id, titulo, autor, situacao, leitor in lista:
        print(f"{id} - {titulo} | {autor} ({situacao})")

while True:
    menu1 = int(input("Escolha:\n1 - Criar conta\n2 - Entrar\n3 - Excluir conta\n4 - Listar usuários\n5 - Alterar usuário\n6 - Sair\n"))
    e = [1, 2, 3, 4, 5, 6]
    if menu1 in e:
        match menu1:
            case 1:
                user = str(input("Usuário: "))
                password = str(input("Senha: "))
                Usuario_c.criar(user, password)
            case 2:
                user = str(input("Usuário: "))
                password = str(input("Senha: "))
                login = Usuario_c.autenticar(user, password)
                if login[0] == True:
                    while True:
                        if login[1] == 'admin':
                            menu2 = int(input("Escolha:\n1 - Cadastrar livro\n2 - Excluir livro\n3 - Listar livros\n4 - Alterar livro\n5 - Sair\n"))
                            e = [1, 2, 3, 4, 5]
                            if menu2 in e:
                                match menu2:
                                    case 1:
                                        title = str(input("Título: "))
                                        author = str(input("Autor: "))
                                        Livro_c.criar(title, author)
                                    
                                    case 2:
                                        lista_book()
                                        id = int(input("Índice: "))
                                        Livro_c.excluir(id)

                                    case 3:
                                        lista_book()

                                    case 4:
                                        lista_book()
                                        id = int(input("Índice: "))
                                        ntitle = str(input("Novo Título: "))
                                        nauthor = str(input("Novo Autor: "))
                                        Livro_c.alterar(id, ntitle, nauthor)

                                    case 5:
                                        print("Saindo da conta...")
                                        break
                            else:
                                print("Opção inválida. Tente novamente.")
                        else:
                            menu2 = int(input("Escolha:\n1 - Empréstimo\n2 - Devolução\n3 - Listar livros\n4 - Sair\n"))
                            e = [1, 2, 3, 4]
                            if menu2 in e:
                                match menu2:
                                    case 1:
                                        lista = Livro_c.emprestar1()
                                        for id, titulo, autor, situacao, leitor in lista:
                                            print(f"{id} - {titulo} | {autor} ({situacao})")
                                        id = int(input("Índice: "))
                                        Livro_c.emprestar2(id, login[1])
                                    
                                    case 2:
                                        lista = Livro_c.devolver1(login[1])
                                        for id, titulo, autor, situacao, leitor in lista:
                                            print(f"{id} - {titulo} | {autor} ({situacao})")
                                        id = int(input("Índice: "))
                                        Livro_c.devolver2(id)

                                    case 3:
                                        lista = Livro_c.listar()
                                        for id, titulo, autor, situacao, leitor in lista:
                                            print(f"{id} - {titulo} | {autor} ({situacao})")

                                    case 4:
                                        print("Saindo da conta...")
                                        break
                                        
                            else:
                                print("Opção inválida. Tente novamente.")

            case 3:
                lista_user()
                id = int(input("Índice: "))
                Usuario_c.excluir(id)
            case 4:
                lista_user()

            case 5:
                lista_user()
                id = int(input("Índice: "))
                nu = str(input("Novo Usuário: "))
                ns = str(input("Nova Senha: "))
                Usuario_c.alterar(id, nu, ns)

            case 6:
                print("Encerrando o programa...")
                break
    else:
        print("Opção inválida. Tente novamente.")
            