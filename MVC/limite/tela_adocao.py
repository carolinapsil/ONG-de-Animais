class TelaAdocao:
    def tela_opcoes(self):
        print("-------- ADOÇÃO ----------")
        print("Escolha a opcao")
        print("1 - Incluir Adoção")
        print("2 - Alterar Adoção")
        print("3 - Listar Adoção")
        print("4 - Excluir Adoção")
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

    def pega_dados_adocao(self):
        print("-------- DADOS ADOÇÃO ----------")
        adotante = input("Adotante: ")
        animal = input("Animal: ")
        data = input("Data de Adocao: ")
        codigo = input("Codigo da Adocao: ")

        return {"adotante": adotante, "animal": animal, "data": data, "codigo": codigo}

    def mostra_adocao(self, dados_adocao):
        print("ADOTANTE: ", dados_adocao["adotante"])
        print("ANIMAL: ", dados_adocao["animal"])
        print("DATA DA ADOÇÃO: ", dados_adocao["data"])
        print("CODIGO DA ADOÇÃO: ", dados_adocao["codigo"])
        print("\n")

    def mostra_lista_adocoes(self, adocoes):
        print("-------- LISTA DE ADOÇOES --------")
        for adocao in adocoes:
            print("ADOTANTE: ", adocao.adotante)
            print("ANIMAL: ", adocao.animal)
            print("DATA DA ADOÇAO: ", adocao.data)
            print("CODIGO DA ADOÇAO: ", adocao.codigo)
            print("\n")

    def seleciona_adocao(self):
        codigo = input("Codigo da Adoção que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
