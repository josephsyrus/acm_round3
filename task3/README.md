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


