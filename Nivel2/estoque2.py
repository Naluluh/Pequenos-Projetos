nomes = []
precos = []
quantidade = []

def cadastrar():
    produto = str(input("Insira o nome do produto: "))
    quant = int(input("Insira a quantidade: "))
    preco = float(input("Insira o preço: "))
    nomes.append(produto)
    quantidade.append(quant)
    precos.append(preco)

def listar():
    print("PRODUTO\t\tQUANTIDADE\tPREÇO\t")
    for i in range(len(nomes)):
        print(f"{nomes[i]}\t\t{quantidade[i]}\t\t{precos[i]}\t")


def excluir():
    for i, p in enumerate(nomes):
        print(f"{i} - {p}")
    ind = int(input("Insira o índice do produto que deseja excluir: "))
    del quantidade[ind]
    del nomes[ind]
    del precos[ind]
    print("Produto excluído com sucesso.")

while True:
    menu = int(input("Escolha:\n1 - Cadastrar produto\n2 - Listar produto\n3 - Excluir produto\n4 - Sair\n"))
    if menu == 1 or menu == 2 or menu == 3 or menu == 4:
        match menu:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                excluir()
            case 4:
                print("Saindo...")
                break
    else:
        print("Opção inválida. Encerrando...")
        break