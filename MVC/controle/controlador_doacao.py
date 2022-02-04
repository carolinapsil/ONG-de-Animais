from MVC.limite.tela_doacao import TelaDoacao
from MVC.entidade.doacao import Doacao

class ControladorDoacoes():
    def __init__(self, controlador_sistema):
        self.__doacoes = []
        self.__tela_doacoes = TelaDoacao
        self.__controlador_sistema = controlador_sistema

    def pega_doacao_por_codigo(self, codigo: int):
        for doacao in self.__doacoes:
            if(doacao.codigo == codigo):
                return doacao
        return None

    def incluir_doacao(self):
        self.__controlador_sistema.controlador_doadores.lista_doadores()
        self.__controlador_sistema.controlador_doacoes.lista_doacao()
        dados_doacao = self.__tela_doacoes.pega_dados_doacao()

    def excluir_doacao(self):
        self.lista_doacao()
        codigo_doacao = self.__tela_doacoes.seleciona_doacao()
        doacao = self.pega_doacao_por_codigo(int(codigo_doacao))

        if (doacao is not None):
            self.__doacoes.remove(doacao)
            self.lista_doacao()
        else:
            self.__tela_doacoes.mostra_mensagem("ATENCAO: Doacao não existente")
