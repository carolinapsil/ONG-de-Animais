from MVC.limite.tela_doador import TelaDoador
from MVC.entidade.doador import Doador

class ControladorDoadores():
    def __init__(self, controlador_sistema):
        self.__doadores = []
        self.__tela_doador = TelaDoador
        self.__controlador_sistema = controlador_sistema
