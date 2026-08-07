from database import Database

class Produto:
    @staticmethod
    def cadastrar(p, m, qnt, preco):
        conexao, cursor = Database.conectar()
        cursor.execute("""CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, produto TEXT, marca TEXT, quantidade INTEGER, preco NUMERIC)""")
        cursor.execute("""INSERT INTO produtos (produto, marca, quantidade, preco) VALUES (?,?,?,?)""", (p, m, qnt, preco))
        conexao.commit()
        Database.desconectar(conexao, cursor)

    @staticmethod
    def listar():
        conexao, cursor = Database.conectar()
        cursor.execute("""SELECT * from produtos""")
        lista = cursor.fetchall()
        return lista
    
    @staticmethod
    def alterar(id, p, m, qnt, preco):
        conexao, cursor = Database.conectar()
        cursor.execute("""UPDATE produtos SET produto = ?, marca = ?, quantidade = ?, preco = ? WHERE id = ?""", (p, m, qnt, preco, id))
        conexao.commit()
        Database.desconectar(conexao, cursor)

    @staticmethod
    def excluir(id):
        conexao, cursor = Database.conectar()
        cursor.execute("""DELETE from produtos WHERE id = ?""", (id,))
        conexao.commit()
        Database.desconectar(conexao, cursor)