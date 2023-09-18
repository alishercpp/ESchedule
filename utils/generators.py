from random import *
from uuid import uuid4
import string
from time import time

def gen_id():
    pid = ''
    for _ in range(6):
        r = choice(string.digits)
        if r == '0':
            pid += '3'
        else:
            pid += r
    return int(pid)

if __name__ == '__main__':
    print("Pupil ID: ", gen_id())