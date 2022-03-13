from MVC.limite.tela_animal import TelaAnimal
from MVC.entidade.animal import Animal
from MVC.controle.controlador_doacao import ControladorDoacoes

class ControladorAnimal:

        def __init__(self, controlador_sistema):
                self.__animais = []
                self.__tela_animal = TelaAnimal()
                self.__controlador_sistema = controlador_sistema

        def pega_animal_por_nome(self, nome: str):
            for animal in self.__animais:
                if animal.nome == nome:
                    return animal
                return None

        def incluir_animal(self):
            dados_animal = self.__tela_animal.pega_dados_animal()
            if not self.__controlador_sistema.controlador_animal.pega_animal_por_nome(dados_animal["nome"]):
                animal = Animal(dados_animal["nome"], dados_animal["chegada"], dados_animal["ano_nascimento"],
                                dados_animal["sexo"], dados_animal["doenca"], dados_animal["vacina"],
                                dados_animal["castracao"])
                if animal.vacina.lower() == "sim" and animal.castracao.lower() == "sim":
                    self.__animais.append(animal)
                else:
                    self.__tela_animal.mostra_mensagem("ATENCAO: Para inclusao de animais, é preciso que ele esteja "
                                                       "castrado e vacinado")
            else:
                self.__tela_animal.mostra_mensagem("Já existe um animal cadastrado com esse nome! Por favor, tente outro")

        def alterar_animal(self):
            self.lista_animais()
            nome_animal = self.__tela_animal.seleciona_animal()
            animal = self.pega_animal_por_nome(nome_animal)

            if animal is not None:
                novos_dados_animal = self.__tela_animal.pega_dados_animal()
                animal.nome = novos_dados_animal["nome"]
                animal.chegada = novos_dados_animal["chegada"]
                animal.ano_nascimento = novos_dados_animal["ano_nascimento"]
                animal.sexo = novos_dados_animal["sexo"]
                animal.doenca = novos_dados_animal["doenca"]
                animal.vacina = novos_dados_animal["vacina"]
                animal.castracao = novos_dados_animal["castracao"]
                self.lista_animais()
            else:
                self.__tela_animal.mostra_mensagem("ATENCAO: Animal não existente")

        def lista_animais(self):
            for animal in self.__animais:
                self.__tela_animal.mostra_animal({"nome": animal.nome, "chegada": animal.chegada, "ano_nascimento": animal.ano_nascimento,
                                                "sexo": animal.sexo, "doenca": animal.doenca, "vacina": animal.vacina, "castracao": animal.castracao})


        def excluir_animal(self):
            self.lista_animais()
            nome = self.__tela_animal.seleciona_animal()
            animal = self.pega_animal_por_nome(nome)

            if animal is not None:
                self.__animais.remove(animal)
                self.lista_animais()
            else:
                self.__tela_animal.mostra_mensagem("ATENCAO: Animal não existente")

        def retornar(self):
            self.__controlador_sistema.abre_tela()

        def abre_tela(self):
            lista_opcoes = {1: self.incluir_animal, 2: self.alterar_animal, 3: self.lista_animais, 4: self.excluir_animal, 0: self.retornar}
            continua = True
            while continua:
                lista_opcoes[self.__tela_animal.tela_opcoes()]()

        def animais_disponiveis(self):
            lista_disponiveis = []
            for animal in self.__animais:
                if not self.__controlador_sistema.controlador_adocao.pega_adocao_por_animal(animal.nome):
                    lista_disponiveis.append(animal.nome)
                    self.__tela_animal.mostra_mensagem(animal.nome)
