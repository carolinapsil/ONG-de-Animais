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

        while True:

            try:
                opcoes_validas = [0, 1, 2, 3]
                opcao = int(input("Escolha uma opção: "))
                print('\n')
                if opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print('Opcao invalida!')
                print('\n')

    def pega_dados_doador(self):
        print("-------- DADOS DOADOR ----------")

        while True:
            try:
                nome = input("Nome: ")
                if nome == "":
                    raise ValueError
                break
            except ValueError:
                print("Por favor, não deixe o campo vazio!")
        while True:
            try:
                data_nascimento = input("Data de nascimento: ")
                if data_nascimento == "":
                    raise ValueError
                break
            except ValueError:
                print("Por favor, não deixe o campo vazio!")
        while True:
            try:
                telefone = input("Telefone: ")
                if telefone == "":
                    raise ValueError
                break
            except ValueError:
                print("Por favor, não deixe o campo vazio!")
        while True:
            try:
                genero = input("Genero: ")
                if (genero == "") or (genero.lower() != "feminino" and genero.lower() != "masculino"):
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente.")
        while True:
            try:
                email = input("E-mail: ")
                if (email == "") or ('@' not in email) or '.' not in email:
                    raise ValueError
                break
            except ValueError:
                print("E-mail invalido! Por favor, preencha o campo corretamente.")
        while True:
            try:
                endereco = input("Endereco: ")
                if endereco == "":
                    raise ValueError
                break
            except ValueError:
                print("Por favor, não deixe o campo vazio!")

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
