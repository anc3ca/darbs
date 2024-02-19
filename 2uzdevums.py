import PySimpleGUI as sg


menu_def = [["File",["Iziet"]],["Edit"]] 
dalas = [
    [sg.Menu(menu_def)],
    [sg.T("")],
    [sg.T("   "), sg.Button("Sveiki!",size=(8,4)),sg.T("   "),sg.Button("Nekas", size=(8,4))],
    [sg.T("")],
    [sg.T("   "), sg.Checkbox("Drukāt", default=False, key="IN")],
    [sg.T("   "), sg.Radio("Ir atļauja", 'Radio1', default=False, key='IN2')], 
    [sg.T("   "), sg.Radio("Nav atļauja", 'Radio1', default=False, key='IN3')],
    [sg.T("")],
    {sg.Multiline(size=(40,10), key="Multiline", disabled=True)}, 
    [sg.Button("Print"),sg.Button("Iziet")]

]


logs = sg.Window("woooooo",dalas, size= (600,500))





while True:
    event, values= logs.read()


    if event == sg.WIN_CLOSED or event == "Iziet": 
        break



    elif event =="Sveiki!":

        if values["IN"]==True and values["IN2"]:
         logs["Multiline"].update("Labrīt")
    
