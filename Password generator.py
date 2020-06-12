import PySimpleGUI as sg  
import os
import sys
import time
import pyperclip
import random
from random import SystemRandom


pass_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Welcome','LoveIT']


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def generate_rand():
    srand = SystemRandom()
    n = len(pass_list)
    x = srand.choice(range(0,n))
    
    srand = SystemRandom()
    num = srand.choice(range(1000, 9999))

    rand_word = pass_list[x]+str(num)
    pyperclip.copy(rand_word)
    print(rand_word)
    win_main.Element('_BAR_').Update(rand_word)



layout_main = [
                 
            
            
            [sg.Text('Random Password is:')],
            [sg.Text('')],
            
            [sg.Button('Generate',key='_RANDOM_',pad=((39, 0), (2, 2)))],
            [sg.Text('')],
            
            [sg.StatusBar('Status bar ...',pad=((0, 0), (20, 0)),auto_size_text=False,size=(15, None),key='_BAR_')],
          ]  


win_main = sg.Window('Rename PC', layout_main, location=(880,50),icon=resource_path('window.ico'))



# main loop

while True:
    ev_main, values = win_main.read()
    
    if ev_main=='_RANDOM_':
        generate_rand()
        
    
    if ev_main is None: # if user closes window or clicks cancel
        win_main.Close()
        break
   
    