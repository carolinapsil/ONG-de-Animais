from MVC.entidade.voluntario import Voluntario
from MVC.entidade.animal import Animal


class LarTemporario:
    def __init__(self, voluntario: Voluntario, animal: Animal, data_entrada: str, codigo: str):
        self.__voluntario = voluntario
        self.__animal = animal
        self.__data_entrada = data_entrada
        self.__codigo = codigo

    @property
    def voluntario(self):
        return self.__voluntario

    @voluntario.setter
    def voluntario(self, voluntario: Voluntario):
        self.__voluntario = voluntario

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal: Animal):
        self.__animal = animal

    @property
    def data_entrada(self):
        return self.__data_entrada

    @data_entrada.setter
    def data_entrada(self, data_entrada):
        self.__data_entrada = data_entrada

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
