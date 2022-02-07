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
        voluntario = input("Voluntario: ")
        animal = input("Animal: ")
        data_entrada = input("Data de Entrada: ")
        codigo = input("Codigo do Lar Temporario: ")

        return {"voluntario": voluntario, "animal": animal, "data_entrada": data_entrada, "codigo": codigo}

    def mostra_lartemporario(self, dados_lartemporario):
        print("voluntario: ", dados_lartemporario["voluntario"])
        print("Animal: ", dados_lartemporario["animal"])
        print("DATA: ", dados_lartemporario["data_entrada"])
        print("CODIGO: ", dados_lartemporario["codigo"])
        print("\n")

    def mostra_lista_lartemporario(self, lares):
        print("-------- LISTA DE LARES TEMPORARIOS --------")
        for lartemporario in lares:
            print("voluntario: ", lartemporario.voluntario)
            print("Animal: ", lartemporario.animal)
            print("Data: ", lartemporario.data_entrada)
            print("Codigo: ", lartemporario.codigo)
            print("\n")

    def seleciona_lartemporario(self):
        codigo = input("Codigo da Lar Temporario que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
