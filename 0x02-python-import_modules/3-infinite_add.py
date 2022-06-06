#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
	add = 0
	for a in range(0, len(argv)):
	    if a > 0:
		add += int(argv[a])
	print("{:d}".format(add))
