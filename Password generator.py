import PySimpleGUIQt as sg
import pyperclip
import random
import os
import sys
from random import SystemRandom

menu_def = ['BLANK',['&Generate', 'E&xit']]


pass_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Welcome','Saturday','Sunday']


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


tray = sg.SystemTray(menu=menu_def, filename=resource_path('Icon.ico'))

while True:  # The event loop
    menu_item = tray.Read()
    if menu_item == 'Exit':
        break
    elif menu_item == 'Generate':
        generate_rand()
        
