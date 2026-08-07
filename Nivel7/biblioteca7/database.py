import sqlite3
def conectar():
    conexao = sqlite3.connect("biblioteca7.db")
    cursor = conexao.cursor()
    return conexao, cursor