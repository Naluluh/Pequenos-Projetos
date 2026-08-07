telefones = []
def cadastro():
    nome = str(input("Insira o nome que deseja cadastrar: "))
    tel = str(input("Insira o telefone que deseja cadastrar: "))
    with open ("agenda4.txt", "a", encoding="utf-8") as agenda:
        agenda.write(f"Nome: {nome}\nTelefone: {tel}\n\n")


def lista():
    with open("agenda4.txt", "r", encoding="utf-8") as agenda:
        linhas = agenda.readlines()
    for i in range(0, len(linhas), 3):
        print(f"Índice {i//3}")
        print(linhas[i], end="")
        print(linhas[i+1], end="")
        print()

def excluir():
    with open("agenda4.txt", "r", encoding="utf-8") as agenda:
        linhas = agenda.readlines()
        quantidade = len(linhas) // 3
    deleta = int(input("Insira o índice que deseja que excluir: "))
    while deleta < 0 or deleta > quantidade-1:
        deleta = int(input("Índice inválido. Insira novamente: "))
    
    inicio = deleta*3
    del linhas[inicio:inicio + 3]

    with open ("agenda4.txt", "w", encoding="utf-8") as agenda:
            agenda.writelines(linhas)
    

while True:
    menu = int(input("Escolha:\n1 - Cadastrar contato\n2 - Listar contatos\n3 - Excluir contato\n4 - Sair\n"))
    if menu == 1 or menu == 2 or menu == 3 or menu == 4:
        match menu:
            case 1:
                cadastro()
            case 2: 
                lista() 
            case 3:
                excluir()
            case 4:
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Encerrando...")
                break