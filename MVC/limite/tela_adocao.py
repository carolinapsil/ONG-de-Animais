class TelaAdocao:


    def tela_opcoes(self):
        print("-------- ADOÇÃO ----------")
        print("Escolha a opcao")
        print("1 - Incluir Adoção")
        print("2 - Alterar Adoção")
        print("3 - Listar Adoção")
        print("4 - Excluir Adoção")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_adocao(self):
        print("-------- DADOS ADOÇÃO ----------")
        adotante = input("Adotante: ")
        animal = input("Animal: ")
        data = input("Data de Adocao: ")
        codigo = input("Codigo da doacao: ")

        return {"adotante": adotante, "animal": animal, "data": data, "codigo": codigo}

    def mostra_adocao(self, dados_adocao):
        print("ADOTANTE: ", dados_adocao["adotante"])
        print("ANIMAL: ", dados_adocao["animal"])
        print("DATA DA ADOÇÃO: ", dados_adocao["data"])
        print("\n")

    def seleciona_adocao(self):
        codigo = input("Codigo da Adoção que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
