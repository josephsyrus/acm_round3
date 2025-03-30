# Task 3:

Design a malware (decent and working) and submit a writeup explaining the process of making , its working and POC. It should include videos and screenshots.

## Disclaimer: 
Keylogger & Encryption Script (For Educational Purposes Only).

This script demonstrates keylogging and AES encryption techniques for **ethical security research and educational purposes**. It is **not intended for malicious use**.

Only run this code in a safe and secure environment such as an air gapped Virtual Machine

## Process of Making & Working:
This malware uses concepts of both keylogging and ransomware (partially implemented)

On the main thread, we run a keyboard listener imported from pynput. This calls a unique function onpress or onrelease based on the event it is listening to

Implemented a set 'pressed' to check if keys are being registered twice (faced this issue on windows 10 VM)

Defined a list 'doNotEncrypt' which contains directories essential to the smooth operation of the OS. Encrypting files in these directories could lead to the system crashing. Also define a path to the log file where keystrokes are begin logged.

Next, we run a daeamon process on another thread which calls the encrypt function. From the USER directory, we explore other paths in the system, while ensuring it is not a part of the 'doNotEncrypt' list. If the conditions are satisfied, we use AES encryption on these files

Advanced Encryption Standard (AES) is a symmetric encryption, wherein we can use the same key to encrypt and decrypt information. 

In this code we can implement AES using the python library pycryptodome. First we create a random key of 16bytes. Read the data from the file in the form of binary, split the bits into blocks (Cipher Block Chaining) and then run the encryption. Incase a block does not have enough bits, we can pad it with bits. Finally write the encrypted data back to the files along with an initialization vector, which is required for decrypting the data later on.

The code can be converted to an executable by intalling pyinstaller and running the following command: pyinstaller --onefile --noconsole --hidden-import=pynput --hidden-import=Crypto --name=task3  main.py

## Screenshots:

![Screenshot 2025-03-30 215243](https://github.com/user-attachments/assets/4d51f1bb-6605-47ef-8fe2-57d598bd0aca)
![Screenshot 2025-03-30 215317](https://github.com/user-attachments/assets/840daff7-9fe0-4efd-a05f-8038e88c8e78)
![Screenshot 2025-03-30 215338](https://github.com/user-attachments/assets/0aabff90-7e5a-42ac-9e48-cabac9639564)
![Screenshot 2025-03-30 215406](https://github.com/user-attachments/assets/b43d6298-d7f9-4f66-b4d4-0e56c959498e)
![Screenshot 2025-03-30 215438](https://github.com/user-attachments/assets/891e91ae-494d-427b-b739-f1bacb7cb75a)
![Screenshot 2025-03-30 215533](https://github.com/user-attachments/assets/fff95f3b-0747-4d30-bc9e-e0bb0369f8e6)


## Screen Recording:

https://drive.google.com/file/d/1pJOzjdOlkWfJ-6DAqCibDMSeiHyywy3j/view?usp=drive_link


## Shortcomings:

Since some files required for enhanced user experience such as the file explorer get encrypted, the system loses a lot of functionality.

Encryption uses a different key each time, making decryption difficult.

Easily gets flagged and deleted by Windows Defender, due to lack of certification and a common footprint to other malware.



