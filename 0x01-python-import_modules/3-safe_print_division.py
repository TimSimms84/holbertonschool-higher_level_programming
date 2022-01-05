#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        prod = a / b
    except:
        prod = None
    finally:
        print("Inside result: {}".format(prod))
        return prod
