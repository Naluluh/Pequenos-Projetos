import sqlite3

class Database:

    @staticmethod
    def conectar():
        conexao = sqlite3.connect("papelaria7.db")
        cursor = conexao.cursor()
        return conexao, cursor

    @staticmethod
    def desconectar(conexao, cursor):
        cursor.close()
        conexao.close()