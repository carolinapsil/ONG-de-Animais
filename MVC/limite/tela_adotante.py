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

    def pega_dados_adotante(self):
        print("-------- DADOS ADOTANTE ----------")
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
        while True:
            try:
                idade = (input("Idade: "))
                if (idade.isnumeric() == False) or idade == "":
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente")

        return {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone,
                "genero": genero, "email": email, "endereco": endereco, "idade": int(idade)}

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
