from model.vendas import Compra

class CompraC:
    @staticmethod
    def comprar(id, qntd, user):
        q = Compra.comprar1(id)
        v = Compra.comprar2(id, qntd, q, user)
        return v

    @staticmethod  
    def historico(user):
        lista = Compra.historico(user)
        return lista
    
    @staticmethod
    def recibo():
        lista = Compra.recibo()
        return lista
