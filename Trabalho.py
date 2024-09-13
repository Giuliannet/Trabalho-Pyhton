import PySimpleGUI as sg
def tela_2():


    # All the stuff inside your window.
    layout = [  [sg.Text("Nota do aluno")]
               
                ]

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
    lista = []

    # All the stuff inside your window.
    layout = [  [sg.Text("Digite seu nome"),sg.InputText(key='campo_nome')],
                [sg.Text("Digite a primeira nota"),sg.InputText(key='nota_aluno')],
                [sg.Text("Digite a segunda nota"),sg.InputText(key='nota_aluno2')],
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
            nota1 = valores['nota_aluno']
            nota2 = valores['nota_aluno2']

            if nota1 == '' or nota2 == '' or nome == '':
                sg.popup ("erro porque esta vazio")


            elif nome.isdigit() == True:
                sg.popup("Está errado porque é necessário inserir um texto")  

            elif nome.isdigit() == False and len(nome)<3:
                sg.popup("Esta errado é para colocar mais do que três letras")        

            elif valores['nota_aluno'].isdigit() == True or valores['nota_aluno2'].isdigit() == True: 
                nota1 = float(valores['nota_aluno'])
                nota2 = float(valores['nota_aluno2'])

                if nota1 > 10 and nota2 > 10:
                    sg.popup("erro porque é para colocar um numero menor do que dez")    
                else:
                    lista.append({
                        'nome': nome,
                        'nota1': nota1,
                        'nota2' : nota2
                    })

                    return lista 
            else:
                sg.popup("erro porque é para colocar numero no lugar de texto")

             


    window.close()

Tema tela_1()