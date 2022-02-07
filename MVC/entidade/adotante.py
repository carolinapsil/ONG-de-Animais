from MVC.entidade.pessoa import Pessoa


class Adotante(Pessoa):

    def __init__(self, nome: str, data_nascimento: str, telefone: str, genero: str, email: str,
                 endereco: str, idade: int):
        super().__init__(nome, data_nascimento, telefone, genero, email, endereco)
        self.__idade = idade

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade
