#!/usr/bin/python3
"""
My list class
"""


class MyList(list):
    """
    inheriting from list list
    """
    def __init__(self):
        """initializes the object using super()"""
        super().__init__()

    def print_sorted(self):
        """prints itself sorted"""
        print(sorted(self))
