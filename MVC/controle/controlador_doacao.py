from MVC.limite.tela_doacao import TelaDoacao
from MVC.entidade.doacao import Doacao

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

        doador = self.__controlador_sistema.controlador_doacao.pega_doacao_por_codigo(dados_doacao["doador"])
        valor = self.__controlador_sistema.controlador_doacao.pega_doacao_por_codigo(dados_doacao["valor"])
        data_doacao = self.__controlador_sistema.controlador_doacao.pega_doacao_por_codigo(dados_doacao["data_doacao"])
        codigo = self.__controlador_sistema.controlador_doacao.pega_doacao_por_codigo(dados_doacao["codigo"])
        doacao = Doacao(doador, valor, data_doacao, codigo)
        self.__doacoes.append(doacao)

    def altera_doacao(self):
        self.lista_doacao()
        codigo_doacao = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_codigo(codigo_doacao)

        if(doacao is not None):
          novos_dados_doacao = self.__tela_doacao.pega_dados_doacao()
          doacao.doador = novos_dados_doacao["doador"]
          doacao.valor = novos_dados_doacao["valor"]
          doacao.data_doacao = novos_dados_doacao["data_doacao"]
          doacao.codigo = novos_dados_doacao["codigo"]
          self.lista_doacao()
        else:
          self.__tela_doacao.mostra_mensagem("ATENCAO: Doacao não existente")

    def seleciona_doacao(self):
        self.__tela_doacao.mostra_lista_doacoes(self.__doacoes)
        codigo = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_codigo()(codigo)
        if doacao is not None:
            return doacao

    def lista_doacao(self):
        for i in self.__doacoes:
            self.__tela_doacao.mostra_doacao({"doador": i.doador.nome,
                                              "data_doacao": i.data_doacao,
                                              "valor": i.valor,
                                              "codigo": i.codigo})

    def excluir_doacao(self):
        self.lista_doacao()
        codigo_doacao = self.__tela_doacao.seleciona_doacao()
        doacao = self.pega_doacao_por_codigo(int(codigo_doacao))

        if (doacao is not None):
            self.__doacoes.remove(doacao)
            self.lista_doacao()
        else:
            self.__tela_doacao.mostra_mensagem("ATENCAO: Doacao não existente")

    def mostra_opcoes(self):
        self.__tela_doacao.tela_opcoes()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        self.mostra_opcoes()
        lista_opcoes = {1: self.incluir_doacao(), 2: self.altera_doacao(), 3: self.lista_doacao, 4: self.excluir_doacao(),
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_doacao.tela_opcoes()]()
       # while True:
        #    opcao_escolhida = self.__tela_doacao.tela_opcoes()
         #   funcao_escolhida = lista_opcoes[opcao_escolhida]
          #  funcao_escolhida()
