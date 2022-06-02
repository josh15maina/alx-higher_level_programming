#!/usr/bin/python3
for c in range(0, 99):
    print("{:02d}".format(c), end=', ')
else:
    print("{:02d}".format(c + 1))
