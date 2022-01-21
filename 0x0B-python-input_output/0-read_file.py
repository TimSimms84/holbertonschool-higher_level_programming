#!/usr/bin/python3
"""
Reads text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    with open(filename) as my_file:
        print(my_file.read())
