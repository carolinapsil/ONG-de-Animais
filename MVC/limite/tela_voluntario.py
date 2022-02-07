class TelaVoluntario:
    def tela_opcoes(self):
        print("-------- VOLUNTARIO ----------")
        print("Escolha a opcao")
        print("1 - Incluir Voluntario")
        print("2 - Alterar Voluntario")
        print("3 - Listar Voluntario")
        print("4 - Excluir Voluntario")
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

    def pega_dados_voluntario(self):
        print("-------- DADOS VOLUNTARIO ----------")

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
                oferece_lt = input("Oferece lar temporario? ")
                if oferece_lt.lower() != "sim" or oferece_lt.lower() != "nao" or oferece_lt.lower() != "não":
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente")

        return {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone, "genero": genero,
                "email": email, "endereco": endereco, "oferece_lt": oferece_lt}

    def mostra_voluntario(self, dados_voluntario):
        print("NOME DO VOLUNTARIO: ", dados_voluntario["nome"])
        print("DATA NASCIMENTO DO VOLUNTARIO: ", dados_voluntario["data_nascimento"])
        print("TELEFONE DO VOLUNTARIO: ", dados_voluntario["telefone"])
        print("GENERO DO VOLUNTARIO: ", dados_voluntario["genero"])
        print("E-MAIL DO VOLUNTARIO: ", dados_voluntario["email"])
        print("ENDERECO DO VOLUNTARIO: ", dados_voluntario["endereco"])
        print("OFERECE LAR TEMPORARIO: ", dados_voluntario["oferece_lt"])
        print("\n")

    def seleciona_voluntario(self):
        telefone_voluntario = input("Telefone do voluntario que deseja selecionar: ")
        return telefone_voluntario

    def mostra_mensagem(self, msg):
        print(msg)
