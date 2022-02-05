from MVC.controle.controlador_doacao import ControladorDoacoes
from MVC.controle.controlador_doador import ControladorDoador
from MVC.controle.controlador_adotantes import ControladorAdotantes
from MVC.controle.controlador_animal import ControladorAnimal
from MVC.limite.tela_principal import TelaPrincipal


class ControladorONG:

    def __init__(self):
        self.__controlador_doacao = ControladorDoacoes(self)
        self.__controlador_doador = ControladorDoador(self)
        self.__controlador_adotantes = ControladorAdotantes(self)
        self.__controlador_animal = ControladorAnimal(self)

        #colocar todos os controladores
        self.__tela_principal = TelaPrincipal()

    @property
    def controlador_doacao(self):
        return self.__controlador_doacao

    @property
    def controlador_doador(self):
        return self.__controlador_doador

    @property
    def controlador_adotantes(self):
        return self.__controlador_adotantes

    @property
    def controlador_controlador_animal(self):
        return self.__controlador_animal

    def inicia_sistema(self):
        opcao = self.__tela_principal.mostra_opcoes()
        if opcao == 1:
            self.__controlador_doacao.mostra_opcoes()
        elif opcao == 2:
            self.__controlador_animal.mostra_opcoes()


    def cadastro_doador(self):
        self.__controlador_doador.abre_tela_inicial()

    def cadastro_adotante(self):
        self.__controlador_adotantes.abre_tela_inicial()

    def cadastro_adocao(self):
        self.__controlador_doacao.abre_tela()

    def cadastro_animal(self):
        self.__controlador_animal.abre_tela()


controlador_ong = ControladorONG()
controlador_ong.inicia_sistema()