#!/usr/bin/python3


def no_c(my_string):
    no_c = "C,c"

    for character in no_c:
        my_string = my_string.replace(character, "")
        return my_string
    else:
        return my_string
