import sys
import PySimpleGUI as pygui
import time
import json

def ratioCalc(groundWeight, chosenRatio):
    if isinstance(groundWeight, int):
        if isinstance(chosenRatio, int):
            return groundWeight * chosenRatio


def saveCurrentSelections(weight, ratio):
    
    data = {"weight": weight, "ratio": ratio}
    with open('userSetting.json', 'w') as json_file:
        json.dump(data, json_file)

def eventLoop(window,timer_running, counter):
    while True:                             
        event, values = window.read(timeout=10)
        if event in (pygui.WIN_CLOSED, 'Quit'):             # if user closed the window using X or clicked Quit button

            break

        elif event == 'Start/Stop':
            timer_running = not timer_running
        elif event == 'Reset':
            counter = 0
            timer_running = False
            window['timer'].update('{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100))
        if timer_running:
            window['timer'].update('{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100))
            counter += 1

        if event == 'Submit':
            try:
                window['BloomOutput'].update(str(ratioCalc(int(values['GramInput']),2))+'g')
                window['TotalOutput'].update(str(ratioCalc(int(values['GramInput']),int(values['ratioDropdown'])))+'g')
            except Exception:
                pygui.popup("Looks like you didn't input a valid number.")
        saveCurrentSelections(values['GramInput'], values['ratioDropdown'])
    window.close()

def main():
    pygui.theme('DarkBlue1')
            #Ratio Calculator Section Gui
    layout=[[pygui.Text('Enter your coffee amount in grams:')],
            [pygui.Input(size=(15,1), key='GramInput'), pygui.Text('Water Ratio:'),pygui.Combo(['14','15','16'], default_value='15',key='ratioDropdown')],
            [pygui.Text('Bloom:'), pygui.Text('g',size=(8,1),key='BloomOutput')],
            [pygui.Text('Total Weight:'), pygui.Text('g',size=(8,1), key='TotalOutput')],
            [pygui.Button('Submit')],

            ##Timer Section Gui
            [pygui.Button('Start/Stop'), pygui.Button('Reset', button_color=('white', '#007339'), key='Reset')],
            [pygui.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='timer')]
            ]
    window = pygui.Window('CoffeeCalc', layout)

    timer_running, counter = False, 0

    eventLoop(window, timer_running, counter)
    
main()
