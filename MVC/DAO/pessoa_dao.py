from MVC.dao.dao import Dao
from MVC.entidade.pessoa import Pessoa


class PessoaDao(Dao):
    def __init__(self):
        super().__init__('pessoas.pkl')

    def add_pessoa(self, pessoa: Pessoa):
        if pessoa is not None and isinstance(pessoa, Pessoa):
            super().add(pessoa.nome, pessoa)

    def remove_pessoa(self, pessoa: Pessoa):
        if pessoa is not None and isinstance(pessoa, Pessoa):
            super().remove(pessoa.nome)

    def update_pessoa(self, pessoa: Pessoa):
        if pessoa is not None and isinstance(pessoa, Pessoa):
            super().update(pessoa.nome, pessoa)

    def get_pessoa(self, nome_pessoa: str):
        if isinstance(nome_pessoa, str):
            return super().get(nome_pessoa)