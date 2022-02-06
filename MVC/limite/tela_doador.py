#from MVC.controle.controlador_doador import ControladorDoador


class TelaDoador():

    def __init__(self, controlador_doador):
        self.__controlador_doador = ControladorDoador()

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

    def pega_dados_doador(self):
        print("-------- DADOS DOADOR ----------")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        telefone = input("Telefone: ")
        genero = input("Genero: ")
        email = input("E-mail: ")
        endereco = input("Endereco: ")

        return {"nome": nome, "data nascimento": data_nascimento, "telefone": telefone,
                "genero": genero, "email": email, "endereco": endereco}

    def mostra_doador(self, dados_doador):
        print("NOME DO DOADOR: ", dados_doador["nome"])
        print("IDADE DO DOADOR: ", dados_doador["idade"])
        print("TELEFONE DO DOADOR: ", dados_doador["telefone"])
        print("GENERO DO DOADOR: ", dados_doador["nome"])
        print("E-MAIL DO DOADOR: ", dados_doador["nome"])
        print("ENDERECO DO DOADOR: ", dados_doador["nome"])
        print("\n")

    def excluir_doador(self):
        self.lista_doadores()
        telefone_doador = self.__tela_doador.seleciona_doador()
        doador = self.pega_doador_por_telefone(telefone_doador)

        if doador is not None:
            self.__doadores.remove(doador)
            self.lista_doadores()
        else:
            self.__tela_doador.mostra_mensagem("ATENCAO: Doador não existente")

    def seleciona_doador(self):
        telefone = input("Telefone do doador que deseja selecionar: ")
        return telefone

    def mostra_mensagem(self, msg):
        print(msg)
