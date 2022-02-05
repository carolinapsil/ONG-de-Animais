from MVC.controle.controlador_doacao import ControladorDoacoes
from MVC.controle.controlador_animal import ControladorAnimal
from MVC.controle.controlador_doador import ControladorDoador
from MVC.controle.controlador_adotantes import ControladorAdotantes
from MVC.limite.tela_principal import TelaPrincipal


class ControladorONG:

    def __init__(self):
        self.__controlador_doacao = ControladorDoacoes(self)
        self.__controlador_animal = ControladorAnimal(self)
        self.__controlador_doador = ControladorDoador(self)
        self.__controlador_adotantes = ControladorAdotantes(self)

        #colocar todos os controladores
        self.__tela_principal = TelaPrincipal()

    def inicia_sistema(self):
        opcao = self.__tela_principal.mostra_opcoes()
        if opcao == 1:
            self.__controlador_doacao.mostra_opcoes()


controlador_ong = ControladorONG()
controlador_ong.inicia_sistema()