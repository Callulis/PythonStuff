# Chris Allulis
# Introduction to Cryptography

import scrapy
import requests
import sympy

def reverse_encrypt(plaintext):
    pointer = len(plaintext) - 1
    ciphertext = ""
    while pointer >= 0:
        ciphertext = ciphertext + plaintext[pointer]
        pointer = pointer - 1
    return ciphertext

def reverse_decrypt(ciphertext):
    pointer = len(ciphertext) - 1
    plaintext = ""
    while pointer >= 0:
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

"""
def mask_encrypt(plaintext, mask):
def mask_decrypt(ciphertext, mask):
"""

def print_ascii():
    for index in range(33,256):
        print chr(index)

def main():
    my_cipher = ""
    print


if __name__ == "__main__":
    main()