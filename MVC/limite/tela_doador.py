#from MVC.controle.controlador_doador import ControladorDoador


class TelaDoador():

    def __init__(self, controlador_doador):
        self.__controlador_doador = controlador_doador

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

        return {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone,
                "genero": genero, "email": email, "endereco": endereco}

    def mostra_doador(self, dados_doador):
        print("NOME DO DOADOR: ", dados_doador["nome"])
        print("DATA DE NASCIMENTO DO DOADOR: ", dados_doador["data_nascimento"])
        print("TELEFONE DO DOADOR: ", dados_doador["telefone"])
        print("GENERO DO DOADOR: ", dados_doador["genero"])
        print("E-MAIL DO DOADOR: ", dados_doador["email"])
        print("ENDERECO DO DOADOR: ", dados_doador["endereco"])
        print("\n")

    def seleciona_doador(self):
        telefone = input("Telefone do doador que deseja selecionar: ")
        return telefone

    def mostra_mensagem(self, msg):
        print(msg)
