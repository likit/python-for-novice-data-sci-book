import PySimpleGUI as sg

# layout
layout = [
    [sg.Text('Enter your name:'), sg.Input(key='name', size=(20, 1))],
    [sg.Text('Enter your weight in kg:'), sg.Input(key='weight', size=(20, 1))],
    [sg.Text('Enter your height in cm:'), sg.Input(key='height', size=(20, 1))],
    [sg.Text('', key='bmi'), sg.Text('', key='interpret')],
    [sg.Text('', key='suggestion')],
    [sg.Button('Calculate'), sg.Button('Reset'), sg.Exit()]
]

# window creation
window = sg.Window('BMI Calculator', layout=layout)


def gain_normal_bmi(weight, height, bmi):
    if bmi < 18.5:
        desired_weight = 18.5 * ((height*.01)**2)
    elif bmi >= 25:
        desired_weight = 24 * ((height * .01) ** 2)
    return desired_weight - weight

# event loop
while True:
    event, values = window.Read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Calculate':
        weight = float(values['weight'])
        height = float(values['height'])
        bmi = weight/(height*.01)**2
        window['bmi'].Update(f'Your bmi is {bmi:.2f}.')
        if bmi < 18.5:
            window['interpret'].Update('You are underweight.')
        elif bmi < 25.0:
            window['interpret'].Update('You are in good shape.')
            window['suggestion'].Update('Keep up what you are doing.')
        elif bmi < 30.0:
            window['interpret'].Update('You are overweight.')
        elif bmi < 35.0:
            window['interpret'].Update('You are in class 1 of obesity.')
        elif bmi < 40.0:
            window['interpret'].Update('You are in class 2 of obesity')
        else:
            window['interpret'].Update('You are in class 3 of obesity.')
        if not (18.5 <= bmi < 25):
            desired_weight = gain_normal_bmi(weight, height, bmi)
            if desired_weight > 0:
                window['suggestion'].Update(f'You should gain at least {desired_weight:.1f} kg.')
            else:
                window['suggestion'].Update(f'You should lose at least {desired_weight:.1f} kg.')
    elif event == 'Reset':
        window['name'].Update('')
        window['weight'].Update('')
        window['height'].Update('')
        window['bmi'].Update('')
        window['interpret'].Update('')
        window['suggestion'].Update('')

window.close()
