from MVC.entidade.doador import Doador


class Doacao:
    def __init__(self, doador: Doador, valor: float, data_doacao: str):
        if (isinstance(doador, Doador)):
            self.__doador = doador
        self.__valor = valor
        self.__data_doacao = data_doacao

    @property
    def doador(self):
        return self.__doador

    @doador.setter
    def doador(self, doador):
        self.__doador = doador

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def data_doacao(self):
        return self.__data_doacao

    @data_doacao.setter
    def data_doacao(self, data_doacao):
        self.__data_doacao = data_doacao
