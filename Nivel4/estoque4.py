import csv

with open("estoque4.csv", "r", newline="", encoding="utf-8") as est:
    texto = list(csv.reader(est, delimiter=";"))

if not texto: 
    with open("estoque4.csv", "w", newline="", encoding="utf-8") as est:
            escreva = csv.writer(est, delimiter=";")
            escreva.writerow(["Produto", "Quantidade", "Preço"])

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
    
    with open("estoque4.csv", "a", newline="", encoding="utf-8") as est:
        escreva = csv.writer(est, delimiter=";")
        escreva.writerow([produto, quant, preco])

def listar():
    with open("estoque4.csv", "r", newline="", encoding="utf-8") as est:
        texto = csv.reader(est, delimiter=";")

        for linha in texto:
            print(linha)

def excluir():

    with open("estoque4.csv", "r", newline="", encoding="utf-8") as est:
        texto = csv.reader(est)

        for n, linha in enumerate(texto):
            if n == 0:
                continue
            print(f"{n} - {linha}")
    ind = int(input("Insira o índice do produto que deseja excluir: "))

    linhas = [["Produto", "Quantidade", "Preço"]]
    for i in range(len(nomes)):
        linhas.append([nomes[i], quantidade[i], precos[i]])
    print("Produto excluído com sucesso.")
    with open("estoque4.csv", "w", newline="", encoding="utf-8") as est:
        escreva = csv.writer(est, delimiter=";")
        escreva.writerows(linhas)

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