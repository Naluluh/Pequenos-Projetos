from database import conectar

class Usuario:
    @staticmethod    
    def criar(usuario, senha):
        conexao, cursor = conectar()
        cursor.execute("""CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT, senha TEXT)""")
        cursor.execute("""INSERT INTO login (usuario, senha) VALUES (?,?)""", (usuario, senha))
        cursor.close()
        conexao.commit()
        conexao.close()

    @staticmethod    
    def autenticar(usuario, senha):
        conexao, cursor = conectar()
        cursor.execute("""SELECT * from login WHERE usuario = ? AND senha = ?""", (usuario, senha))
        user = cursor.fetchone()
        return user
        
    def excluir(id):
        conexao, cursor = conectar()
        cursor.execute("""DELETE from login WHERE id = ?""", (id,))
        cursor.close()
        conexao.commit()
        conexao.close()

    def alterar(id, nUser, nPassword):
        conexao, cursor = conectar()
        cursor.execute("""UPDATE login SET usuario = ?, senha = ? WHERE id = ?""", (nUser, nPassword, id))
        cursor.close()
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao, cursor = conectar()
        cursor.execute("""SELECT * from login """)
        lista = cursor.fetchall()
        cursor.close()
        conexao.close()
        return lista    



