#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        a = sorted(a_dictionary.items(), key=lambda x: x[1])
        return a[-1]
    else:
        return None
