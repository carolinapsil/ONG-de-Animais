from MVC.DAO.abstrata_dao import Dao
from MVC.entidade.animal import Animal


class AnimalDao(Dao):
    def __init__(self):
        super().__init__('animais.pkl')

    def add_animal(self, animal: Animal):
        if animal is not None and isinstance(animal, Animal):
            super().add(animal.nome, animal)

    def remove_animal(self, animal: Animal):
        if animal is not None and isinstance(animal, Animal):
            super().remove(animal.nome)

    def update_animal(self, animal: Animal):
        if animal is not None and isinstance(animal, Animal):
            super().update(animal.nome, animal)

    def get_animal(self, nome_animal: str):
        if isinstance(nome_animal, str):
            return super().get(nome_animal)