from MVC.limite.tela_adocao import TelaAdocao
from MVC.entidade.adocao import Adocao


class ControladorAdocao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__adocoes = []
        self.__tela_adocao = TelaAdocao(self)

    def pega_adocao_por_codigo(self, codigo: str):
        for adocao in self.__adocoes:
            if adocao.codigo == codigo:
                return adocao
        return None

    def incluir_adocao(self):
        dados_adocao = self.__tela_adocao.pega_dados_adocao()
        #if self.__controlador_sistema.controlador_adotante.pega_adotante_por_nome(dados_adocao["adotante"]) \
         #       and self.__controlador_sistema.controlador_animal.pega_animal_por_nome(dados_adocao["animal"]):
          #  adocao = Adocao(dados_adocao["adotante"], dados_adocao["animal"], dados_adocao["data"], dados_adocao["codigo"])
           # self.__adocoes.append(adocao)
        if self.__controlador_sistema.controlador_adotante.pega_adotante_por_nome(dados_adocao["adotante"])\
                and self.__controlador_sistema.controlador_animal.pega_animal_por_nome(dados_adocao["animal"]):
            adocao = Adocao(dados_adocao["adotante"], dados_adocao["animal"],
                                          dados_adocao["data"], dados_adocao["codigo"])
            self.__adocoes.append(adocao)
        else:
            self.__tela_adocao.mostra_mensagem("ATENCAO: Adotante e/ou animal não cadastrado")

    def altera_adocao(self):
        self.lista_adocao()
        codigo_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_codigo(codigo_adocao)

        if adocao is not None:
            novos_dados_adocao = self.__tela_adocao.pega_dados_adocao()
            if self.__controlador_sistema.controlador_adotante.pega_adotante_por_nome(novos_dados_adocao["adotante"])\
                and self.__controlador_sistema.controlador_animal.pega_animal_por_nome(novos_dados_adocao["animal"]):
                adocao.adotante = novos_dados_adocao["adotante"]
                adocao.animal = novos_dados_adocao["animal"]
                adocao.data = novos_dados_adocao["data"]
                adocao.codigo = novos_dados_adocao["codigo"]
                self.lista_adocao()
            else:
                self.__tela_adocao.mostra_mensagem("Adotante e/ou animal não cadastrado")
        else:
            self.__tela_adocao.mostra_mensagem("ATENCAO: Adoção não existente")

    def lista_adocao(self):
        for adocao in self.__adocoes:
            self.__tela_adocao.mostra_adocao({"adotante": adocao.adotante, "animal": adocao.animal, "data": adocao.data,
                                              "codigo": adocao.codigo})

    def lista_adotados(self):
        adotados = []
        for adocao in self.__adocoes:
            adotados.append(adocao.animal)
        return adotados

    def pega_adocao_por_animal(self, animal: str):
        for adocao in self.__adocoes:
            if adocao.animal == animal:
                return adocao
        return None

    def excluir_adocao(self):
        self.lista_adocao()
        codigo_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_codigo(codigo_adocao)

        if adocao is not None:
            self.__adocoes.remove(adocao)
            self.lista_adocao()
        else:
            self.__tela_adocao.mostra_mensagem("ATENCAO: Adoção não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adocao, 2: self.altera_adocao, 3: self.lista_adocao, 4: self.excluir_adocao, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_adocao.open()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
