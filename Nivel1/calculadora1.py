def somar(a,b):
    return a+b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

while True:
    opcao = int(input("Selecione a operação:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair\n"))
    if opcao == 5:
        print("Saindo...")
        break
    if opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4 or opcao != 5:
        print("Opção inválida. Encerrando programa...")
        break

    a = int(input("Selecione o primeiro número: " ))
    b = int(input("Selecione o segundo número: "))

    match opcao:
        case 1:
            resultado = somar(a,b)
            print(f"A soma de {a} e {b} é {resultado}")
            
        case 2:
            resultado = subtracao(a,b)
            print(f"A diferença de {a} e {b} é {resultado}")
            
        case 3:
            resultado = multiplicacao(a,b)
            print(f"O produto de {a} e {b} é {resultado}")
            
        case 4:
            if b != 0:
                resultado = divisao(a,b)
                print(f"O quociente de {a} e {b} é {resultado}")
            else:
                print("Divisão por zero indisponível.")

