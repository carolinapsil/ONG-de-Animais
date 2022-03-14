class NomeAnimalDuplicado(Exception):
    def __init__(self):
        super().__init__("Já existe um animal cadastrado com esse nome!")