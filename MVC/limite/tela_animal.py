class TelaAnimal:
    def tela_opcoes(self):
        print("-------- ANIMAIS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Animais")
        print("2 - Alterar Animais")
        print("3 - Listar Animais")
        print("4 - Excluir Animais")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))

        return opcao

    def pega_dados_animal(self):
        print("-------- DADOS ANIMAL ----------")
        nome = input("Nome: ")
        chegada = input("Chegada: ")
        ano_nascimento = input("ano_nascimento: ")
        sexo = input("sexo: ")
        doenca = input("doenca: ")
        vacina = input("vacina: ")
        castracao = input("castracao: ")

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
