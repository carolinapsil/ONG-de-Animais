from MVC.controle.controlador_doacao import ControladorDoacoes
from MVC.controle.controlador_doador import ControladorDoador
from MVC.controle.controlador_adotante import ControladorAdotante
from MVC.controle.controlador_animal import ControladorAnimal
from MVC.controle.controlador_adocao import ControladorAdocao
from MVC.controle.controlador_voluntario import ControladorVoluntario
from MVC.controle.controlador_lartemporario import ControladorLarTemporario
from MVC.limite.tela_principal import TelaPrincipal


class ControladorONG:

    def __init__(self):
        self.__controlador_doacao = ControladorDoacoes(self)
        self.__controlador_doador = ControladorDoador(self)
        self.__controlador_adotante = ControladorAdotante(self)
        self.__controlador_animal = ControladorAnimal(self)
        self.__controlador_adocao = ControladorAdocao(self)
        self.__controlador_voluntario = ControladorVoluntario(self)
        self.__controlador_lartemporario = ControladorLarTemporario(self)
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

    @property
    def controlador_voluntario(self):
        return self.__controlador_voluntario

    @property
    def controlador_lartemporario(self):
        return self.__controlador_lartemporario

    def inicia_sistema(self):
        self.abre_tela()

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

    def pesquisa_animais_disponiveis(self):
        self.__controlador_animal.animais_disponiveis()

    def finaliza_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_doacao, 2: self.cadastra_animal,
                        3: self.cadastra_adotante, 4: self.cadastra_doador,
                        5: self.cadastra_voluntario, 6: self.cadastra_adocao,
                        7: self.cadastra_lartemporario, 8: self.pesquisa_animais_disponiveis,
                        0: self.finaliza_sistema}

        while True:
            opcao_escolhida = self.__tela_principal.open()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
