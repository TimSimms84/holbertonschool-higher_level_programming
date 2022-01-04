#!/usr/bin/python3


def uppercase(str):
    upper_case = ""
    for i in str:
        char = ord(i)
        if ord('a') <= char <= ord('z'):
            char -= 32
        upper_case += chr(char)
    print('{:s}'.format(upper_case))
