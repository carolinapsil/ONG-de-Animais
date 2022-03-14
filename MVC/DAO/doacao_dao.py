from MVC.DAO.abstrata_dao import Dao
from MVC.entidade.doacao import Doacao

class DoacaoDao(Dao):
    def __init__(self):
        super().__init__('doacoes.pkl')

    def add_doacao(self, doacao: Doacao):
        if evento is not None and isinstance(doacao, Doacao):
            super().add(doacao.codigo, doacao)

    def remove_doacao(self, doacao: Doacao):
        if doacao is not None and isinstance(doacao, Doacao):
            super().remove(doacao.codigo)

    def update_doacao(self, doacao: Doacao):
        if doacao is not None and isinstance(doacao, Doacao):
            super().update(doacao.codigo, doacao)

    def get_doacao(self, codigo: int):
        if isinstance(codigo, int):
            return super().get(codigo)
