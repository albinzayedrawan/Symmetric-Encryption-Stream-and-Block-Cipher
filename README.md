# Symmetric Encryption (Stream and Block Cipher)

## Stream Cipher (RC4):
- The Python program will implement the RC4 algorithm using a given key.
- The program should accept plaintext and a key as input, and output the corresponding ciphertext in hexadecimal format.
- It should also decrypt the ciphertext back to plaintext using the same key.

## Block Cipher (AES):
- Use Python’s cryptography library to implement AES encryption.
```bash
pip install cryptography
```
- The program should prompt the user to select either ECB or CBC mode.
- It should take plaintext, a 16-byte (128-bit) key for simplicity, and IV (for CBC mode) as input, and output the ciphertext in hexadecimal format.
- The program should also be able to decrypt the ciphertext back to plaintext.
