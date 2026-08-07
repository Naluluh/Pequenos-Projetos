import sqlite3

def conn():
    conexao = sqlite3.connect("papelaria6.db")
    cursor = conexao.cursor()
    return conexao, cursor

class Produto:
    @staticmethod
    def cadastrarP():
        produto = str(input("PRODUTO: "))
        preco = float(input("PREÇO: "))
        quant = int(input("QUANTIDADE: "))
        conexao, cursor = conn()
        cursor.execute("""
    """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, produto TEXT, preco NUMERIC, quantidade NUMERIC)
    """)
        cursor.execute("""
        INSERT INTO produtos (produto, preco, quantidade) VALUES (?,?,?)""", (produto, preco, quant))
        conexao.commit()
        cursor.close()
        conexao.close()
        
    @staticmethod
    def listarP():
        conexao, cursor = conn()
        cursor.execute("""
            SELECT * from produtos
    """)
        lista = cursor.fetchall()
        print("PRODUTO\t|PREÇO\t|QUANTIDADE")
        for id, produto, preco, quantidade in lista:
            print(f"{produto}\t|{preco}\t|{quantidade}")
        conexao.commit()
        cursor.close()
        conexao.close()
        
    @staticmethod
    def excluirP():
        conexao, cursor = conn()
        cursor.execute("""
            SELECT * from produtos
    """)
        lista = cursor.fetchall()
        print("ID\t|PRODUTO\t|PREÇO\t|QUANTIDADE")
        for id, produto, preco, quantidade in lista:
            print(f"{id}\t|{produto}\t|{preco}\t|{quantidade}")
        conexao.commit()
        ind = int(input("ÍNDICE: "))
        cursor.execute("""
            DELETE from produtos WHERE id = ?""", (ind,))
        conexao.commit()
        cursor.close()
        conexao.close()
        
    @staticmethod
    def alterarP():
        conexao, cursor = conn()
        cursor.execute("""
            SELECT * from produtos
    """)
        lista = cursor.fetchall()
        print("ID\t|PRODUTO\t|PREÇO\t|QUANTIDADE")
        for id, produto, preco, quantidade in lista:
            print(f"{id}\t|{produto}\t|{preco}\t|{quantidade}")
        conexao.commit()
        ind = int(input("ÍNDICE: "))
        produto = str(input("NOVO PRODUTO: "))
        preco = float(input("NOVO PREÇO: "))
        quant = int(input("NOVA QUANTIDADE: "))
        cursor.execute("""
            UPDATE produtos SET produto = ?, preco = ?, quantidade = ? WHERE id = ?""", (produto, preco, quant, ind))
        conexao.commit()
        cursor.close()
        conexao.close()
        
class Cliente:
    @staticmethod
    def cadastrarC():
        user = str(input("USUÁRIO: "))
        password = str(input("SENHA: "))
        conexao, cursor = conn()
        cursor.execute("""
    """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logins (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario VARCHAR, senha VARCHAR)""")
        cursor.execute("""
            INSERT INTO logins (usuario, senha) VALUES (?,?)""", (user, password))
        conexao.commit()
        cursor.close()
        conexao.close()
        
    @staticmethod
    def listarC():
        conexao, cursor = conn()
        cursor.execute("""
            SELECT * from logins
    """)
        lista = cursor.fetchall()
        print("USUÁRIOS")
        for id, usuario, senha in lista:
            print(f"{usuario}")
        conexao.commit()
        cursor.close()
        conexao.close()
        
    @staticmethod
    def excluirC():
        conexao, cursor = conn()
        cursor.execute("""
            SELECT * from logins
    """)
        lista = cursor.fetchall()
        print("ID\t|USUÁRIO")
        for id, usuario, senha in lista:
            print(f"{id}\t|{usuario}")
        conexao.commit()
        ind = int(input("ÍNDICE: "))
        cursor.execute("""
            DELETE from logins WHERE id = ?""", (ind,))
        conexao.commit()
        cursor.close()
        conexao.close()
        

    @staticmethod
    def autenticar():
        conexao, cursor = conn()
        user = str(input("USUÁRIO: "))
        password = str(input("SENHA: "))
        cursor.execute("""
            SELECT * from logins WHERE usuario = ? AND senha = ?""", (user, password))
        log = cursor.fetchone()
        conexao.commit()
        cursor.close()
        conexao.close()
        if log == None:
            print("Usuário ou senha incorretos.")
            return False
        else:
            print("Login efetuado com sucesso.")
            return True, user
        
    @staticmethod    
    def alterarC():
        conexao, cursor = conn()
        cursor.execute("""
            SELECT * from logins
    """)
        lista = cursor.fetchall()
        print("ID\t|USUÁRIO\t")
        for id, usuario, senha in lista:
            print(f"{id}\t|{usuario}\t")
        conexao.commit()
        ind = int(input("ÍNDICE: "))
        user = str(input("NOVO USUÁRIO: "))
        password = str(input("NOVA SENHA: "))
        cursor.execute("""
            UPDATE logins SET usuario = ?, senha = ? WHERE id = ? """, (user, password, ind))
        conexao.commit()
        cursor.close()
        conexao.close()
        
