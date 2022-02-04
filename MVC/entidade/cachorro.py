from animal import Animal


class Cachorro(Animal):

    def __init__(self, nome: str, chegada: str, ano_nascimento: str, sexo: str, doenca: str, vacina: str, castracao: str, porte: str):
        self.__porte = porte
        super.__init__(nome, chegada, ano_nascimento, sexo, doenca, vacina, castracao)
