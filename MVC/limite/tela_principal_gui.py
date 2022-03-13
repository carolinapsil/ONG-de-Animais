import PySimpleGUI as sg


class TelaPrincipal():
    def __init__(self):
        self.__window = None

    def init_components(self):
        sg.ChangeLookAndFeel('BlueMono')
        botoes = [[sg.Button('Doações', size=(20, 2), key=1, button_color='#7B68EE')],
                  [sg.Button('Animais', size=(20, 2), key=2, button_color='#7B68EE')],
                  [sg.Button('Adotante', size=(20, 2), key=3, button_color='#7B68EE')],
                  [sg.Button('Doador', size=(20, 2), key=4)],
                  [sg.Button('Voluntário', size=(20, 2), key=5)],
                  [sg.Button('Adoções', size=(20, 2), key=6)],
                  [sg.Button('Lar Temporário', size=(20, 2), key=7)],
                  [sg.Button('Pesquisar animais disponíveis para adoção', size=(20, 2), key=8)],
                  [sg.Button('Finalizar sistema', size=(20, 2), key=0)]]

        layout = [[sg.Text('ONG de Animais', size=(15, 2), font=('Montserrat', 20), justification=('center'))],
                  [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]]

        self.__window = sg.Window("oCurso", default_element_size=(40, 1)).Layout(layout)

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button

    def close(self):
        if self.__window != None:
            self.__window.Close()
            self.__window = None

    def mostra_mensagem(self, mensagem):
        sg.Popup(mensagem)
