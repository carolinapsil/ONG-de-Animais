from MVC.controle.controlador_doacao import ControladorDoacoes
from MVC.controle.controlador_doador import ControladorDoador
from MVC.controle.controlador_adotante import ControladorAdotante
from MVC.controle.controlador_animal import ControladorAnimal
from MVC.controle.controlador_adocao import ControladorAdocoes
from MVC.limite.tela_principal import TelaPrincipal


class ControladorONG:

    def __init__(self):
        self.__controlador_doacao = ControladorDoacoes(self)
        self.__controlador_doador = ControladorDoador(self)
        self.__controlador_adotantes = ControladorAdotante(self)
        self.__controlador_animal = ControladorAnimal(self)
        self.__controlador_adocao = ControladorAdocoes
        #colocar todos os controladores
        self.__tela_principal = TelaPrincipal()

    @property
    def controlador_doacao(self):
        return self.__controlador_doacao

    @property
    def controlador_doador(self):
        return self.__controlador_doador

    @property
    def controlador_adotante(self):
        return self.__controlador_adotante

    @property
    def controlador_animal(self):
        return self.__controlador_animal

    @property
    def controlador_adocao(self):
        return self.__controlador_adocao

    def inicia_sistema(self):
        self.abre_tela()

        #opcao = self.__tela_principal.mostra_opcoes()
        #if opcao == 1:
        #    self.__controlador_doacao.mostra_opcoes()
        #elif opcao == 2:
         #   self.__controlador_animal.mostra_opcoes()


    def cadastra_doador(self):
        self.__controlador_doador.abre_tela()

    def cadastra_adotante(self):
        self.__controlador_adotante.abre_tela()

    def cadastra_adocao(self):
        self.__controlador_adocao.abre_tela()

    def cadastra_animal(self):
        self.__controlador_animal.abre_tela()

    def cadastra_doacao(self):
        self.__controlador_doacao.abre_tela()

    def cadastra_voluntario(self):
        self.__controlador_voluntario.abre_tela()

    def cadastra_lartemporario(self):
        self.__controlador_lartemporario.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.__cadastra_doacao, 2: self.__cadastra_doador,
                        3: self.__cadastra_adotante, 4: self.__cadastra_voluntario,
                        5: self.__cadastra_lartemporario, 6: self.__cadastra_animal}

        while True:
            opcao_escolhida = self.__tela_principal.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

controlador_ong = ControladorONG()
controlador_ong.inicia_sistema()