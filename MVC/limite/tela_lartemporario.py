class TelaLarTemporario:
    def tela_opcoes(self):
        print("-------- Lar Temporário ----------")
        print("Escolha a opcao")
        print("1 - Incluir Lar Temporário")
        print("2 - Alterar Lar Temporário")
        print("3 - Listar Lar Temporário")
        print("4 - Excluir Lar Temporário")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_lartemporario(self):
        print("-------- DADOS Lar Temporário ----------")
        voluntario = input("Voluntário: ")
        animal = input("Animal: ")
        data_entrada = input("Data de Entrada: ")

        return {"voluntario": voluntario, "data_entrada": data_entrada, "animal": animal}

    def mostra_lartemporario(self, dados_lartemporario):
        print("Voluntário: ", dados_lartemporario["voluntario"])
        print("Animal: ", dados_lartemporario["animal"])
        print("Data de Entrada: ", dados_lartemporario["data_entrada"])
        print("\n")

    def seleciona_lartemporario(self):
        voluntario = input("Voluntario do Lar Temporario que deseja selecionar: ")
        return voluntario

    def mostra_mensagem(self, msg):
        print(msg)
