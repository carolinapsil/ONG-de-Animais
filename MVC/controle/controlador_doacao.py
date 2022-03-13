import MVC.entidade.doador
from MVC.limite.tela_doacao import TelaDoacao
from MVC.entidade.doacao import Doacao
from MVC.entidade.doador import Doador


class ControladorDoacoes():
    def __init__(self, controlador_sistema):
        self.__doacoes = []
        self.__tela_doacao = TelaDoacao(self)
        self.__controlador_sistema = controlador_sistema

    def pega_doacao_por_codigo(self, codigo: int):
        for doacao in self.__doacoes:
            if(doacao.codigo == codigo):
                return doacao
        return None

    def incluir_doacao(self):
        self.__controlador_sistema.controlador_doador.lista_doadores()
        self.__controlador_sistema.controlador_doacao.lista_doacao()
        dados_doacao = self.__tela_doacao.pega_dados_doacao()
        if self.__controlador_sistema.controlador_doador.pega_doador_por_nome(dados_doacao["doador"]):
            doacao = Doacao(dados_doacao["doador"], dados_doacao["valor"], dados_doacao["data_doacao"],
                            dados_doacao["codigo"])
            self.__doacoes.append(doacao)
        else:
            self.__tela_doacao.mostra_mensagem("ATENCAO: Doador não cadastrado")

    def altera_doacao(self):
        self.lista_doacao()
        codigo_doacao = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_codigo(codigo_doacao)

        if(doacao is not None):
            novos_dados_doacao = self.__tela_doacao.pega_dados_doacao()
            if self.__controlador_sistema.controlador_doador.pega_doador_por_nome(novos_dados_doacao["doador"]):
                doacao.doador = novos_dados_doacao["doador"]
                doacao.valor = novos_dados_doacao["valor"]
                doacao.data_doacao = novos_dados_doacao["data_doacao"]
                doacao.codigo = novos_dados_doacao["codigo"]
                self.lista_doacao()
            else:
                self.__tela_doacao.mostra_mensagem("ATENCAO: Doador não cadastrado")
        else:
          self.__tela_doacao.mostra_mensagem("ATENCAO: Doacao não existente")

    def seleciona_doacao(self):
        self.__tela_doacao.mostra_lista_doacoes(self.__doacoes)
        codigo = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_codigo()(codigo)
        if doacao is not None:
            return doacao

    def lista_doacao(self):
        for doacao in self.__doacoes:
            self.__tela_doacao.mostra_doacao({"doador": doacao.doador, "data_doacao": doacao.data_doacao,
                                              "valor": doacao.valor, "codigo": doacao.codigo})

    def excluir_doacao(self):
        self.lista_doacao()
        codigo_doacao = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_codigo(codigo_doacao)

        if (doacao is not None):
            self.__doacoes.remove(doacao)
            self.lista_doacao()
        else:
            self.__tela_doacao.mostra_mensagem("ATENCAO: Doacao não existente")



    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_doacao, 2: self.altera_doacao, 3: self.lista_doacao, 4: self.excluir_doacao,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_doacao.open()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()