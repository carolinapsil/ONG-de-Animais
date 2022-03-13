import PySimpleGUI as sg


class AnimalView:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel("Reddit")

    column1 = [[sg.Text('Column 1', background_color='#F7F3EC',
                justification='center', size=(10, 1))],
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box1')],
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box2')],
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box3')]]

    layout = [[sg.Text('Inserir os dados do Animal abaixo: ', size=(30, 1),
                        justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
                [sg.Text('Nome', size=(15, 1)), sg.InputText('nome', key='nome')],
                [sg.Text('Chegada', size=(15, 1)), sg.InputText('chegada', key='chegada')],
                [sg.Text('Ano Nascimento', size=(15, 1)), sg.InputText('ano_nascimento', key='ano_nascimento')],
                [sg.Text("Qual o sexo do Animal:")],
                [sg.Radio('Fêmea', "RADIO1", default=True, size=(10, 1)), sg.Radio('Macho', "RADIO1")],
                [sg.Text("O Animal possui doenças?:")],
                [sg.Radio('Sim', "RADIO1", default=True, size=(10, 1)), sg.Radio('Não', "RADIO1")],
                [sg.Text("O Animal está vacinado?:")],
                [sg.Radio('Sim', "RADIO1", default=True, size=(10, 1)), sg.Radio('Não', "RADIO1")],
                [sg.Text("O Animal está castrado?:")],
                [sg.Radio('Sim', "RADIO1", default=True, size=(10, 1)), sg.Radio('Não', "RADIO1")],
                [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]]

    window = sg.Window('Everything bagel', default_element_size=(40, 1), grab_anywhere = False).Layout(layout)
    button, values = window.Read()
    sg.Popup('Title',
             'The results of the window.',
             'The button clicked was "{}"'.format(button),
             'The values are', values)


