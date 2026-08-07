from model.usuario_model import Usuario

class User:
    def lista():
        lista = Usuario.listar()
        return lista
        
    def cadastro(usuario, senha):
        Usuario.cadastrar(usuario, senha)

    def autenticacao(usuario, senha):
        login = Usuario.autenticar(usuario, senha)
        return login

    def exclusao(id):
        Usuario.excluir(id)

    def alteracao(id, usuario, senha):
        Usuario.alterar(id, usuario, senha)

        