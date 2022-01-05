#!/usr/bin/python3

import sys

j = len(sys.argv)


if j == 1:
    print("0 arguments.")
elif j == 2:
    print("1 argument\n1: {}".format(str(sys.argv[1])))
else:
    print("{} arguments:".format(j - 1))
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        print("{}: {}".format(i, str(sys.argv[i])))
