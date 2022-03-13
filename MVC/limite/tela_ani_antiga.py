class TelaAnimalAntiga:
    def tela_opcoes(self):
        print("-------- ANIMAIS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Animais")
        print("2 - Alterar Animais")
        print("3 - Listar Animais")
        print("4 - Excluir Animais")
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

    def pega_dados_animal(self):
        print("-------- DADOS ANIMAL ----------")

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
                chegada = input("Chegada: ")
                if chegada == "":
                    raise ValueError
                break
            except ValueError:
                print("Por favor, não deixe o campo vazio!")
        while True:
            try:
                ano_nascimento = input("ano_nascimento: ")
                if ano_nascimento == "" or ano_nascimento.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente com um número.")
        while True:
            try:
                sexo = input("Macho ou femea? ")
                if (sexo == "") or (sexo.lower() != "macho" and sexo.lower() != "femea" and sexo.lower() != "fêmea"):
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente com a opcao macho ou femea")
        while True:
            try:
                doenca = input("Possui alguma doenca? ")
                if doenca == "" or (doenca.lower() != "sim" and doenca.lower() != "nao" and doenca.lower() != "não"):
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente com sim ou nao")
        while True:
            try:
                vacina = input("Vacinado? ")
                if vacina == "" or (vacina.lower() != "sim" and vacina.lower() != "nao" and vacina.lower() != "não"):
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente com sim ou nao")
        while True:
            try:
                castracao = input("Castrado? ")
                if castracao == "" or (castracao.lower() != "sim" and \
                        castracao.lower() != "nao" and castracao.lower() != "não"):
                    raise ValueError
                break
            except ValueError:
                print("Por favor, preencha o campo corretamente com sim ou nao")

        return {"nome": nome, "chegada": chegada, "ano_nascimento": ano_nascimento, "sexo": sexo, "doenca": doenca, "vacina": vacina,
                "castracao": castracao}

    def mostra_animal(self, dados_animal):
        print("NOME DO ANIMAL: ", dados_animal["nome"])
        print("CHEGADA DO ANIMAL: ", dados_animal["chegada"])
        print("ANO DE NASCIMENTO DO ANIMAL: ", dados_animal["ano_nascimento"])
        print("O ANIMAL POSSUI DOENÇAS?: ", dados_animal["doenca"])
        print("VACINAS DO ANIMAL: ", dados_animal["vacina"])
        print("O ANIMAL É CASTRADO?: ", dados_animal["castracao"])
        print("\n")

    def seleciona_animal(self):
        nome = input("Nome do animal que deseja selecionar: ")
        return nome

    def mostra_mensagem(self, msg):
        print(msg)

#teste commit