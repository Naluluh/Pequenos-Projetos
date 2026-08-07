from database import Database

class Usuario:
    @staticmethod
    def listar():
        conn, cursor = Database.conectar()
        cursor.execute("""SELECT * from login""")
        lista = cursor.fetchall()
        conn, cursor = Database.desconectar(conn, cursor )
        return lista
    
    @staticmethod
    def cadastrar(user, senha):
        conn, cursor = Database.conectar()
        cursor.execute("""CREATE TABLE IF NOT EXISTS login 
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       usuario TEXT,
                       senha TEXT)""")
        cursor.execute("""INSERT INTO login (usuario, senha) VALUES (?,?)""",(user, senha))
        conn.commit()
        conn, cursor = Database.desconectar(conn, cursor)

    @staticmethod
    def autenticar(user, senha):
        conn, cursor = Database.conectar()
        cursor.execute("""SELECT * from login WHERE usuario = ? AND senha = ?""", (user, senha))
        login = cursor.fetchone()
        if login:
            return True, user
        else:
            return False, None
        conn, cursor = Database.desconectar(conn, cursor)

    @staticmethod
    def excluir(id):
        conn, cursor = Database.conectar()
        cursor.execute("""DELETE from login WHERE id = ?""", (id,))
        conn.commit()
        conn, cursor = Database.desconectar(conn, cursor )

    @staticmethod
    def alterar(id, usuario, senha):
        conn, cursor = Database.conectar()
        cursor.execute("""UPDATE login SET usuario = ?, senha = ? WHERE id = ?""", (usuario, senha, id))
        conn.commit()
        conn, cursor = Database.desconectar(conn, cursor)

    

    