from MVC.DAO.abstrata_dao import Dao
from MVC.entidade.pessoa import Pessoa


class DoadorDao(Dao):
    def __init__(self):
        super().__init__('doadores.pkl')

    def add_doador(self, doador: Doador):
        if doador is not None and isinstance(doador, Doador):
            super().add(doador.cpf, doador)

    def remove_doador(self, doador: Doador):
        if doador is not None and isinstance(doador, Doador):
            super().remove(doador.cpf)

    def update_doador(self, doador: Doador):
        if doador is not None and isinstance(doador, Doador):
            super().update(doador.nome, doador)

    def get_doador(self, nome_doador: str):
        if isinstance(nome_doador, str):
            return super().get(nome_doador)