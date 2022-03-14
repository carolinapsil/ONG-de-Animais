from MVC.DAO.abstrata_dao import Dao
from MVC.entidade.pessoa import Pessoa


class AdotanteDao(Dao):
    def __init__(self):
        super().__init__('adotantes.pkl')

    def add_adotante(self, adotante: Adotante):
        if adotante is not None and isinstance(adotante, Adotante):
            super().add(adotante.nome, adotante)

    def remove_adotante(self, adotante: Adotante):
        if adotante is not None and isinstance(adotante, Adotante):
            super().remove(adotante.nome)

    def update_adotante(self, adotante: Adotante):
        if adotante is not None and isinstance(adotante, Adotante):
            super().update(adotante.nome, adotante)

    def get_adotante(self, nome_adotante: str):
        if isinstance(nome_adotante, str):
            return super().get(nome_adotante)