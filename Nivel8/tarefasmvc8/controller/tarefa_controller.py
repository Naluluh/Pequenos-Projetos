from model.tarefa_model import Tarefa

class Task:
    def cadastro(tarefa, prioridade, prazo, situacao):
        Tarefa.cadastrar(tarefa, prioridade, prazo, situacao)

    def realizacao(id, login):
        Tarefa.realizar(id, login)

    def alteracao(id, tarefa, prioridade, prazo, situacao, funcionario, data):
        Tarefa.alterar(id, tarefa, prioridade, prazo, situacao, funcionario, data)

    def exclusao(id):
        Tarefa.excluir(id)

    def demanda(id, user):
        Tarefa.demandar(id, user)
    
    def exportacao():
        Tarefa.exportar()

    def lista():
        lista = Tarefa.listar()
        return lista
