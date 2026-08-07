import sqlite3

def cadastrar():
    livro = str(input("Título: "))
    autor = str(input("Autor: "))

    conexao = sqlite3.connect("biblioteca5.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS biblioteca (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT);
        """)
    cursor.execute("""INSERT INTO biblioteca VALUES (NULL, ?, ?);
""", (livro, autor))
    conexao.commit()
    conexao.close()

def consultar():
    conexao = sqlite3.connect("biblioteca5.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * from biblioteca
    """) 
    result = cursor.fetchall()
    for id, titulo, autor in result:
        print(f"{titulo} - {autor}")

def excluir():
    conexao = sqlite3.connect("biblioteca5.db")
    cursor = conexao.cursor()
    cursor.execute("""
         SELECT * from biblioteca          
    """, )
    lista = cursor.fetchall()
    for id, titulo, autor in lista:
        print(f"{id} - {titulo} - {autor}")
    livro = str(input("Insira o índice do livro que deseja excluir: "))
    cursor.execute("""
        DELETE from biblioteca WHERE id = ?;
    """, (livro,))
    conexao.commit()
    conexao.close()

while True:
    menu = int(input("Escolha\n1 - Cadastrar livro\n2 - Consultar livro\n3 - Excluir livro\n4 - Sair\n"))
    if menu == 1 or menu == 2 or menu == 3 or menu == 4:
        match menu:
            case 1:
                cadastrar()
            case 2:
                consultar()
            case 3:
                excluir()
            case 4:
                print("Saindo...")
                break
    else:
        print("Ação indisponível. Selecione uma opção válida: ") 