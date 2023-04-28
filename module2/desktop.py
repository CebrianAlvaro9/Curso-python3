import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
button_size = (7,3)
PLAYER_ONE = "X"
PLAYER_TWO ="O"


deck = [0,0,0,
        0,0,0,
        0,0,0]

current_player = PLAYER_ONE

layout = [  [sg.Button("",key="-1-" ,size = button_size),
             sg.Button("",key="-2-" , size = button_size),
             sg.Button("",key="-3-", size = button_size)],
            [sg.Button("",key="-4-", size = button_size),
             sg.Button("",key="-5-", size = button_size),
             sg.Button("",key="-6-", size = button_size)],
            [sg.Button("",key="-7-", size = button_size),
             sg.Button("",key="-8-", size = button_size),
             sg.Button("", key="-9-",size = button_size)],
            
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    if window.Element(event).ButtonText =="":
        window.Element(event).Update(text=current_player)
        
        if current_player == PLAYER_ONE:
            current_player =PLAYER_TWO
        else:
            current_player ==PLAYER_ONE

window.close()