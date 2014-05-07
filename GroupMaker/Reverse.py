dictionary = {}

for x in range(65,90):
    dictionary[chr(x)] = chr((x+5) % 25 + 65)

print dictionary

plaintext = "Hello World!" # Message to encrypt
cipher = ""                # The final encrypted message
key = 10                   # The key to add to each character

for character in plaintext:
    cipher += chr(ord(character) + key)

print cipher