#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        s = sum([x * y for x, y in my_list])
        res = s / sum([y for x, y in my_list])
        return res
    return 0
