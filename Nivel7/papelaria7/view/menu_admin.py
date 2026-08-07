from controller.produto_controller import ProdutoC
from controller.compra_controller import CompraC

def menu2():
    while True:
        menu1 = int(input("1 - Cadastrar produto\n2 - Listar produtos\n3 - Excluir produto\n4 - Alterar produto\n5 - Histórico de vendas\n6 - Sair\n"))
        e = [1,2,3,4,5,6]
        if menu1 in e:
            match menu1:
                case 1:
                    produto = str(input("Produto: "))
                    marca = str(input("Marca: "))
                    quantidade = str(input("Quantidade: "))
                    preco = str(input("Preço: "))
                    ProdutoC.cadastrar(produto, marca, quantidade, preco)

                case 2:
                    lista = ProdutoC.listar()
                    print("-" * 90)
                    print(f"{'ID':<6}|{'PRODUTO':<20}|{'MARCA':<20}|{'QUANTIDADE':<20}|{'PREÇO':<20}|")
                    print("-" * 90)

                    for id, produto, marca, quantidade, preco in lista:
                        print(f"{id:<6}|{produto:<20}|{marca:<20}|{quantidade:<20}|{preco:<20}|")

                case 3:
                    lista = ProdutoC.listar()
                    for id, produto, marca, quantidade, preco in lista:
                        print(f"{id} - {produto} ({marca}) - {quantidade} | R${preco}")
                    id = int(input("Índice: "))
                    ProdutoC.excluir(id)
                
                case 4:
                    lista = ProdutoC.listar()
                    for id, produto, marca, quantidade, preco in lista:
                        print(f"{id} - {produto} ({marca}) - {quantidade} | R${preco}")
                    id = int(input("Índice: "))
                    produto = str(input("Novo Produto: "))
                    marca = str(input("Nova Marca: "))
                    quantidade = str(input("Nova Quantidade: "))
                    preço = str(input("Novo Preço: "))
                    ProdutoC.alterar(id, produto, marca, quantidade, preco)
                    
                case 5:
                    lista = CompraC.recibo()
                    print("-" * 111)
                    print(f"{'ID':<6}|{'PRODUTO':<20}|{'MARCA':<20}|{'QUANTIDADE':<20}|{'PREÇO':<20}|{'COMPRADOR':<20}|")
                    print("-" * 111)
                    for id, produto, marca, quantidade, valor, comprador in lista:
                        print(f"{id:<6}|{produto:<20}|{marca:<20}|{quantidade:<20}|{valor:<20}|{comprador:<20}|")

                case 6:
                    print("Saindo da conta...")
                    break

        else:
            print("Opção inválida. Tente novamente.")         