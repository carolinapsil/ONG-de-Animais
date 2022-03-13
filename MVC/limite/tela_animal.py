import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button


class TelaAnimal:

    def __init__(self, controlador_animal):
        self.__controlador_animal = controlador_animal
        self.__window = None
        self.__window2 = None
        self.init_components()

    @property
    def window(self):
        return self.__window

    @property
    def window2(self):
        return self.__window2

    def init_components(self):
        sg.ChangeLookAndFeel('BlueMono')

        botoes = [
                    [sg.Button('Incluir', size=(20, 2), key=1, button_color='#7B68EE')],
                    [sg.Button('Alterar', size=(20, 2), key=2, button_color='#7B68EE')],
                    [sg.Button('Listar', size=(20, 2), key=3, button_color='#7B68EE')],
                    [sg.Button('Excluir', size=(20, 2), key=4, button_color='#7B68EE')],
                    [sg.Button('Retornar', size=(20, 2), key=0, button_color='#7B68EE')]
        ]

        layout = [
                    [sg.Text("ANIMAIS", justification='center', size=(20, 1), font=("Helvetica", 25))],
                    [sg.Text("O que deseja fazer?", justification='center', size=(15, 1), font=("Helvetica", 25))],
                    [sg.Column(botoes, vertical_alignment='center', justification='center')]
        ]

        self.__window = sg.Window('Tela Animais', default_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def pega_dados_animal(self):
        sg.ChangeLookAndFeel('BlueMono')

        entrada = [[[sg.Text('Inserir os dados do Animal abaixo: ', size=(30, 1),
                    justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
                    [sg.Text('Nome', size=(15, 1)), sg.InputText('nome', key='nome')],
                    [sg.Text('Chegada', size=(15, 1)), sg.InputText('chegada', key='chegada')],
                    [sg.Text('Ano Nascimento', size=(15, 1)), sg.InputText('ano_nascimento', key='ano_nascimento')],
                    [sg.Text("Qual o sexo do Animal:")],
                    [sg.InputText('sexo', key='sexo')],
                    [sg.Text("O Animal possui doenças?:")],
                    [sg.InputText('doenças', key='doenca')],
                    [sg.Text("O Animal está vacinado?:")],
                    [sg.InputText('vacinação', key='vacina')],
                    [sg.Text("O Animal está castrado?:")],
                    [sg.InputText('castração', key='castracao')],
                    [sg.Submit(tooltip='Clique para enviar os dados'), sg.Cancel()]]]

        layout = [[sg.Text('Cadastro Animal', size=(10, 1), font=("Helvetica", 25), justification='center')],
                  [sg.Column(entrada, vertical_alignment='center', justification='center', k='-C-')]]

        self.__window2 = sg.Window("Cadastro de Animal", default_element_size=(30, 1)).Layout(layout)

    def mostra_animal(self):
        self.pega_dados_animal()
        button, values = self.__window2.Read()
        return values

    def fechar_cadastro_animal(self):
        if self.__window2 != None:
            self.__window2.Close()
        self.__window2 = None

    def seleciona_animal(self):
        nome = input("Nome do animal que deseja selecionar: ")
        return nome

