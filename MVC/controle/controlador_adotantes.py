from MVC.limite.tela_adotante import TelaAdotante
from MVC.entidade.adotante import Adotante

class ControladorAdotantes():
    def __init__(self, controlador_sistema):
        self.__adotantes = []
        self.__tela_adotante = TelaAdotante
        self.__controlador_sistema = controlador_sistema

