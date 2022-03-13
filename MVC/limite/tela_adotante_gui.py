import PySimpleGUI as sg
from PySimpleGUI import Button


class TelaAdotanteGUI():

    def __init__(self, controlador_adotante):
        self.__controlador_adotante = controlador_adotante
        self.__window = None
        self.init_components()

    @property
    def window(self):
        return self.__window

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
        return button, values

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)