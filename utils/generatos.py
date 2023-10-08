from random import choice
from string import ascii_lowercase

DIGITS = '0123456789'

def generate():
    uid = ''
    for i in range(3):
        uid += choice(ascii_lowercase)
        uid += choice(DIGITS)
    return uid

if __name__ == "__main__":
    uid = generate()
    print(uid)