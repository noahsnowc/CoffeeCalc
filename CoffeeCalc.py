import sys
import PySimpleGUI as pygui
import time

def ratioCalc(groundWeight, chosenRatio):
    if isinstance(groundWeight, int):
        if isinstance(chosenRatio, int):
            return groundWeight * chosenRatio


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

    while True:                                 # Event Loop
        event, values = window.read(timeout=10) # Please try and use as high of a timeout value as you can
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
    window.close()
main()
'''
    current_time = 0
    paused = True
    start_time = int(round(time.time() * 100))  
    pause_time = 0;  

##This is fucking wonky
    while True:
       
        
        if not paused:
            event, values = window.read(timeout=10)
            current_time = int(round(time.time()*100)) - start_time
        else:
            event, values = window.read()
        if event == 'button':
            event = window[event.GetText()]
    # --------- Do Button Operations --------
        if event == pygui.WIN_CLOSED:       # ALWAYS give a way out of program
            break
        if event == 'Reset':
            start_time = int(round(time.time() * 100))
            current_time = 0
            paused_time = start_time
        elif event == 'Pause':
            paused = True
            paused_time = int(round(time.time() * 100))
            element = window['PauseButton']
            element.update(text='Run')
        elif event == 'Start Timer':
            paused = False
            start_time = start_time + int(round(time.time() * 100)) - pause_time
            element = window['PauseButton']
            element.update(text='Pause')   
        window['timer'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,(current_time // 100) % 60, current_time % 100))
    
    
    window.close()

main()
'''
'''
 event, values = window.read()
        print(event, values)
        if event == pygui.WIN_CLOSED:
            break
        if event == 'Submit':
            try:
                window['BloomOutput'].update(str(ratioCalc(int(values['GramInput']),2))+'g')
                window['TotalOutput'].update(str(ratioCalc(int(values['GramInput']),int(values['ratioDropdown'])))+'g')
            except Exception:
                pygui.popup("Looks like you didn't input a valid number.")
'''