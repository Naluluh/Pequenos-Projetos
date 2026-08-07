from model.produtos import Produto

class ProdutoC:
    @staticmethod
    def cadastrar(prod, marca, qntd, preco):
        e = [prod, marca, qntd, preco]
        if None in e:
            print("Insira informações válidas.")
        else:
            Produto.cadastrar(prod, marca, qntd, preco)
            print("Produto cadastrado.")

    @staticmethod
    def listar():
        lista = Produto.listar()
        return lista

    @staticmethod
    def alterar(id, prod, marca, qntd, preco):
        e = [id, prod, marca, qntd, preco]
        if None in e:
            print("Insira informações válidas.")
        else:
            Produto.alterar(id, prod, marca, qntd, preco)
            print("Produto modificado.")

    @staticmethod
    def excluir(id):
        Produto.excluir(id)
        print("Produto excuído com sucesso.")