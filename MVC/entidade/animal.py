from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def __init__(self, nome: str, chegada: str, ano_nascimento: str, sexo: str, doenca: str, vacina: str, castracao: str):
        self.__nome = nome
        self.__chegada = chegada
        self.__ano_nascimento = ano_nascimento
        self.__sexo = sexo
        self.__doenca = doenca
        self.__vacina = vacina
        self.__castracao = castracao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def chegada(self):
        return self.__chegada

    @chegada.setter
    def chegada(self, chegada):
        self.__chegada = chegada

    @property
    def ano_nascimento(self):
        return self.__ano_nascimento

    @ano_nascimento.setter
    def ano_nascimento(self, ano_nascimento):
        self.__ano_nascimento = ano_nascimento

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def doenca(self):
        return self.__doenca

    @doenca.setter
    def doenca(self, doenca):
        self.__doenca = doenca

    @property
    def vacina(self):
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina):
        self.__vacina = vacina

    @property
    def castracao(self):
        return self.__castracao

    @castracao.setter
    def castracao(self, castracao):
        self.__castracao = castracao
