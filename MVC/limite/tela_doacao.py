#from MVC.controle.controlador_doacao import ControladorDoacoes


class TelaDoacao:

    def __init__(self, controlador_doacao):
        self.__controlador_doacao = controlador_doacao

    def tela_opcoes(self):
        print("-------- DOACAO ----------")
        print("Escolha a opcao")
        print("1 - Incluir Doacao")
        print("2 - Alterar Doacao")
        print("3 - Listar Doacao")
        print("4 - Excluir Doacao")
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

    def pega_dados_doacao(self):
        print("-------- DADOS DOACAO ----------")

        while True:
            try:
                doador = input("Doador: ")
                if (doador == "") or (doador.isalpha() == False):
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente")
        while True:
            try:
                valor = input("Valor doado: ")
                if valor == "" or (valor.isnumeric() == False):
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente")
        while True:
            try:
                data_doacao = input("Data de doacao: ")
                if data_doacao == "" or data_doacao.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente")
        while True:
            try:
                codigo = input("Codigo da doacao: ")
                if codigo == "" or codigo.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente")

        return {"doador": doador, "valor": valor, "data_doacao": data_doacao, "codigo": codigo}

    def mostra_doacao(self, dados_doacao):
        print("DOADOR: ", dados_doacao["doador"])
        print("VALOR DA DOACAO: ", dados_doacao["valor"])
        print("DATA DA DOACAO: ", dados_doacao["data_doacao"])
        print("CODIGO DA DOACAO: "), dados_doacao["codigo"]
        print("\n")

    def mostra_lista_doacoes(self, doacoes):
        print("-------- LISTA DE DOACOES --------")
        for doacao in doacoes:
            print("DOADOR: ", doacao.doador.nome)
            print("VALOR DA DOACAO: ", doacao.valor)
            print("DATA DA DOACAO: ", doacao.data_doacao)
            print("CODIGO DA DOACAO: ", doacao.codigo)
            print("\n")

    def seleciona_doacao(self):
        codigo = input("Codigo da doacao que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
