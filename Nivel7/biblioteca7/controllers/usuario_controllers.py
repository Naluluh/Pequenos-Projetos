from models.usuario_models import Usuario

class Usuario_c:
    @staticmethod
    def criar(usuario, senha):
        if usuario == "" or senha == "":
            print("Inválido.")
            return
        else:
            Usuario.criar(usuario, senha)
            print("Usuário cadastrado.")

    @staticmethod
    def autenticar(usuario, senha):
        user = Usuario.autenticar(usuario, senha)
        f = 0
        if user:
            f = 1
        else:
            f += 0
        if f == 1:
            print("Login efetuado com sucesso.")
            return True, usuario
        else:
            print("Usuário ou senha incorretos.")
            return False, None
        
    @staticmethod
    def excluir(id):
        Usuario.excluir(id)
        print("Conta excluída com sucesso.")

    @staticmethod
    def alterar(id, novoU, novaS):
        Usuario.alterar(id, novoU, novaS)
        print("Conta modificada com sucesso.")

    @staticmethod
    def listar():
        lista = Usuario.listar()
        return lista