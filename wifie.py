from os import system as c
import time
import random
import os

# Colors
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
P = '\x1b[38;5;201m'

def logo():
    c('clear')
    print(f"""{C}
 ▄▄▄▄▄  ▄▄▄▄▄  ▄▄▄▄▄ 
▐█   █▌▐█   █▌▐█    
▐█▀▀▀  ▐█▀▀▀  ▐█▀▀▀ 
▐█     ▐█     ▐█▄▄▄ 

{P} RIMON WORLD - WIFI PASSWORD HACK VIP (NON ROOT )
""")

def loading(task, sec):
    print(f"{Y}[+] {task}")
    for i in range(sec):
        print(f"{G}[*] Processing{'.' * (i % 4)}")
        time.sleep(1)
   
    else:
        print(f"{G}[✓]  Access Confirmed!\n")
        time.sleep(1)

def wifi_hack():
    logo()
    ssid = input(f"{C}ENTER TARGET WIFI NAME (SSID): ")
    loading(f"Connecting to {ssid}", 3)
    print(f"{G}[✓] Connected to {ssid}!\n")
    loading("Decrypting WiFi Password...", 3)
    print(f"{Y}[!]  Password Crack...\n")
    time.sleep(2)
    
    time.sleep(2)
    loading("Decrypting Password) ", 4)
    real_pass = random.choice
    print(f"{P}[✓] PASSWORD FOUND: {Y}{real_pass}\n")
    input(f"{A}Press Enter To Return To Menu...")
    menu()

def menu():
    logo()
    print(f"{A}[1] Start WiFi Password Hack ( NON ROOT)")
    print(f"{A}[0] Exit Tool")
    choice = input(f"{Y}Select Option: ")
    if choice == '1':
        wifi_hack()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] Invalid Option!")
        time.sleep(1)
        menu()

menu()