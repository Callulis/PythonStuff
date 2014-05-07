# Chris Allulis
# What does this progrma do?
# http://pastebin.com/nxr5HD5z
import random
from itertools import product
import time

def generatePassword(characters):
    password = []
    for x in range(characters):
        num = random.randrange(65,90)
        password.append(chr(num))
    passwordString = ""
    passwordString = "".join(password)
    return passwordString

def guessPassword(minChars,maxChars):
    characters = minChars
    list = [] * characters
    guessed = False
    if(guessed == False):
        list = [chr(65)] * characters
    guess = "".join(list)
    print guess

def guessPasswordRandom(minChars,maxChars,password):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # chars to look for

    for length in range(minChars, maxChars):
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
            if password == ''.join(attempt):
                print password
                return


def main():
    start = time.time()
    password =  generatePassword(7)
    guessPasswordRandom(3,8,password)
    end = time.time()
    print str(end - start + 1)[0:4] + " seconds"

if __name__ == "__main__":
    main()