#!/usr/bin/python3
"""
Reads text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    reads file and prints it to STDOUT
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
