# Chris Allulis
# Introduction to Cryptography

def reverse_encrypt(plaintext):
    pointer = len(plaintext) - 1
    cipher = ''
    while (pointer >= 0):
        cipher = cipher + plaintext[pointer]
        pointer = pointer - 1
    return cipher

def reverse_decrypt(ciphertext):
    pointer = len(ciphertext) - 1
    plaintext = ''
    while (pointer >= 0):
        plaintext = plaintext + ciphertext[pointer]
        pointer = pointer - 1
    return plaintext

def caesar_encrypt(plaintext, key):
    cipher = ''
    for index in range(len(plaintext)):
        cipher = cipher + chr(ord(plaintext[index]) + key % 256)
    return cipher

def caesar_decrypt(ciphertext, key):
    plaintext = ''
    for index in range(len(ciphertext)):
        plaintext = plaintext + chr(ord(ciphertext[index]) - key % 256)
    return plaintext

def mask_encrypt(plaintext, mask):
    cipher = ''
    for index in range(len(plaintext)):
        cipher = cipher + chr(ord(plaintext[index]) + ord(mask[index%len(mask)]) % 256)
    return cipher

def mask_decrypt(ciphertext, mask):
    plaintext = ''
    for index in range(len(ciphertext)):
        plaintext = plaintext + chr(ord(ciphertext[index]) - ord(mask[index%len(mask)]) % 256)
    return plaintext

def print_ascii():
    for index in range(33,256):
        print chr(index)

def main():
    print_ascii()

if __name__ == "__main__":
    main()