#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        d = ord(str[c])
        if (d >= 65) and (d <= 90):
            print("{}".format(chr(d)), end = "")
        else:
            print()
