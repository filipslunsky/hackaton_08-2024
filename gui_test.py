import PySimpleGUI as sg

layout = [
    [sg.Text('Health Tracker', size=(30, 1), justification='center', font=("Helvetica", 25))],
    [sg.Text('Metric', size=(15, 1)), sg.InputText(key='metric')],
    [sg.Text('Value', size=(15, 1)), sg.InputText(key='value')],
    [sg.Button('Add'), sg.Button('Update'), sg.Button('Delete')],
    [sg.Table(values=[], headings=['Metric', 'Value'], key='table', auto_size_columns=True, display_row_numbers=True)]
]

window = sg.Window('Health Tracker', layout)

data = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Add':
        metric = values['metric']
        value = values['value']
        data.append([metric, value])
        window['table'].update(values=data)
    elif event == 'Update':
        selected_row = values['table'][0]
        data[selected_row] = [values['metric'], values['value']]
        window['table'].update(values=data)
    elif event == 'Delete':
        selected_row = values['table'][0]
        data.pop(selected_row)
        window['table'].update(values=data)

window.close()
