nomes = []
marcas = []
quantidades = []
precos = []

def cadastrar():
    nome = str(input("Produto: "))
    marca = str(input("Marca: "))
    quantidade= int(input("Quantidade: "))
    preco = float(input("Preço: "))

    nomes.append(nome)
    quantidades.append(quantidade)
    marcas.append(marca)
    precos.append(preco)

def consultar():
    print("PRODUTO\t\tMARCA\t\tQUANTIDADE\tPREÇO\t\t")
    for i in range (len(nomes)):
        print(f"{nomes[i]}\t\t{marcas[i]}\t\t{quantidades[i]}\t\t{precos[i]}\t\t")

def alterar():
    for i, op in enumerate(nomes):
        print(f"{i} - {op}")
    e = int(input("Escolha o índice: "))
    nomes[e] = str(input("Novo produto: "))
    marcas[e] = str(input("Nova marca:"))
    quantidades[e] = int(input("Nova quantidade: "))
    precos[e] = float(input("Novo preco: "))

def excluir():
    for i, op in enumerate(nomes):
        print(f"{i} - {op}")
    e = int(input("Escolha o índice: "))
    del nomes[e]
    del quantidades[e]
    del marcas[e]
    del precos[e]
    print("Item excluído com sucesso.")

while True:
    menu = int(input("Escolha:\n1 - Cadastrar produto\n2 - Consultar produto\n3 - Excluir produto\n4 - Alterar produto\n5 - Sair\n"))
    if menu == 1 or menu == 2 or menu == 3 or menu == 4 or menu == 5:
        match menu:
            case 1:
                cadastrar()
            case 2:
                consultar()
            case 3:
                excluir()
            case 4:
                alterar()
            case 5:
                print("Saindo...")
                break
    else:
        print("Opção inválida. Encerrando...")
        break