#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
	argc = len(argv) - 1
	if argc == 0:
	    print("{:d} arguments.".format(argc))
	elif argc == 1:
	    print("{:d} arguments.".format(argc))
	else:
	    print("{:d} arguments:".format(argc))
	for g in range(0, len(argv)):
        if g > 0:
            print("{:d}: {:s}".format(g, argv[g]))