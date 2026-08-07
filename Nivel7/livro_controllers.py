from models.livro_models import Livro

class Livro_c:
    @staticmethod
    def criar(titulo, autor):
        if titulo == "" or autor == "":
            print("Inválido.")
        else:
            Livro.cadastrar(titulo, autor)
            print("Livro cadastrado.")

    @staticmethod
    def listar():
        lista = Livro.listar()
        return lista
    
    @staticmethod
    def alterar(id, nt, na):
        Livro.alterar(id, nt, na)
        print("Informações do livro alteradas.")

    @staticmethod
    def excluir(id):
        Livro.excluir(id)
        print("Livro excluído com sucesso.")

    @staticmethod
    def devolver1(user):
        lista = Livro.devolveu1(user)
        return lista
    
    @staticmethod
    def devolver2(id):
        Livro.devolveu2(id)
        print("Livro devolvido com sucesso.")
    
    @staticmethod
    def emprestar1():
        lista = Livro.emprestou1()
        return lista

    @staticmethod
    def emprestar2(id, user):
        Livro.emprestou2(id, user)
        print("Livro emprestado com sucesso.")