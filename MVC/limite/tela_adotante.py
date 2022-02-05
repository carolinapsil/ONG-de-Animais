class TelaAdotante:
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

    def pega_dados_adotante(self):
        print("-------- DADOS ADOTANTE ----------")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        telefone = input("Telefone: ")
        genero = input("Genero: ")
        email = input("E-mail: ")
        endereco = input("Endereco: ")

        return {"nome": nome, "data nascimento": data_nascimento, "telefone": telefone, "genero": genero, "email": email, "endereco": endereco}

    def mostra_adotante(self, dados_adotante):
        print("NOME DO ADOTANTE: ", dados_adotante["nome"])
        print("IDADE DO ADOTANTE: ", dados_adotante["idade"])
        print("TELEFONE DO ADOTANTE: ", dados_adotante["telefone"])
        print("GENERO DO ADOTANTE: ", dados_adotante["nome"])
        print("E-MAIL DO ADOTANTE: ", dados_adotante["nome"])
        print("ENDERECO DO ADOTANTE: ", dados_adotante["nome"])
        print("\n")

    def seleciona_adotante(self):
        email = input("E-mail do adotante que deseja selecionar: ")
        return email

    def mostra_mensagem(self, msg):
        print(msg)
