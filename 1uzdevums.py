import PySimpleGUI as sg



dalas = [
    [sg.Text("ievadiet vārdu"), sg.InputText(key="vards")],
    [sg.Text("ievadiet uzvārdu"), sg.InputText(key="uzvards")],
    {sg.Multiline(size=(50,10), key="Multiline", disabled=True)}, 
    [sg.Button("Print"),sg.Button("Iziet")]

]

logs = sg.Window("okokokokok",dalas)

while True:
    event, values = logs.read()

    if event == sg.WIN_CLOSED or event == "Iziet": 
        break
    if event == "Print":

        vards=values["vards"]
        uzvards=values["uzvards"]

    logs["Multiline"].update(f"Labdien, tevi sauc {vards},{uzvards}!")
logs.close()

