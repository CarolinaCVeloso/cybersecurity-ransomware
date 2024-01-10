import os
import pyaes
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def decrypt_file(file_path, key):
    # Reads the encrypted file
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Removes the encrypted file
    os.remove(file_path)

    # Initializes AES decryption
    aes = pyaes.AESModeOfOperationCTR(key)

    # Decrypt the file data
    decrypt_data = aes.decrypt(file_data)

    # Save the decrypted file
    new_file_path = file_path.replace('.ransomwaretroll', '')
    with open(new_file_path, 'wb') as new_file:
        new_file.write(decrypt_data)
    print(f'File "{file_path}" decrypted and saved as "{new_file_path}"')

if __name__ == "__main__":
    # Ask user to select an encrypted file
    Tk().withdraw()
    file_path = askopenfilename(title="Select an encrypted file to decrypt")

    if not file_path:
        print("No file selected. Exiting.")
    else:
        # Key for decryption
        key = b'testeransomwares'

        # Decrypt the selected file
        decrypt_file(file_path, key)
