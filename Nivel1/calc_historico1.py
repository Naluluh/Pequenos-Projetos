historico = ["=== HISTÓRICO ==="]

def somar(a,b):
    historico.append(f"{a} + {b} = {a+b}")
    return a+b

def subtracao(a,b):
    historico.append(f"{a} - {b} = {a-b}")
    return a - b

def multiplicacao(a,b):
    historico.append(f"{a} X {b} = {a*b}")
    return a*b

def divisao(a,b):
    historico.append(f"{a} / {b} = {a/b}")
    return a/b

def numeros():
    a = int(input("Selecione o primeiro número: " ))
    b = int(input("Selecione o segundo número: "))
    return a, b

while True:
    opcao = int(input("Selecione a operação:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Histórico\n6 - Sair\n"))

    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5 or opcao == 6:
        match opcao:
            case 1:
                a, b = numeros()
                resultado = somar(a,b)
                print(f"A soma de {a} e {b} é {resultado}")
                
            case 2:
                a, b = numeros()
                resultado = subtracao(a,b)
                print(f"A diferença de {a} e {b} é {resultado}")
                
            case 3:
                a, b = numeros()
                resultado = multiplicacao(a,b)
                print(f"O produto de {a} e {b} é {resultado}")
                
            case 4:
                a, b = numeros()
                if b != 0:
                    resultado = divisao(a,b)
                    print(f"O quociente de {a} e {b} é {resultado}")
                else:
                    print("Divisão por zero indisponível.")

            case 5:
                hist = "\n".join(historico)
                print(hist)

            case 6:
                print("Saindo...")
                break

    else:
        print("Opção inválida. Encerrando programa...")
        break

    

    

    