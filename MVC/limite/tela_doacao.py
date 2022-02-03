class TelaDoacao():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- DOAÇÃO ----------")
    print("Escolha a opcao")
    print("1 - Incluir Doação")
    print("2 - Alterar Doação")
    print("3 - Listar Doação")
    print("4 - Excluir Doação")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_doacao(self):
    print("-------- DADOS DOAÇÃO ----------")
    doador = input("Doador: ")
    valor = input("Valor doado: ")
    data_doacao = input("Data de doação: ")
    codigo = input("Código da doação: ")

    return {"doador": doador, "valor": valor, "data_doacao": data_doacao, "codigo": codigo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_doacao(self, dados_doacao):
    print("DOADOR: ", dados_doacao["doador"])
    print("VALOR DA DOAÇÃO: ", dados_doacao["valor"])
    print("DATA DA DOAÇÃO: ", dados_doacao["data_doacao"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_doacao(self):
    codigo = input("Código da doação que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)