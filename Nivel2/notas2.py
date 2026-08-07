alunos = []
notas = [[],
         []]
def aluno():
    nome = str(input("Insira o nome do aluno: "))
    alunos.append(nome)

def nota():
    list = " ".join(alunos)
    tam = len(alunos)
    for i in range (len(alunos)):
        print(f"{i} - {alunos[i]}")
    j = int(input("Selecione o índice do aluno: "))
    nota = float(input("Insira a nota do aluno: "))
    notas[j].append(nota)

def medias():
    for i in range(len(alunos)):
        print(f"{i} - {alunos[i]}")
    j = int(input("Selecione o índice do aluno: "))
    s = 0
    for n in notas[j]:
        s += n
    media = s / len(notas[j])
    print(f"Aluno: {alunos[j]}\nMédia: {media:.2f}")


while True:
    menu = int(input("Escolha:\n1 - Cadastrar aluno\n2 - Cadastrar nota\n3 - Ver média\n4 - Sair\n"))
    if menu == 1 or menu == 2 or menu == 3 or menu == 4:
        match menu:
            case 1:
                aluno()
            case 2:
                nota()
            case 3:
                medias()
            case 4:
                print("Saindo...")
                break
    else:
        print("Opção inválida. Encerrando...")
        break

    