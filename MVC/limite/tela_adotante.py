#from MVC.entidade.adotante import Adotante
#from MVC.controle.controlador_adotante import ControladorAdotante

class TelaAdotante:

    def __init__(self, controlador_adotante):
        self.__controlador_adotante = controlador_adotante

    def tela_opcoes(self):
        print("-------- ADOTANTE ----------")
        print("Escolha a opcao")
        print("1 - Incluir Adotante")
        print("2 - Alterar Adotante")
        print("3 - Listar Adotante")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_adotante(self):
        print("-------- DADOS ADOTANTE ----------")
        nome = input("Nome: ")
        data_nascimento = input("data_nascimento: ")
        telefone = input("Telefone: ")
        genero = input("Genero: ")
        email = input("E-mail: ")
        endereco = input("Endereco: ")
        idade = input("Idade: ")

        return {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone,
                "genero": genero, "email": email, "endereco": endereco, "idade": idade}

    def mostra_adotante(self, dados_adotante):
        print("NOME DO ADOTANTE: ", dados_adotante["nome"])
        print("data nascimento DO ADOTANTE: ", dados_adotante["data_nascimento"])
        print("TELEFONE DO ADOTANTE: ", dados_adotante["telefone"])
        print("GENERO DO ADOTANTE: ", dados_adotante["genero"])
        print("E-MAIL DO ADOTANTE: ", dados_adotante["email"])
        print("ENDERECO DO ADOTANTE: ", dados_adotante["endereco"])
        print("IDADE DO ADOTANTE: "), dados_adotante["idade"]
        print("\n")

    def lista_adotantes(self):
        for adotante in self.__adotantes:
            self.__tela_adotante.mostra_adotante({"nome": adotante.nome, "data_nascimento": adotante.data_nascimento,
                                                  "telefone": adotante.telefone, "genero": adotante.genero,
                                                  "email": adotante.email, "endereco": adotante.endereco,
                                                  "idade": adotante.idade})

    def seleciona_adotante(self):
        telefone_adotante = input("Telefone do adotante que deseja selecionar: ")
        return telefone_adotante

    def mostra_mensagem(self, msg):
        print(msg)
