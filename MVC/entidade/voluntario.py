from pessoa import Pessoa


class Voluntario(Pessoa):

    def __init__(self, nome: str, data_nascimento: str, telefone: str, genero: str, email: str, endereco: str, oferece_lt: str):
        self.__oferece_lt = oferece_lt
        super.__init__(nome, data_nascimento, telefone, genero, email, endereco)
