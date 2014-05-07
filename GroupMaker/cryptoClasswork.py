plaintext = raw_input("Enter a message!")
cipher = ""
pointer = len(plaintext)-1

#We iterate through ever character
#Of "plaintext" backwards and append
#Those characters to "cipher"
while(pointer >= 0):
    cipher = cipher + plaintext[pointer]
    pointer = pointer - 1

print cipher

