import sqlite3 

def cadastrar():
    user = str(input("Crie um usuário: "))
    password = str(input("Crie uma senha: "))

    conexao = sqlite3.connect("login5.db")
    cursor = conexao.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS logins (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT NOT NULL, senha TEXT)
    """)

    cursor.execute("""
        INSERT INTO logins (usuario, senha) values (?,?)
    """, (user, password))

    cursor.close()
    conexao.commit()
    conexao.close()
    return 

def login():
    user = str(input("Insira o usuário: "))
    password = str(input("Insira a senha: "))
    conexao = sqlite3.connect("login5.db")
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT * from logins WHERE usuario=? AND senha=?
    """, (user, password))
    result = cursor.fetchone()
    if result:
        print("Login efetuado com sucesso")
    else:
        print("Login ou senha incorretos.")
    
def listar():
    conexao = sqlite3.connect("login5.db")
    cursor = conexao.cursor()
    cursor.execute(
        """
        SELECT usuario from logins
    """)
    lista = cursor.fetchall()
    print("\nUSUÁRIOS")
    for (usuario,) in lista:
        print(usuario)
    print()

while True:
    menu = int(input("Escolha:\n1 - Cadastrar\n2 - Login\n3 - Listar usuários\n4 - Sair\n"))
    if menu == 1 or menu == 2 or menu or menu == 3 or menu == 4:
        match menu:
            case 1:
                cadastrar()
            case 2:
                login()
            case 3:
                listar()
            case 4:
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
    else:
        print("Opção inválida. Tente novamente.")


