telefones = ([])
def cadastro():
    nome = str(input("Insira o nome que deseja cadastrar: "))
    tel = str(input("Insira o telefone que deseja cadastrar: "))
    telefones.append(f"Nome: {nome}\nTelefone: {tel}")
    return nome

def lista():
    list = "\n".join(telefones)
    print(list)

def excluir():
    list = " ".join(telefones)
    tam = len(telefones)
    for i in range (len(telefones)):
        print(f"{i} - {telefones[i]}")
    deleta = int(input("Insira o índice que deseja que excluir: "))
    del telefones[deleta]

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