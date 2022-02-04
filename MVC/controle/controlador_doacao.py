from MVC.limite.tela_doacao import TelaDoacao
from MVC.entidade.doacao import Doacao

class ControladorDoacoes():
    def __init__(self, controlador_sistema):
        self.__doacoes = []
        self.__tela_doacoes = TelaDoacao
        self.__controlador_sistema = controlador_sistema

