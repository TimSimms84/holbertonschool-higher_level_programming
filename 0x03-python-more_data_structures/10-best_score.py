#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = 0
        for key, value in a_dictionary.items():
            if value > best:
                best, newkey = value, key
        return newkey

