import PySimpleGUI as sg


class TelaPrincipal():
    def __init__(self):
        self.__window = None

    def init_components(self):
        sg.ChangeLookAndFeel('BlueMono')
        botoes = [[sg.Button('Doações', size=(30, 2), key=1, button_color='#7B68EE')],
                  [sg.Button('Animais', size=(30, 2), key=2, button_color='#7B68EE')],
                  [sg.Button('Adotante', size=(30, 2), key=3, button_color='#7B68EE')],
                  [sg.Button('Doador', size=(30, 2), key=4, button_color='#7B68EE')],
                  [sg.Button('Voluntário', size=(30, 2), key=5, button_color='#7B68EE')],
                  [sg.Button('Adoções', size=(30, 2), key=6, button_color='#7B68EE')],
                  [sg.Button('Lar Temporário', size=(30, 2), key=7, button_color='#7B68EE')],
                  [sg.Button('Pesquisar animais disponíveis para adoção', size=(30, 2), key=8, button_color='#7B68EE')],
                  [sg.Button('Finalizar sistema', size=(30, 2), key=0, button_color='#7B68EE')]]

        layout = [[sg.Text('ONG de Animais', size=(50, 2), font=('Helvetica', 20), justification=('center'))],
                  [sg.Text('Aviso: Antes de cadastrar uma adoção, doação ou um lar temporário, certifique-se de '
                           'cadastrar o animal, adotante, doador ou voluntário!',
                           font=('Helvetica', 10), justification=('center'))],
                  [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]]

        self.__window = sg.Window("ONG de Animais", default_element_size=(40, 1)).Layout(layout)

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
