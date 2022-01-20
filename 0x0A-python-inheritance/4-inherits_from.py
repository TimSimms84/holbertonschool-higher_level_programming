#!/usr/bin/python3
"""
check if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Return: True if obj is instance of a class...
    else False
    """
    if type(obj) == a_class:
        return False
    return(issubclass(type(obj), a_class))
