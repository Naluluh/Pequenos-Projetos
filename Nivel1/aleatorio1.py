import random

def uma():
    numero = random.randint(1, 100)
    palpite = int(input("Tente descubrir o número: "))

    if palpite == numero:
        print(f"Parabéns! O número era: {numero}")
    else:
        print(f"Não foi desta vez. O número era: {numero}, não {palpite}")
    
def varias():
    numero = random.randint(1, 100)
    palpite = int(input("Tente descubrir o número: "))

    if palpite > numero:
        print(f"Não foi desta vez. O número é menor que {palpite}")
        palpite = int(input("Tente novamente descubrir o número: "))
    elif palpite < numero:
        print(f"Não foi desta vez. O número é maior que {palpite}")
        palpite = int(input("Tente novamente descubrir o número: "))
    else:
        print(f"Parabéns! O número era: {numero}")

while True:
    menu=int(input("Escolha:\n1 - Uma tentativa\n2 - Várias tentativas\n3 - Sair\n"))
    match menu:
        case 1:
            uma()
        case 2:
            varias()
        case 3:
            print("Saindo...")
            break
        case _:
            print("Opção inválida. Encerrando...")
            break    