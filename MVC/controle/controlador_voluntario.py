from MVC.limite.tela_voluntario import TelaVoluntario
from MVC.entidade.voluntario import Voluntario


class ControladorVoluntario:
    def __init__(self, controlador_sistema):
        self.__voluntarios = []
        self.__tela_voluntario = TelaVoluntario
        self.__controlador_sistema = controlador_sistema

    def inicia(self):
        self.abre_tela()

    def pega_voluntario_por_telefone(self, telefone: str):
        for voluntario in self.__voluntarios:
            if voluntario.telefone == telefone:
                return voluntario
        return None

    def inclui_voluntario(self):
        dados_voluntario = self.__tela_voluntario.pega_dados_voluntario()
        voluntario = Voluntario(dados_voluntario["nome"], dados_voluntario["data_nascimento"], dados_voluntario["telefone"],
                                dados_voluntario["genero"], dados_voluntario["email"], dados_voluntario["endereco"], dados_voluntario["oferece_lt"])
        self.__voluntarios.append(voluntario)

    def altera_voluntario(self):
        self.lista_voluntarios()
        telefone_voluntario = self.__tela_voluntario.seleciona_voluntario(self)
        voluntario = self.pega_voluntario_por_telefone(telefone_voluntario)

        if voluntario is not None:
            novos_dados_voluntario = self.__tela_voluntario.pega_dados_voluntario()
            voluntario.nome = novos_dados_voluntario["nome"]
            voluntario.data_nascimento = novos_dados_voluntario["data_nascimento"]
            voluntario.telefone = novos_dados_voluntario["telefone"]
            voluntario.genero = novos_dados_voluntario["genero"]
            voluntario.email = novos_dados_voluntario["email"]
            voluntario.endereco = novos_dados_voluntario["endereco"]
            voluntario.oferece_lt = novos_dados_voluntario["oferece_lt"]
            self.lista_voluntarios()
        else:
            self.__tela_voluntario.mostra_mensagem("ATENCAO: voluntario não existente")

    def lista_voluntarios(self):
        for voluntario in self.__voluntarios:
            self.__tela_voluntario.mostra_voluntario(self, dados_voluntario={"nome": voluntario.nome, "data_nascimento": voluntario.data_nascimento,
                                                     "telefone": voluntario.telefone, "genero": voluntario.genero,
                                                     "email": voluntario.email, "endereco": voluntario.endereco,
                                                      "oferece_lt": voluntario.oferece_lt})

    def exclui_voluntario(self):
        self.lista_voluntarios()
        telefone_voluntario = self.__tela_voluntario.seleciona_voluntario(self)
        voluntario = self.pega_voluntario_por_telefone(telefone_voluntario)

        if voluntario is not None:
            self.__voluntarios.remove(voluntario)
            self.lista_voluntarios()
        else:
            self.__tela_voluntario.mostra_mensagem("ATENCAO: voluntario não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_voluntario, 2: self.altera_voluntario, 3: self.lista_voluntarios, 4: self.exclui_voluntario,
                        0: self.retornar}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_voluntario.tela_opcoes(self)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
