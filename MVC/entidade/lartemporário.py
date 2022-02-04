from MVC.entidade.voluntario import Voluntario
from MVC.entidade.animal import Animal


class LarTemporario(Voluntario, Animal):
    def __init__(self, voluntario: Voluntario, animal: Animal, data_entrada: str):
        if isinstance(voluntario, Voluntario):
            self.__voluntario = voluntario
        if (isinstance(animal, Animal)):
            self.__animal = Animal
        self.__data_entrada = data_entrada

    @property
    def voluntario(self):
        return self.__voluntario

    @voluntario.setter
    def voluntario(self, voluntario: Voluntario):
        if isinstance(voluntario, Voluntario):
            self.__voluntario = voluntario

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animal = animal

    @property
    def data_entrada(self):
        return self.__data_entrada

    @data_entrada.setter
    def data_entrada(self, data_entrada):
        self.__data_entrada = data_entrada
