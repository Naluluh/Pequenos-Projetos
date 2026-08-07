import sqlite3
class Database:
    def conectar():
        conn = sqlite3.connect("tarefas.db")
        cursor = conn.cursor()
        return conn, cursor

    def desconectar(conn, cursor):
        cursor.close()
        conn.close()
        return cursor, conn