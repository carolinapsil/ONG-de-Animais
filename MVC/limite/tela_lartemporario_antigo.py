class TelaLarTemporario:
    def tela_opcoes(self):
        print("-------- Lar Temporário ----------")
        print("Escolha a opcao")
        print("1 - Incluir Lar Temporário")
        print("2 - Alterar Lar Temporário")
        print("3 - Listar Lar Temporário")
        print("4 - Excluir Lar Temporário")
        print("0 - Retornar")

        while True:

            try:
                opcoes_validas = [0, 1, 2, 3, 4]
                opcao = int(input("Escolha uma opção: "))
                print('\n')
                if opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print('Opcao invalida!')
                print('\n')

    def pega_dados_lartemporario(self):
        print("-------- DADOS Lar Temporário ----------")

        while True:
            try:
                voluntario = input("Voluntario: ")
                if voluntario == "":
                    raise ValueError
                break
            except ValueError:
                print("Por favor, não deixe o campo vazio!")
        while True:
            try:
                animal = input("Animal: ")
                if animal == "":
                    raise ValueError
                break
            except ValueError:
                print("Por favor, não deixe o campo vazio!")
        while True:
            try:
                data_entrada = input("Data de entrada: ")
                if data_entrada == "" or data_entrada.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente")
        while True:
            try:
                codigo = input("Codigo do Lar Temporario: ")
                if codigo == "" or codigo.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente")

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
