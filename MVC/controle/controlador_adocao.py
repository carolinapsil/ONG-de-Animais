from limite.tela_adocao import TelaAdocao
from entidade.adocao import Adocao


class ControladorAdocao:

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__adocoes = []
    self.__tela_adocao = TelaAdocao()

  def pega_adocao_por_codigo(self, codigo: int):
    for adocao in self.__adocoes:
      if(adocao.codigo == codigo):
        return adocao
    return None

  def incluir_adocao(self):
        dados_adocao = self.__tela_adocao.pega_dados_adocao()
        adocao = Adocao(dados_adocao["adotante"],dados_adocao["animal"], dados_adocao["data"])
        self.__adocoes.append(adocao)

  def lista_adocao(self):
    for e in self.__adocoes:
      self.__tela_adocao.mostra_adocao({"adotante": e.adotante,
                                                "animal": e.animal,
                                                "data": e.data)

  def excluir_adocao(self):
    self.lista_adocao()
    codigo_adocao = self.__tela_adocao.seleciona_adocao()
    adocao = self.pega_adocao_por_codigo(int(codigo_adocao))

    if adocao is not None:
      self.__adocoes.remove(adocao)
      self.lista_adocao()
    else:
      self.__tela_adocao.mostra_mensagem("ATENCAO: Adoção não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_adocao, 2: self.lista_adocao, 3: self.excluir_adocao,0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_adocao.tela_opcoes()]()
