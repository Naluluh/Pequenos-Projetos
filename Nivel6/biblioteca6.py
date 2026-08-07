import sqlite3

class Livro:
    def __init__(self, titulo, autor, situacao, leitor):
        self.titulo = titulo
        self.autor = autor
        self.situacao = situacao
        self.leitor = leitor
    
    def cadastrarLivro(titulo, autor):
        conexao = sqlite3.connect("biblioteca6.db")
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR, autor VARCHAR, situacao TEXT, leitor TEXT)
        """)
        cursor.execute("""
            INSERT INTO livros (titulo, autor, situacao, leitor) VALUES (?,?,?, NULL)""", (titulo, autor, "disponível"))
        conexao.commit()
        conexao.close()

    def listar():
        conexao = sqlite3.connect("biblioteca6.db")
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR, autor VARCHAR, situacao TEXT, leitor TEXT)
        """)
        cursor.execute("""
            SELECT * from livros
        """)
        res = cursor.fetchall()
        for id, titulo, autor, situacao, leitor in res:
            print(f"{titulo} - {autor} ({situacao})")
        conexao.close()

    def excluirLivro():
        conexao = sqlite3.connect("biblioteca6.db")
        cursor = conexao.cursor()
        conexao = sqlite3.connect("biblioteca6.db")
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * from livros WHERE situacao <> "emprestado"
            """)
        log = cursor.fetchall()
        for id, titulo, autor, situacao, leitor in log:
            print(f"{id}. {titulo} - {autor}")
        ind = input("Selecione o índice do livro que deseja excluir: ")
        cursor.execute("""
            DELETE from livros WHERE id = ?""", (ind,))
        conexao.commit()
        conexao.close()

class Usuario:

    def cadastrarUser(login, senha):
        conexao = sqlite3.connect("biblioteca6.db")
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario VARCHAR, senha VARCHAR)
        """)
        cursor.execute("""
            INSERT INTO login(usuario, senha) VALUES (?,?)""", (login, senha,))
        conexao.commit()
        conexao.close()
        
    def autenticar(loginD, senhaD):
        conexao = sqlite3.connect("biblioteca6.db")
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario VARCHAR, senha VARCHAR)
        """)
        cursor.execute("""
            SELECT * from login
            """)
        log = cursor.fetchall()
        p = 0
        for id, usuario, senha in log:
            if usuario == loginD and senha == senhaD:
                p = 1
            else:
                p += 0
        if p == 1: 
            print("Login realizado com sucesso.")
            return True, loginD
        else:
            print("Usuário ou senha incorretos.")
            return False, None    

    def excluirUser():
        conexao = sqlite3.connect("biblioteca6.db")
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * from login """)
        log = cursor.fetchall()
        for id, usuario, senha in log:
            print(f"{id} - {usuario}")
        ind = input("Selecione o índice do usuário que deseja excluir: ")
        cursor.execute("""
            DELETE from login WHERE id = ?""", (ind,))
        conexao.commit()
        conexao.close()

class Emprestimo:

    def emprestar(usuario):
        conexao = sqlite3.connect("biblioteca6.db")
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * from livros WHERE situacao <> "emprestado"
            """)
        log = cursor.fetchall()
        for id, titulo, autor, situacao, leitor in log:
            print(f"{id} - {titulo}\n{autor}")
        ind = int(input("Selecione o índice do livro: "))
        cursor.execute("""
            UPDATE livros SET situacao = "emprestado", leitor = ? WHERE id =?                       
    """, (usuario, ind,))
        conexao.commit()
        conexao.close()
        print("Livro emprestado com sucesso.")
    
    def devolver(usuario):
        conexao = sqlite3.connect("biblioteca6.db")
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * from livros WHERE leitor = ? AND situacao = ?
            """, (usuario, "emprestado",))
        log = cursor.fetchall()
        for id, titulo, autor, situacao, leitor in log:
            print(f"{id} - {titulo}\n{autor}")
        ind = int(input("Selecione o índice do livro: "))
        cursor.execute("""
            UPDATE livros SET situacao = "disponível", leitor = NULL WHERE id =?                       
    """, (ind,))
        conexao.commit()
        conexao.close()
        print("Livro devolvido com sucesso.")

while True:
    menu1 = int(input("Escolha:\n1 - Criar conta\n2 - Entrar\n3 - Excluir Conta\n4 - Sair\n"))
    if menu1 == 1 or menu1 == 2 or menu1 == 3 or menu1 == 4:
        match menu1:
            case 1:
                user = str(input("Usuário: "))
                password = (str(input("Senha: ")))
                Usuario.cadastrarUser(user, password)
            case 2:
                user = str(input("Usuário: "))
                password = str(input("Senha: "))
                login = Usuario.autenticar(user, password)
                while login[0] == True:
                    menu2 = int(input("Escolha:\n1 - Cadastrar Livro\n2 - Ver Livros\n3 - Excluir Livro\n4 - Empréstimo de Livros\n5 - Devolução de livro\n6 - Sair\n"))
                    if menu2 == 1 or menu2 == 2 or menu2 == 3 or menu2 == 4 or menu2 == 5 or menu2 == 6:
                        match menu2:
                            case 1:
                                t = str(input("Título: "))
                                a = str(input("Autor: "))
                                Livro.cadastrarLivro(t, a)
                            case 2:
                                Livro.listar()
                            case 3:
                                Livro.excluirLivro()
                            case 4:
                                Emprestimo.emprestar(login[1])
                            case 5:
                                Emprestimo.devolver(login[1])
                            case 6:
                                print("Saindo...")
                                break
                    else: 
                        print("Selecione uma opção válida.")
            case 3:
                Usuario.excluirUser()
            case 4:
                print("Saindo...")
                break
    else:
        print("Opção inválida. Tente novamente.")