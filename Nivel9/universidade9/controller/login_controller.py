from model.login import Usuario

class UsuarioC:
    @staticmethod
    def cadastrar(usuario, senha):
        if not usuario or not senha:
            print("Digite usuário e senha válidos.")
            return
        else:
            Usuario.cadastrar(usuario, senha)
            print("Conta cadastrada.")

    @staticmethod
    def autenticar(usuario, senha):
        user = Usuario.autenticar(usuario, senha)
        f = 0
        if user:
            f = 1
            print("Login efetuado com sucesso.")
            return True, usuario
        else:
            f += 0
            print("Usuário ou senha incorretos.")
            return False, None

    @staticmethod
    def listar():
        lista = Usuario.listar()
        return lista
    
    @staticmethod
    def alterar(id, usuario, senha):
        if not usuario or not senha:
            print("Digite usuário e senha válidos.")
            return
        else:
            Usuario.alterar(id, usuario, senha)
            print("Conta modificada.")

    @staticmethod
    def excluir(id):
        Usuario.excluir(id)
        print("Conta excluída com sucesso.")