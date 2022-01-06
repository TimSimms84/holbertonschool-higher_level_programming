#!/usr/bin/python3


def no_c(my_list):
    no_c = "C,c"
    new_string = my_list[:]

    for character in no_c:
        new_string = new_string.replace(character, "")
        return new_string
    else:
        return new_string
