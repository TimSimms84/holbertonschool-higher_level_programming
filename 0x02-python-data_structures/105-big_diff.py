#!/usr/bin/python3
def big_diff(my_list=[]):
    if len(my_list) < 2:
        return 0
    else:
        max, min = my_list[0], my_list[0]
        for i in my_list:
            if i > max:
                max = i
            if i < min:
                min = i
        return max - min
