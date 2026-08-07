from database import Database

class Usuario:
    @staticmethod
    def cadastrar(u, s):
        conexao, cursor = Database.conectar()
        cursor.execute("""CREATE TABLE IF NOT EXISTS login(id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT, senha TEXT)""")
        cursor.execute("""INSERT INTO login (usuario, senha) VALUES (?,?)""", (u, s))
        conexao.commit()
        Database.desconectar(conexao, cursor)

    @staticmethod
    def autenticar(u, s):
        conexao, cursor = Database.conectar()
        cursor.execute("""SELECT * from login WHERE usuario = ? AND senha = ?""", (u, s))
        usuario = cursor.fetchone()
        return usuario
    
    @staticmethod
    def listar():
        conexao, cursor = Database.conectar()
        cursor.execute("""SELECT * from login""")
        lista = cursor.fetchall()
        return lista
    
    @staticmethod
    def alterar(id, u, s):
        conexao, cursor = Database.conectar()
        cursor.execute("""UPDATE login SET usuario = ?, senha = ? WHERE id = ?""", (u, s, id))
        conexao.commit()
        Database.desconectar(conexao, cursor)

    @staticmethod
    def excluir(id):
        conexao, cursor = Database.conectar()
        cursor.execute("""DELETE from login WHERE id = ?""", (id,))
        conexao.commit()
        Database.desconectar(conexao, cursor)