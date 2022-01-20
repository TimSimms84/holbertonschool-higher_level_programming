#!/usr/bin/python3
"""
checks if same class
"""


def is_same_class(obj, a_class):
    """
    Return: True if obj is the exact class a_class, else False
    """
    return(type(obj) == a_class)
