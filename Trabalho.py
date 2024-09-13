import PySimpleGUI as sg
def tela_2():


    # All the stuff inside your window.
    layout = [  [sg.Text("What's your name?")],
                [sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Hello Example', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        print('Hello', values[0], '!')

    window.close()


def tela_1():
    # All the stuff inside your window.
    layout = [  [sg.Text("Digite seu nome"),sg.InputText(key='campo_nome')],
                [sg.Text("Digite a primeira nota"),sg.InputText()],
                [sg.Text("Digite a segunda nota"),sg.InputText()],
                [sg.Button('enviar'),sg.Button('resultado'),sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Hello Example', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, valores = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'resultado':
            window.close()
            tela_2()
        if event == 'enviar':    
            nome = valores['campo_nome']
            if len(nome)<3:
                sg.popup("esta errado é para colocar mais do que três letras")        
    window.close()

tela_1()