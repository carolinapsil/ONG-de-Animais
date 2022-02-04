from MVC.limite.tela_adotante import TelaAdotante
from MVC.entidade.adotante import Adotante

class ControladorAdotantes():
    def __init__(self, controlador_sistema):
        self.__adotantes = []
        self.__tela_adotante = TelaAdotante
        self.__controlador_sistema = controlador_sistema

    def inicia(self):
        self.abre_tela_inicial()

    def inclui_adotante(self):
        pass

    def altera_adotante(self):
        pass

    def exclui_adotante(self):
        pass

    def finalizar(self):
        pass

    def abre_tela_inicial(self):
        switcher = (1: self.inclui_adotante, 2: self.altera_adotante, 3: self.lista_adotante, 4: self.exclui_adotante, 0: self.finalizar)