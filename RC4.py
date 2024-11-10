def KSA(key):
    # Key Scheduling Algorithm (KSA)
    key_length = len(key)
    S = list(range(256))  # Initialize state array with values from 0 to 255
    j = 0
    for i in range(256):
        # Mix the key into the state array
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values in the state array
    return S

def PRGA(S):
    # Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values in the state array
        # Generate a keystream byte
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key, text):
    # Convert key to list of integers (ASCII values)
    key = [ord(c) for c in key]
    S = KSA(key)  # Initialize the state array using the key
    keystream = PRGA(S)  # Generate the keystream
    
    # Encrypt or decrypt input text using XOR with the keystream
    result = []
    for char in text:
        # XOR each character with the next byte from the keystream
        val = ord(char) ^ next(keystream)
        result.append(val)
    
    # Convert result to hexadecimal format for output
    return ''.join(f'{byte:02x}' for byte in result)

def RC4_decrypt(key, ciphertext):
    # Convert ciphertext (hexadecimal) back to characters and decrypt
    ciphertext_bytes = bytes.fromhex(ciphertext)
    # Convert key to list of integers (ASCII values)
    key = [ord(c) for c in key]
    S = KSA(key)  # Initialize the state array using the key
    keystream = PRGA(S)  # Generate the keystream
    
    # Decrypt the ciphertext using XOR with the keystream
    decrypted_text = ''.join(chr(byte ^ next(keystream)) for byte in ciphertext_bytes)
    return decrypted_text

# Input from user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

# Encrypt the plaintext
ciphertext = RC4(key, plaintext)
print(f"Ciphertext (in hexadecimal): {ciphertext}")

# Decrypt the ciphertext
decrypted_text = RC4_decrypt(key, ciphertext)
print(f"Decrypted text: {decrypted_text}")