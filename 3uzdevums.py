import PySimpleGUI as sg


menu_def=[["Help",["About"]]]


dalas=[
    [sg.Menu(menu_def)],
    [sg.T("Izvētlies jaukāko gadalaiku")],
    [sg.Combo(["Pavasaris", "Vasara", "Rudens","Ziema"], key="COMBO", enable_events=True, size=(40,10))],
    [sg.Button("Tava izvēle ir:")],
    [sg.T("", key="vieta")]
]

logs = sg.Window("aaaaaaaa",dalas, size= (600,500))



while True:
    event, values= logs.read()


    if event== sg.WIN_CLOSED or event == "Iziet": 
        break


   
    elif event=="Tava izvēle ir:":
        mana_izvele=values["COMBO"]
        logs["vieta"].update(f"Tu izvēlējies:{mana_izvele}")
    
    elif event== "Parr..":
        sg.popup("wow ok")
logs.close()


