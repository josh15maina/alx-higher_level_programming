#!/usr/bin/python3
import hidden_4
import sys
if __name__ == "__main__":
    names = dir(hidden_4)
    for y in names:
	if y[:2] != "__":
	    print("{:s}".format(y))
