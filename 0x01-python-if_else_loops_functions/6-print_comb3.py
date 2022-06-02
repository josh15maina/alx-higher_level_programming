#!/usr/bin/python3
for a in range(0, 9):
    for b in range(1, 10):
        if b > a:
            if i != 8:
                print("{}{}, ".format(a, b), end=",")
            else:
                print("{}{}".format(a, b))
