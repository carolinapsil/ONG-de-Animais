import PySimpleGUI as sg
from PySimpleGUI import Button


class TelaAdotante():

    def __init__(self, controlador_adotante):
        self.__controlador_adotante = controlador_adotante
        self.__window = None
        self.__window2 = None
        self.init_components()

    @property
    def window(self):
        return self.__window

    @property
    def window2(self):
        return self.__window2

    @window.setter
    def window(self, window):
        self.__window = window

    @window2.setter
    def window2(self, window2):
        self.__window2 = window2

    def init_components(self):
        sg.ChangeLookAndFeel('BlueMono')

        botoes = [
                    [sg.Button('Cadastrar', size=(20, 2), key=1, button_color='#7B68EE')],
                    [sg.Button('Alterar', size=(20, 2), key=2, button_color='#7B68EE')],
                    [sg.Button('Listar', size=(20, 2), key=3, button_color='#7B68EE')],
                    [sg.Button('Retornar', size=(20, 2), key=0, button_color='#7B68EE')]
        ]

        layout = [
                    [sg.Text("ADOTANTE", justification='center', size=(20, 1), font=("Montserrat", 25))],
                    [sg.Text("O que deseja fazer?", justification='center', size=(15, 1), font=("Montserrat", 25))],
                    [sg.Column(botoes, vertical_alignment='center', justification='center')]
        ]

        self.__window = sg.Window('Tela Adotante', default_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def pega_dados_adotante(self):
        sg.ChangeLookAndFeel('BlueMono')

        entrada = [
                    [sg.Text("Nome")],
                    [sg.InputText(size=(20,2), key="nome")],
                    [sg.Text("Data de nascimento")],
                    [sg.InputText(size=(20,2), key="data_nascimento")],
                    [sg.Text('Telefone')],
                    [sg.InputText(size=(20, 2), key="telefone")],
                    [sg.InputCombo(('Feminino', 'Masculino'), size=(20, 3), key='genero')],
                    [sg.Text('Email')],
                    [sg.InputText(size=(20, 2), key="email")],
                    [sg.Text('Endereço')],
                    [sg.InputText(size=(20, 2), key="endereco")],
                    [sg.Text('Idade')],
                    [sg.Slider(range=(21, 100), orientation='h', size=(34, 20), default_value=21, key="idade")],
                    [sg.Button("Cadastrar")]
                ]

        layout = [
          [sg.Text('Cadastro de Adotante', size=(10,1), font=("Helvetica", 25), justification='center')],
          [sg.Column(entrada, vertical_alignment='center', justification='center', k='-C-')]
        ]

        self.__window2 = sg.Window("Cadastro de Adotante", default_element_size=(30, 1)).Layout(layout)

    def abrir_cadastro_adotante(self):
        self.pega_dados_adotante()
        button, values = self.__window2.Read()
        return values

    def fechar_cadastro_adotante(self):
        if self.__window2 != None:
            self.__window2.Close()
        self.__window2 = None
