from database import Database
import sqlite3
import pandas as pd

class Tarefa:
    def cadastrar(tarefa, prioridade, prazo, situacao):
        conn, cursor = Database.conectar()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, tarefa TEXT, prioridade TEXT, prazo DATE, situacao TEXT, funcionario TEXT, data DATE)""")
        cursor.execute("""INSERT INTO tarefas (tarefa, prioridade, prazo, situacao, funcionario, data) VALUES (?,?,?,?,?,?)""", (tarefa, prioridade, prazo, situacao, None, None))
        conn.commit()
        conn, cursor = Database.desconectar(conn, cursor)

    def realizar(id, login):
        conn, cursor = Database.conectar()
        cursor.execute("""UPDATE tarefas SET situacao = ?, funcionario = ?, data = date('now') WHERE id = ?""", ("Realizada", login, id))
        conn.commit()
        conn, cursor = Database.desconectar(conn, cursor)

    def alterar(id, tarefa, prioridade, prazo, situacao, funcionario, data):
        conn, cursor = Database.conectar()
        cursor.execute("""UPDATE tarefas SET tarefa = ?, prioridade = ?, prazo = ?, situacao = ?, funcionario = ?, data = ? WHERE id = ?""", (tarefa, prioridade, prazo, situacao, funcionario, data, id))
        conn.commit()
        conn, cursor = Database.desconectar(conn, cursor)
        
    def excluir(id):
        conn, cursor = Database.conectar()
        cursor.execute("""DELETE from tarefas WHERE id = ?""", (id,))
        conn.commit()
        conn, cursor = Database.desconectar(conn, cursor)

    def demandar(id, user):
        conn, cursor = Database.conectar()
        cursor.execute("""SELECT usuario from login WHERE id = ?""", (user,))
        lista = cursor.fetchone()[0]
        cursor.execute("""UPDATE tarefas SET funcionario = ? WHERE id = ?""", (lista, id))
        conn.commit()
        conn, cursor = Database.desconectar(conn, cursor)
    
    def exportar():
        try:
            conn = sqlite3.connect("tarefas.db")
            planilha = pd.read_sql("SELECT * from tarefas", conn)
            planilha.to_excel("tarefas.xlsx", index = False)
            conn.close()
            print("Exportação concluída.")
        
        except ModuleNotFoundError:
            print("Instale: pip install openpyxl")

        except Exception as erro:
            print(f"Erro: {erro}")

    def listar():
        conn,cursor = Database.conectar()
        cursor.execute("""SELECT * from tarefas""")
        lista = cursor.fetchall()
        conn, cursor = Database.desconectar(conn, cursor)
        return lista