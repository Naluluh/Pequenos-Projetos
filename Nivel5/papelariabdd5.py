import sqlite3

def create():
    produto = str(input("Produto: "))
    marca = str(input("Marca: "))
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    conexao = sqlite3.connect("papelaria5.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, produto TEXT, marca TEXT, quantidade NUMERIC, preco NUMERIC)    
    """)
    cursor.execute(
        """INSERT INTO produtos (id, produto, marca, quantidade, preco) VALUES (NULL,?,?,?,?)""",
        (produto, marca, quantidade, preco))
    
    conexao.commit()
    conexao.close()

def read():
    conexao = sqlite3.connect("papelaria5.db")
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * from produtos""")
    lista = cursor.fetchall()
    for id, produto, marca, quantidade, preco, in lista:
        print(f"{id} - {produto}\nMarca: {marca}\nQuantidade: {quantidade}\nPreço: {preco}")

def update():
    conexao = sqlite3.connect("papelaria5.db")
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * from produtos""")
    lista = cursor.fetchall()
    for id, produto, marca, quantidade, preco in lista:
        print(f"{id} - {produto}")
    id = int(input("Insira o índice do produto que deseja alterar: "))
    produto = str(input("Novo produto: "))
    marca = str(input("Nova marca: "))
    quantidade = int(input("Nova quantidade: "))
    preco = float(input("Novo preço: "))
    cursor.execute("""
        UPDATE produtos SET produto = ?, marca = ?, quantidade = ?, preco = ? WHERE id = ?""", (produto, marca, quantidade, preco, id))
    conexao.commit()
    conexao.close()
    print("Item atualizado com sucesso.")

def delete():
    conexao = sqlite3.connect("papelaria5.db")
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * from produtos""")
    lista = cursor.fetchall()
    for id, produto, marca, quantidade, preco in lista:
        print(f"{id} - {produto}")
    id = int(input("Insira o índice do produto que deseja excluir: "))
    cursor.execute("""
        DELETE from produtos WHERE id = ?
    """, (id,))
    print("Item excluído com sucesso.")
    conexao.commit()
    conexao.close()

while True:
    menu = int(input("Escolha:\n1 - Cadastrar\n2 - Ler\n3 - Atualizar\n4 - Excluir\n5 - Sair\n"))
    if menu == 1 or menu == 2 or menu == 3 or menu == 4 or menu == 5:
        match menu:
            case 1:
                create()
            case 2:
                read()
            case 3:
                update()
            case 4:
                delete()
            case 5:
                print("Saindo...")
                break
    else:
        print("Escolha inválida. Tente novamente.")
