from MVC.DAO.abstrata_dao import Dao
from MVC.entidade.pessoa import Pessoa


class VoluntarioDao(Dao):
    def __init__(self):
        super().__init__('voluntarios.pkl')

    def add_voluntario(self, voluntario: Voluntario):
        if voluntario is not None and isinstance(voluntario, Voluntario):
            super().add(voluntario.nome, voluntario)

    def remove_voluntario(self, voluntario: Voluntario):
        if voluntario is not None and isinstance(voluntario, Voluntario):
            super().remove(voluntario.nome)

    def update_voluntario(self, voluntario: Voluntario):
        if voluntario is not None and isinstance(voluntario, Voluntario):
            super().update(voluntario.nome, voluntario)

    def get_voluntario(self, nome_voluntario: str):
        if isinstance(nome_voluntario, str):
            return super().get(nome_voluntario)