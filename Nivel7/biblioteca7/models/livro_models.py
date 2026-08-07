from database import conectar

class Livro:
    @staticmethod
    def cadastrar(titulo, autor):
        conexao, cursor = conectar()
        cursor.execute("""CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT, situacao TEXT, leitor TEXT)""")
        cursor.execute("""
            INSERT INTO livros (titulo, autor, situacao) VALUES (?, ?, ?)""", (titulo, autor, "disponível"))
        cursor.close()
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao, cursor = conectar()
        cursor.execute("""SELECT * from livros """)
        lista = cursor.fetchall()
        cursor.close()
        conexao.close()
        return lista
    
    @staticmethod
    def excluir(id):
        conexao, cursor = conectar()
        cursor.execute("""DELETE from livros WHERE id = ?""", (id,))
        cursor.close()
        conexao.commit()
        conexao.close()

    @staticmethod
    def alterar(id, nTitulo, nAutor):
        conexao, cursor = conectar()
        cursor.execute("""UPDATE livros SET titulo = ?, autor = ? WHERE id = ?""", (nTitulo, nAutor, id))
        cursor.close()
        conexao.commit()
        conexao.close()

    def emprestou1():
        conexao, cursor = conectar()
        cursor.execute("""SELECT * from livros WHERE situacao <> "emprestado" """)
        lista = cursor.fetchall()
        cursor.close()
        conexao.commit()
        conexao.close()
        return lista

    def emprestou2(id, usuario):
        conexao, cursor = conectar()
        cursor.execute("""UPDATE livros SET situacao = ?, leitor = ? WHERE id = ?""", ("emprestado", usuario, id))
        cursor.close()
        conexao.commit()
        conexao.close()

    def devolveu1(user):
        conexao, cursor = conectar()
        cursor.execute("""SELECT * from livros WHERE leitor = ? """, (user,))
        lista = cursor.fetchall()
        cursor.close()
        conexao.commit()
        conexao.close()
        return lista

    def devolveu2(id):
        conexao, cursor = conectar()
        cursor.execute("""UPDATE livros SET situacao = ?, leitor = ? WHERE id = ?""", ("disponível", None, id))
        cursor.close()
        conexao.commit()
        conexao.close()


        

