#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence == "":
        return 0, 'N'
    else:
        return len(sentence), sentence[0]
