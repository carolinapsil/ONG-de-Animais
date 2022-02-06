from MVC.limite.tela_lartemporario import TelaLarTemporario
from MVC.entidade.lartemporário import LarTemporario


class ControladorLarTemporario:
    def __init__(self, controlador_sistema):
        self.__lares = []
        self.__tela_lartemporario = TelaLarTemporario
        self.__controlador_sistema = controlador_sistema

    def inicia(self):
        self.abre_tela()

    def pega_lartemporario_por_data(self, data_entrada: str):
        for lartemporario in self.__lares:
            if lartemporario.data == data_entrada:
                return lartemporario
        return None

    def inclui_lartemporario(self):
        dados_lartemporario = self.__tela_lartemporario.pega_dados_lartemporario()
        lartemporario = LarTemporario(dados_lartemporario["voluntario"],dados_lartemporario["animal"],
                                dados_lartemporario["data_entrada"])
        self.__lares.append(lartemporario)

    def altera_lartemporario(self):
        self.lista_lartemporario()
        data_entrada = self.__tela_lartemporario.seleciona_lartemporario()
        lartemporario = self.pega_lartemporario_por_data(data_entrada)

        if lartemporario is not None:
          novos_dados_lartemporario = self.__tela_lartemporario.pega_dados_lartemporario()
          lartemporario.voluntario = novos_dados_lartemporario["voluntario"]
          lartemporario.animal = novos_dados_lartemporario["animal"]
          lartemporario.data_entrada = novos_dados_lartemporario["data_entrada"]
          self.lista_lartemporario()
        else:
          self.__tela_lartemporario.mostra_mensagem("ATENCAO: Lar temporario não existente")

    def lista_lartemporario(self):
        for lartemporario in self.__lares:
            self.__tela_lartemporario.mostra_lartemporario({"voluntario": lartemporario.voluntario,
                                                      "animal": lartemporario.animal,
                                                      "data_entrada": lartemporario.data_entrada})

    def exclui_lartemporario(self):
        self.lista_lartemporario()
        data_entrada = self.__tela_lartemporario.seleciona_lartemporario()
        lartemporario = self.pega_lartemporario_por_data(data_entrada)

        if lartemporario is not None:
            self.__lares.remove(lartemporario)
            self.lista_lartemporario()
        else:
            self.__tela_lartemporario.mostra_mensagem("ATENCAO: Lar temporario não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        switcher = {1: self.inclui_lartemporario(), 2: self.altera_lartemporario(), 3: self.lista_lartemporario(),
                    4: self.exclui_lartemporario(), 0: self.retornar}
        while True:
            opcao_escolhida = self.__tela_lartemporario.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def mostra_opcoes(self):
        self.__tela_lartemporario.tela_opcoes()
