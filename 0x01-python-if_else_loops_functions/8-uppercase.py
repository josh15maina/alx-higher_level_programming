#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        d = ord(str[c])
        if (d >= 97) and (d <= 122):
            j -= 32
            print("{}".format(chr(d)), end="")
        else:
            print()
