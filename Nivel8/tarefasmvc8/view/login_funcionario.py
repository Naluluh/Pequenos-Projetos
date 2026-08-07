from controller.tarefa_controller import Task 

def funcionario_menu(login):
    while True:
        menu = int(input("1 - Realizar tarefa\n2 - Listar tarefas\n3 - Exportar planilha de tarefas (Excel)\n4 - Sair\n"))
        e = [1,2,3,4]
        if menu in e:
            match menu:
                case 1:
                    lista = Task.lista()
                    print("=== TAREFAS ===")
                    print("-"*90)
                    print(f"{'ID':<5}|{'TAREFA':<15}|{'PRIORIDADE':<10}|{'PRAZO':<13}|{'SITUAÇÃO':<11}|{'FUNCIONÁRIO':<15}|{'DATA':<13}|")
                    print("-"*90)
                    for id, tarefa, prioridade, prazo, situacao, funcionario, data in lista:
                        print(f"{id:<5}|{tarefa:<15}|{prioridade:<10}|{str(prazo):<13}|{situacao:<11}|{funcionario:<15}|{str(data):<13}|")
                    print("-"*90)
                    id = int(input("ID: "))
                    Task.realizacao(id, login[1])

                case 2:
                    lista = Task.lista()
                    print("=== TAREFAS ===")
                    print("-"*90)
                    print(f"{'ID':<5}|{'TAREFA':<15}|{'PRIORIDADE':<10}|{'PRAZO':<13}|{'SITUAÇÃO':<11}|{'FUNCIONÁRIO':<15}|{'DATA':<13}|")
                    print("-"*90)
                    for id, tarefa, prioridade, prazo, situacao, funcionario, data in lista:
                        print(f"{id:<5}|{tarefa:<15}|{prioridade:<10}|{str(prazo):<13}|{situacao:<11}|{funcionario:<15}|{str(data):<13}|")
                    print("-"*90)

                case 3:
                    Task.exportacao()

                case 4:
                    print("Saindo da conta...")
                    break
    else:
        print("Selecione uma opção válida.")