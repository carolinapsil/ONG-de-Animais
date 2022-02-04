class TelaDoador():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- DOADOR ----------")
    print("Escolha a opcao")
    print("1 - Incluir Doador")
    print("2 - Alterar Doador")
    print("3 - Listar Doador")
    print("4 - Excluir Doador")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_doador(self):
    print("-------- DADOS DOADOR ----------")
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    telefone = input("Telefone: ")
    genero = input("Genero: ")
    email = input("E-mail: ")
    endereco = input("Endereco: ")

    return {"nome": nome, "data nascimento": data_nascimento, "telefone": telefone, "genero": genero, "email": email, "endereco": endereco}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_adotante(self, dados_doador):
    print("NOME DO DOADOR: ", dados_doador["nome"])
    print("IDADE DO DOADOR: ", dados_doador["idade"])
    print("TELEFONE DO DOADOR: ", dados_doador["telefone"])
    print("GENERO DO DOADOR: ", dados_doador["nome"])
    print("E-MAIL DO DOADOR: ", dados_doador["nome"])
    print("ENDERECO DO DOADOR: ", dados_doador["nome"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_doador(self):
    email = input("E-mail do doador que deseja selecionar: ")
    return email

  def mostra_mensagem(self, msg):
    print(msg)
