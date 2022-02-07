from MVC.limite.tela_lartemporario import TelaLarTemporario
from MVC.entidade.lartemporário import LarTemporario


class ControladorLarTemporario:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lares = []
        self.__tela_lartemporario = TelaLarTemporario()

    def pega_lartemporario_por_codigo(self, codigo: str):
        for lartemporario in self.__lares:
            if lartemporario.codigo == codigo:
                return lartemporario
        return None

    def incluir_lartemporario(self):
        dados_lartemporario = self.__tela_lartemporario.pega_dados_lartemporario()
        lartemporario = LarTemporario(dados_lartemporario["voluntario"], dados_lartemporario["animal"], dados_lartemporario["data_entrada"], dados_lartemporario["codigo"])
        self.__lares.append(lartemporario)

    def altera_lartemporario(self):
        self.lista_lartemporario()
        codigo_lartemporario = self.__tela_lartemporario.seleciona_lartemporario()
        lartemporario = self.pega_lartemporario_por_codigo(codigo_lartemporario)

        if lartemporario is not None:
            novos_dados_lartemporario = self.__tela_lartemporario.pega_dados_lartemporario()
            lartemporario.voluntario = novos_dados_lartemporario["voluntario"]
            lartemporario.animal = novos_dados_lartemporario["animal"]
            lartemporario.data_entrada = novos_dados_lartemporario["data_entrada"]
            lartemporario.codigo = novos_dados_lartemporario["codigo"]
            self.lista_lartemporario()
        else:
            self.__tela_lartemporario.mostra_mensagem("ATENCAO: Lar Temporário não existente")

    def lista_lartemporario(self):
        for lartemporario in self.__lares:
            self.__tela_lartemporario.mostra_lartemporario({"voluntario": lartemporario.voluntario, "animal": lartemporario.animal, "data_entrada": lartemporario.data_entrada, "codigo": lartemporario.codigo})

    def excluir_lartemporario(self):
        self.lista_lartemporario()
        codigo_lartemporario = self.__tela_lartemporario.seleciona_lartemporario()
        lartemporario = self.pega_lartemporario_por_codigo(codigo_lartemporario)

        if lartemporario is not None:
            self.__lares.remove(lartemporario)
            self.lista_lartemporario()
        else:
            self.__tela_lartemporario.mostra_mensagem("ATENCAO: Lar Temporário não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_lartemporario, 2: self.altera_lartemporario, 3: self.lista_lartemporario, 4: self.excluir_lartemporario, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_lartemporario.tela_opcoes()]()
