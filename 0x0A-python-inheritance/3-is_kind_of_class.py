#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """
    Return: True if obj is object is an instance of or inherithed from a_class
    else False
    """
    return(isinstance(obj) == a_class)
