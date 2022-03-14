from MVC.DAO.abstrata_dao import Dao
from MVC.entidade.lartemporário import LarTemporario


class LarTemporarioDao(Dao):
    def __init__(self):
        super().__init__('larestemporarios.pkl')

    def add_lartemporario(self, lartemporario: LarTemporario):
        if lartemporario is not None and isinstance(lartemporario, LarTemporario):
            super().add(lartemporario.codigo, lartemporario)

    def remove_lartemporario(self, lartemporario: LarTemporario):
        if lartemporario is not None and isinstance(lartemporario, LarTemporario):
            super().remove(lartemporario.codigo)

    def update_lartemporario(self, lartemporario: LarTemporario):
        if lartemporario is not None and isinstance(lartemporario, LarTemporario):
            super().update(lartemporario.codigo, lartemporario)

    def get_lartemporario(self, codigo_lartemporario: int):
        if isinstance(codigo_lartemporario, int):
            return super().get(codigo_lartemporario)