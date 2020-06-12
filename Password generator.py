import PySimpleGUIQt as sg
import pyperclip
import random
import os
import sys
from random import SystemRandom

menu_def = ['BLANK',['&Complex','&Standard', 'E&xit']]


pass_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Welcome','Saturday','Sunday']

complex_char = ['$', '&', '*', "(", ')', '@', '!', '%']

def random_numer(a,b):
    x = SystemRandom().choice(range(a,b))
    return x

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def generate_rand():
    
    n = len(pass_list)
    x = random_numer(0,n)
    
    
    num = random_numer(1000,9999)

    rand_word = pass_list[x]+str(num)
    pyperclip.copy(rand_word)
    print(rand_word)
    
# Generates complex random password with one of the special characters in random part of the one of the words.
def generate_rand_complex():
    n = len(pass_list)
    x = random_numer(0,n)

    rand_word = pass_list[x]
    len_of_word = len(rand_word)
    len_of_word += 1

    y = random_numer(1,len_of_word)

    list_of_char = list(rand_word)
    random_complex_char = SystemRandom().choice(complex_char)
    list_of_char.insert(y-1,random_complex_char)
    new_word = ''.join(list_of_char)
    num = random_numer(1000,9999)
    rand_word = new_word+str(num)
    pyperclip.copy(rand_word)

    print(rand_word)

tray = sg.SystemTray(menu=menu_def, filename=resource_path('Icon.ico'))

while True:  # The event loop
    menu_item = tray.Read()
    if menu_item == 'Exit':
        break
    elif menu_item == 'Standard':
        generate_rand()
    elif menu_item == 'Complex':
        generate_rand_complex()
