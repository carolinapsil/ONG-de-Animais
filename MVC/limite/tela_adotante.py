class TelaAdotante():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- ADOTANTE ----------")
    print("Escolha a opcao")
    print("1 - Incluir Adotante")
    print("2 - Alterar Adotante")
    print("3 - Listar Adotante")
    print("4 - Excluir Adotante")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_adotante(self):
    print("-------- DADOS ADOTANTE ----------")
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    telefone = input("Telefone: ")
    genero = input("Gênero: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")

    return {"nome": nome, "data nascimento": data_nascimento, "telefone": telefone, "genero": genero, "email": email, "endereco": endereco}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_adotante(self, dados_adotante):
    print("NOME DO ADOTANTE: ", dados_adotante["nome"])
    print("IDADE DO ADOTANTE: ", dados_adotante["idade"])
    print("TELEFONE DO ADOTANTE: ", dados_adotante["telefone"])
    print("GÊNERO DO ADOTANTE: ", dados_adotante["nome"])
    print("E-MAIL DO ADOTANTE: ", dados_adotante["nome"])
    print("ENDEREÇO DO ADOTANTE: ", dados_adotante["nome"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_adotante(self):
    email = input("E-mail do adotante que deseja selecionar: ")
    return email

  def mostra_mensagem(self, msg):
    print(msg)