from controller.compra_controller import CompraC
from controller.produto_controller import ProdutoC

def compra(login):
    while True:
        menu1 = int(input("1 - Fazer compra\n2 - Listar produtos\n3 - Histórico de compra\n4 - Sair\n"))
        e = [1,2,3,4]
        if menu1 in e:
            match menu1:
                case 1:
                    lista = ProdutoC.listar()
                    for id, produto, marca, quantidade, preco in lista:
                        print(f"{id} - {produto} ({marca}) - {quantidade} | R${preco}")
                    id = int(input("Índice: "))
                    quantidade = int(input("Quantidade: "))
                    t = CompraC.comprar(id, quantidade, login[1])
                    print(f"Total da Compra: {t}")
                    print("Compra realizada com sucesso.")

                case 2:
                    lista = ProdutoC.listar()
                    print("-" * 90)
                    print(f"{'ID':<6}|{'PRODUTO':<20}|{'MARCA':<20}|{'QUANTIDADE':<20}|{'PREÇO':<20}|")
                    print("-" * 90)
                    for id, produto, marca, quantidade, preco in lista:
                        print(f"{id:<6}|{produto:<20}|{marca:<20}|{quantidade:<20}|{preco:<20}|")

                case 3:
                    lista = CompraC.historico(login[1])
                    print("-" * 111)
                    print(f"{'ID':<6}|{'PRODUTO':<20}|{'MARCA':<20}|{'QUANTIDADE':<20}|{'PREÇO':<20}|{'COMPRADOR':<20}|")
                    print("-" * 111)
                    for id, produto, marca, quantidade, valor, comprador in lista:
                        print(f"{id:<6}|{produto:<20}|{marca:<20}|{quantidade:<20}|{valor:<20}|{comprador:<20}|")
                
                case 4:
                    print("Saindo da conta...")
                    break

        else:
            print("Opção inválida. Tente novamente.")      