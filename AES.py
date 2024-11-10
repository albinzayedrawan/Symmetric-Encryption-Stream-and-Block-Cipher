from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def pad(text):
    # Simple padding function for AES (since AES requires input in blocks of 16 bytes)
    padding_length = 16 - (len(text) % 16)
    return text + chr(padding_length) * padding_length

def unpad(text):
    # Remove padding from the plaintext
    padding_length = ord(text[-1])
    return text[:-padding_length]

def aes_encrypt(plaintext, key, mode, iv=None):
    # Pad the plaintext to ensure it is a multiple of 16 bytes
    padded_text = pad(plaintext)

    if mode == 'ECB':
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    elif mode == 'CBC':
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    else:
        raise ValueError("Invalid mode selected.")

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_text.encode()) + encryptor.finalize()
    return ciphertext.hex()

def aes_decrypt(ciphertext, key, mode, iv=None):
    ciphertext_bytes = bytes.fromhex(ciphertext)
    if mode == 'ECB':
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    elif mode == 'CBC':
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    else:
        raise ValueError("Invalid mode selected.")
    
    decryptor = cipher.decryptor()
    decrypted_padded_text = decryptor.update(ciphertext_bytes) + decryptor.finalize()
    # Remove padding from decrypted text
    return unpad(decrypted_padded_text.decode())

# User input
mode = input("Select AES mode (ECB/CBC): ").strip().upper()
plaintext = input("Enter the plaintext: ")
key = input("Enter a 16-byte (128-bit) key: ").encode()

if len(key) != 16:
    print("Error: Key must be 16 bytes (128 bits).")
else:
    if mode == 'CBC':
        iv = input("Enter a 16-byte IV: ").encode()
        if len(iv) != 16:
            print("Error: IV must be 16 bytes.")
        else:
            ciphertext = aes_encrypt(plaintext, key, mode, iv)
            print(f"Ciphertext (in hexadecimal): {ciphertext}")
            decrypted_text = aes_decrypt(ciphertext, key, mode, iv)
            print(f"Decrypted text: {decrypted_text}")
    elif mode == 'ECB':
        ciphertext = aes_encrypt(plaintext, key, mode)
        print(f"Ciphertext (in hexadecimal): {ciphertext}")
        decrypted_text = aes_decrypt(ciphertext, key, mode)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid mode selected. Please choose either 'ECB' or 'CBC'.")
