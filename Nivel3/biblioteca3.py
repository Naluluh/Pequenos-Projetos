livros = []
autors = []
emprestimo = [[],[]]

def cadastrar():
    livro = str(input("Insira o nome do livro: "))
    autor = str(input("Insira o autor: "))
    livros.append(livro)
    autors.append(autor)

def emprestar():
    for i, op in enumerate(livros):
        print(f"{i} - {op}")
    e = int(input("Selecione o índice do livro: "))
    emprestimo[0].append(livros[e])
    emprestimo[1].append(autors[e])
    del livros[e]
    del autors[e]


def devolver():
    for i, op in enumerate(emprestimo[0]):
        print(f"{i} - {op}")
    e2 = int(input(f"Insira índice do livro que deseja devolver: "))
    livros.append(emprestimo[0][e2])
    autors.append(emprestimo[1][e2])
    del emprestimo[0][e2]
    del emprestimo[1][e2]

while True:
    menu = int(input("Escolha: \n1 - Cadastrar livro\n2 - Emprestar livro\n3 - Devolver livro\n4 - Sair\n"))
    if menu == 1 or menu == 2 or menu == 3 or menu == 4:
        match menu:
            case 1:
                cadastrar()
            case 2:
                emprestar()
            case 3:
                devolver()
            case 4:
                print("Saindo...")
                break
    else:
        print("Opção inválida. Encerrando...")
        break