def calc(quant, prod):
    conexao, cursor = conn()
    cursor.execute("""SELECT preco FROM produtos WHERE produto = ?""", (prod,))
    preco = cursor.fetchone()[0]
    valor = quant * preco
    conexao.commit()
    cursor.close()
    conexao.close()
    return valor


class Venda:
    @staticmethod
    def recibo(usuario):
        conexao, cursor = conn()
        cursor.execute("""
            SELECT * from produtos
    """)
        lista = cursor.fetchall()
        print("ID\t|PRODUTO\t|PREÇO\t|QUANTIDADE")
        for id, produto, preco, quantidade in lista:
            print(f"{id}\t|{produto}\t|{preco}\t|{quantidade}")
        conexao.commit()
        ind = int(input("ÍNDICE: "))
        cursor.execute("""
            SELECT quantidade from produtos WHERE id = ?""", (ind,))
        q = cursor.fetchone()[0]
        quant = int(input("QUANTIDADE: "))
        while quant > q:
            quant = int(input(f"Escolha uma quantidade menor (máx.: {q}):\n"))
        cursor.execute("""
            SELECT produto from produtos WHERE id = ?""", (ind,))
        prod = cursor.fetchone()[0]
        cursor.execute("""UPDATE produtos SET quantidade = quantidade - ? WHERE id = ? """, (quant, ind))
        valor = calc(quant, prod)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (id INTEGER PRIMARY KEY AUTOINCREMENT, comprador VARCHAR, produto TEXT, quantidade NUMERIC, valor NUMERIC)""")
        cursor.execute("""
            INSERT INTO vendas (comprador, produto, quantidade, valor) VALUES (?,?,?,?)""", (usuario, prod, quant, valor))
        conexao.commit()
        cursor.close()
        conexao.close()
        print(f"VALOR: {valor:.2f}")

    def total():
        conexao, cursor = conn()
        cursor.execute("""
            SELECT * from vendas
    """)
        lista = cursor.fetchall()
        print("ID\t|COMPRADOR\t|PRODUTO\t|QUANTIDADE|TOTAL")
        for id, comprador, produto, quantidade, valor in lista:
            print(f"{id}\t|{comprador}\t|{produto}\t|{quantidade}\t{valor}")
        cursor.close()
        conexao.commit()
        conexao.close()

while True:
    menu1 = int(input("Escolha\n1 - Cadastrar usuário\n2 - Entrar\n3 - Listar usuários\n4 - Excluir usuário\n5 - Alterar usuário\n6 - Sair\n"))
    if menu1 == 1 or menu1 == 2 or menu1 == 3 or menu1 == 4 or menu1 == 5 or menu1 == 6: 
        match menu1:
            case 1:
                Cliente.cadastrarC()
            case 2:
                login = Cliente.autenticar()
                if login[0] == True:
                    if login[1] == 'admin':
                        while True:
                            e = [1, 2, 3, 4, 5, 6]
                            menu2 = int(input("Escolha:\n1 - Cadastrar produto\n2 - Listar produtos\n3 - Excluir produtos\n4 - Alterar produtos\n5 - Recibo total\n6 - Sair\n"))
                            if menu2 in e:
                                match menu2:
                                    case 1:
                                        Produto.cadastrarP()
                                    case 2:
                                        Produto.listarP()
                                    case 3:
                                        Produto.excluirP()
                                    case 4:
                                        Produto.alterarP()
                                    case 5:
                                        Venda.total()
                                    case 6:
                                        print("Saindo da conta...")
                                        break
                            else:
                                print("Opção inválida. Tente novamente.")
                    else :
                        while True:
                            e = [1, 2]
                            menu2 = int(input("Escolha:\n1 - Fazer compra\n2 - Sair\n"))
                            if menu2 in e:
                                match menu2:
                                    case 1:
                                        Venda.recibo(login[1])
                                    case 2:
                                        print("Voltando ao menu...")
                                        break
                            else: 
                                print("Opção inválida. Tente novamente.")
            case 3:
                Cliente.listarC()
            case 4:
                Cliente.excluirC()
            case 5:
                Cliente.alterarC()
            case 6:
                print("Encerrando o programa...")
                break

    else:
        print("Opção inválida. Tente novamente.")