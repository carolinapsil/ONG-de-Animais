from MVC.entidade.pessoa import Pessoa


class Doador(Pessoa):

    def __init__(self, nome: str, data_nascimento: str, telefone: str, genero: str, email: str, endereco: str):
        super().__init__(nome, data_nascimento, telefone, genero, email, endereco)
