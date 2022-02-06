from MVC.limite.tela_adotante import TelaAdotante
from MVC.entidade.adotante import Adotante

class ControladorAdotante():
    def __init__(self, controlador_sistema):
        self.__adotantes = []
        self.__tela_adotante = TelaAdotante
        self.__controlador_sistema = controlador_sistema

    def inicia(self):
        self.abre_tela_inicial()

    def pega_adotante_por_telefone(self, telefone: str):
        for adotante in self.__adotantes:
            if adotante.telefone == telefone:
                return adotante
        return None

    def inclui_adotante(self):
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        adotante = Adotante(dados_adotante["nome"],dados_adotante["data_nascimento"], dados_adotante["telefone"],
                            dados_adotante["genero"], dados_adotante["email"], dados_adotante["endereco"])
        self.__adotantes.append(adotante)

    def altera_adotante(self):
        self.lista_adotantes()
        telefone_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_telefone(telefone_adotante)

        if(adotante is not None):
          novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()
          adotante.nome = novos_dados_adotante["nome"]
          adotante.data_nascimento = novos_dados_adotante["data_nascimento"]
          adotante.telefone = novos_dados_adotante["telefone"]
          adotante.genero = novos_dados_adotante["genero"]
          adotante.email = novos_dados_adotante["email"]
          adotante.endereco = novos_dados_adotante["endereco"]
          self.lista_adotantes()
        else:
          self.__tela_adotante.mostra_mensagem("ATENCAO: Adotante não existente")

    def lista_adotantes(self):
        for adotante in self.__adotantes:
            self.__tela_adotante.mostra_adotante({"nome": adotante.nome, "data_nascimento": adotante.data_nascimento,
                                                  "telefone": adotante.telefone, "genero": adotante.genero, "email":
                                                      adotante.email, "endereco": adotante.endereco})

    def exclui_adotante(self):
        self.lista_adotantes()
        telefone_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_telefone(telefone_adotante)

        if (adotante is not None):
            self.__adotantes.remove(adotante)
            self.lista_adotantes()
        else:
            self.__tela_adotante.mostra_mensagem("ATENCAO: Adotante não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def mostra_opcoes(self):
        self.__tela_adotante.tela_opcoes()

    def abre_tela(self):
        self.mostra_opcoes()
        lista_opcoes = {1: self.inclui_adotante, 2: self.altera_adotante, 3: self.lista_adotante, 4: self.exclui_adotante,
                        0: self.retornar}
        continua = True
        while continua:
            opcao_escolhida = self.__tela_doacao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
