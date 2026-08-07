from controller.tarefa_controller import Task 
from controller.usuario_controller import User

def admin_menu(login):
    while True:
        menu = int(input("1 - Cadastrar tarefa\n2 - Realizar tarefa\n3 - Listar tarefas\n4 - Alterar tarefa\n5 - Excluir tarefa\n6 - Demandar tarefa\n7 - Exportar planilha de tarefas (Excel)\n8 - Sair\n"))
        e = [1,2,3,4,5,6,7,8]
        if menu in e:
            match menu:
                case 1:
                    task = str(input("Tarefa: "))
                    priority = str(input("Prioridade (alta, moderada, baixa): "))
                    deadline = str(input("Prazo: "))
                    status = str(input("Situação: "))
                    Task.cadastro(task, priority, deadline, status)

                case 2:
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

                case 3:
                    lista = Task.lista()
                    print("=== TAREFAS ===")
                    print("-"*90)
                    print(f"{'ID':<5}|{'TAREFA':<15}|{'PRIORIDADE':<10}|{'PRAZO':<13}|{'SITUAÇÃO':<11}|{'FUNCIONÁRIO':<15}|{'DATA':<13}|")
                    for id, tarefa, prioridade, prazo, situacao, funcionario, data in lista:
                        print(f"{id:<5}|{tarefa:<15}|{prioridade:<10}|{str(prazo):<13}|{situacao:<11}|{funcionario:<15}|{str(data):<13}|")
                    print("-"*90)

                case 4:
                    lista = Task.lista()
                    print("=== TAREFAS ===")
                    print("-"*90)
                    print(f"{'ID':<5}|{'TAREFA':<15}|{'PRIORIDADE':<10}|{'PRAZO':<13}|{'SITUAÇÃO':<11}|{'FUNCIONÁRIO':<15}|{'DATA':<13}|")
                    print("-"*90)
                    for id, tarefa, prioridade, prazo, situacao, funcionario, data in lista:
                        print(f"{id:<5}|{tarefa:<15}|{prioridade:<10}|{str(prazo):<13}|{situacao:<11}|{funcionario:<15}|{str(data):<13}|")
                    print("-"*90)
                    id = int(input("ID: "))
                    tarefa = str(input("Nova Tarefa: "))
                    prioridade = str(input("Nova Prioridade (alta, moderada, baixa): "))
                    prazo = str(input("Novo Prazo: "))
                    situacao = str(input("Nova Situação: "))
                    funcionario = str(input("Novo Funcionário: "))
                    data = str(input("Nova Data: "))
                    Task.alteracao(id, tarefa, prioridade, prazo, situacao, funcionario, data)

                case 5:
                    lista = Task.lista()
                    print("=== TAREFAS ===")
                    print("-"*90)
                    print(f"{'ID':<5}|{'TAREFA':<15}|{'PRIORIDADE':<10}|{'PRAZO':<13}|{'SITUAÇÃO':<11}|{'FUNCIONÁRIO':<15}|{'DATA':<13}|")
                    print("-"*90)
                    for id, tarefa, prioridade, prazo, situacao, funcionario, data in lista:
                        print(f"{id:<5}|{tarefa:<15}|{prioridade:<10}|{str(prazo):<13}|{situacao:<11}|{funcionario:<15}|{str(data):<13}|")
                    print("-"*90)
                    id = int(input("ID: "))
                    Task.exclusao(id)
                    
                case 6:
                    lista = Task.lista()
                    print("=== TAREFAS ===")
                    print("-"*90)
                    print(f"{'ID':<5}|{'TAREFA':<15}|{'PRIORIDADE':<10}|{'PRAZO':<13}|{'SITUAÇÃO':<11}|{'FUNCIONÁRIO':<15}|{'DATA':<13}|")
                    print("-"*90)
                    for id, tarefa, prioridade, prazo, situacao, funcionario, data in lista:
                        print(f"{id:<5}|{tarefa:<15}|{prioridade:<10}|{str(prazo):<13}|{situacao:<11}|{funcionario:<15}|{str(data):<13}|")
                    print("-"*90)
                    idT = int(input("ID TAREFA: "))
                    print("=== USUÁRIOS ===")
                    lista = User.lista()
                    print("-"*22)
                    print(f"{'ID':<5}|{'USUÁRIO':<15}|")
                    print("-"*22)
                    for id, usuario, senha in lista:
                        print(f"{id:<5}|{usuario:<15}|")
                    print("-"*22)
                    idU = int(input("ID Usuario: "))
                    Task.demanda(idT, idU)

                case 7:
                    Task.exportacao()

                case 8:
                    print("Saindo da conta...")
                    break
    else:
        print("Selecione uma opção válida.")
            



                