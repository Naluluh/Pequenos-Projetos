while True:
    opcao = int(input("Escolha: \n1 - Fahrenheit -> Celsius\n2 - Celsius -> Fahrenheit\n3 - Sair\n"))
    if opcao == 1 or opcao == 2 or opcao == 3:
        print("== CONVERSOR ==")
        match opcao:
            case 1:
                fahrenheit = float(input("Graus Fahrenheit: "))
                celsius = (fahrenheit - 32) * 5 / 9
                print(f"Celsius: {celsius}") 
                
            case 2:
                celsius = float(input("Graus Celsius: "))
                fahrenheit = (celsius * 9 / 5) + 32
                print(f"Fahrenheit: {fahrenheit}") 
                
            case 3:
                print("Saindo...")
                break
                
    else:
        print("Opção inválida. Encerrando...")
        break

