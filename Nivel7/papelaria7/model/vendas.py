from database import Database

class Compra:
    @staticmethod
    def comprar1(id):
        conexao, cursor = Database.conectar()
        cursor.execute("""SELECT quantidade from produtos WHERE id = ?""", (id,))
        q = cursor.fetchone()[0]
        Database.desconectar(conexao, cursor)
        return q

    @staticmethod
    def comprar2(i, qnt, q, buyer):
        conexao, cursor = Database.conectar()
        cursor.execute("""CREATE TABLE IF NOT EXISTS vendas (id INTEGER PRIMARY KEY AUTOINCREMENT, produto TEXT, marca TEXT, quantidade INTEGER, valor NUMERIC, comprador TEXT)""")
        q = q - qnt
        cursor.execute("""SELECT * from produtos WHERE id = ?""", (i,))
        p = cursor.fetchone()
        valor =  qnt * p[4]
        cursor.execute("""UPDATE produtos SET quantidade = ? WHERE id = ?""", (q, i))
        cursor.execute("""INSERT INTO vendas (produto, marca, quantidade, valor, comprador) VALUES (?,?,?,?,?)""", (p[1], p[2], qnt, valor, buyer))
        conexao.commit()
        Database.desconectar(conexao, cursor)
        return valor

    @staticmethod
    def historico(user):
        conexao, cursor = Database.conectar()
        cursor.execute("""SELECT * from vendas WHERE comprador = ?""", (user,))
        recibo = cursor.fetchall()
        return recibo
    
    @staticmethod
    def recibo():
        conexao, cursor = Database.conectar()
        cursor.execute("""SELECT * from vendas""")
        lista = cursor.fetchall()
        return lista
