from MVC.limite.tela_doador import TelaDoador
from MVC.entidade.doador import Doador

class ControladorDoador():
    def __init__(self, controlador_sistema):
        self.__doadores = []
        self.__tela_doador = TelaDoador(self)
        self.__controlador_sistema = controlador_sistema

    def inicia(self):
        self.abre_tela()

    def pega_doador_por_telefone(self, telefone: str):
        for doador in self.__doadores:
            if (doador.telefone == telefone):
                return doador
        return None

    def pega_doador_por_nome(self, nome: str):
        for doador in self.__doadores:
            if (doador.nome == nome):
                return doador
        return None

    def inclui_doador(self):
        dados_doador = self.__tela_doador.abrir_cadastro_doador()
        doador = Doador(dados_doador["nome"],dados_doador["data_nascimento"], dados_doador["telefone"],
                            dados_doador["genero"], dados_doador["email"], dados_doador["endereco"])
        self.__doadores.append(doador)

    def lista_doadores(self):
        for doador in self.__doadores:
            self.__tela_doador.abrir_mostra_doador()

    def altera_doador(self):
        self.lista_doadores()
        telefone_doador = self.__tela_doador.seleciona_doador(self)
        doador = self.pega_doador_por_telefone(telefone_doador)

        if(doador is not None):
            novos_dados_doador = self.__tela_doador.pega_dados_doador(self)
            doador.nome = novos_dados_doador["nome"]
            doador.data_nascimento = novos_dados_doador["data_nascimento"]
            doador.telefone = novos_dados_doador["telefone"]
            doador.genero = novos_dados_doador["genero"]
            doador.email = novos_dados_doador["email"]
            doador.endereco = novos_dados_doador["endereco"]
            self.lista_doadores()
        else:
            self.__tela_doador.mostra_mensagem("ATENCAO: Doador não existente")

    def exclui_doador(self):
        self.lista_doadores()
        telefone_doador = self.__tela_doador.seleciona_doador(self)
        doador = self.pega_doador_por_telefone(telefone_doador)

        if (doador is not None):
            self.__doadores.remove(doador)
            self.lista_doadores()
        else:
            self.__tela_doador.mostra_mensagem("ATENCAO: Doador não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_doador, 2: self.altera_doador, 3: self.lista_doadores, 4: self.exclui_doador,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_doador.open()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
