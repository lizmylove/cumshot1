import subprocess
import sys
import time
import os
import platform
import random

number = +79999999999

RESET = "\033[0m"
GREEN_TEXT = "\033[35m"
BLACK_BG = "\033[48;5;55m"

required_modules = [
"webbrowser",
"telethon",
"requests",
"pyfiglet",
"fake_useragent",
"logging",
"telegram",
"pystyle",
"string",
"termcolor",
"asyncio"
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Для переноса строки после завершения

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_modules():
    for module in required_modules:
        try:
            __import__(module)
            print(GREEN_TEXT + f"{module}")
        except ImportError:
            print(f" {module}...")
            install(module)
            print_with_delay(GREEN_TEXT + f" {module}" + RESET)

    print_with_delay(GREEN_TEXT + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" + RESET)

check_and_install_modules()
os.system('cls' if os.name == 'nt' else 'clear')



import random
import os
import subprocess
import requests
from telethon import TelegramClient
import string
from pystyle import Write, Colors, Center
from termcolor import colored
import logging
import platform
import webbrowser

# Очистка консоли
os.system('cls' if os.name == 'nt' else 'clear')


# Баннер проекта
banner = '''
                                                .x+=:.                                s    
                                               z`    ^%    .uef^"                    :8    
             x.    .        ..    .     :         .   <k :d88E              u.      .88    
      .    .@88k  z88u    .888: x888  x888.     .@8Ned8" `888E        ...ue888b    :888ooo 
 .udR88N  ~"8888 ^8888   ~`8888~'888X`?888f`  .@^%8888"   888E .z8k   888R Y888r -*8888888 
<888'888k   8888  888R     X888  888X '888>  x88:  `)8b.  888E~?888L  888R I888>   8888    
9888 'Y"    8888  888R     X888  888X '888>  8888N=*8888  888E  888E  888R I888>   8888    
9888        8888  888R     X888  888X '888>   %8"    R88  888E  888E  888R I888>   8888    
9888        8888 ,888B .   X888  888X '888>    @8Wou 9%   888E  888E u8888cJ888   .8888Lu= 
?8888u../  "8888Y 8888"   "*88%""*88" '888!` .888888P`    888E  888E  "*888*P"    ^%888*   
 "8888P'    `Y"   'YP       `~    "    `"`   `   ^"F     m888N= 888>    'Y"         'Y"    
   "P'                                                    `Y"   888                        
                                                               J88"                        
                                                               @%                          
                                                             :"                            


'''

Write.Print(Center.XCenter(banner), Colors.blue_to_cyan, interval=0.001)


def propen():
    url = "https://github.com/lizmylove/CumShot"
    system = platform.system()

    if system == "Linux":
        if os.path.exists("/data/data/com.termux/files/usr/bin"):
            os.system(f"am start -a android.intent.action.VIEW -d {url}")
        else:
            webbrowser.open(url)
    elif system == "Windows":
        webbrowser.open(url)
    else:
        print("Unsupported system")


def urrl():
    url = "https://t.me/fanat_bosina"
    system = platform.system()

    if system == "Linux":
        if os.path.exists("/data/data/com.termux/files/usr/bin"):
            os.system(f"am start -a android.intent.action.VIEW -d {url}")
        else:
            webbrowser.open(url)
    elif system == "Windows":
        webbrowser.open(url)
    else:
        print("Unsupported system")

banner = '''
[1] своя жалоба  [2] использовать заготовки
[3] спам кодами  [4] проект на github
          [5] об авторе
'''
Write.Print(Center.XCenter(banner), Colors.blue_to_cyan, interval=0.001)

choice = Write.Input("\n\n[?] выбирай:", Colors.blue_to_cyan, interval=0.001)

if choice == "1":
  subprocess.run(['python', 'elizium.py'])

elif choice == "2":
  bannner = '''
скоро..
'''
  Write.Print(Center.XCenter(bannner), Colors.red_to_black, interval=0.001)


elif choice == "3":
  subprocess.run(['python', 'spamr.py'])

elif choice == "4":
    propen()
  
elif choice == "5":
    urrl()
  
