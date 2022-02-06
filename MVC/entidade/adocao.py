from MVC.entidade.adotante import Adotante
from MVC.entidade.animal import Animal


class Adocao:
    def __init__(self, adotante: Adotante, animal: Animal, data: str, codigo: str):
        self.__adotante = adotante
        self.__animal = animal
        self.__data = data
        self.__codigo = codigo

    @property
    def adotante(self):
        return self.__adotante

    @adotante.setter
    def adotante(self, adotante: Adotante):
        self.__adotante = adotante

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal: Animal):
        self.__animal = animal

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
