#!/usr/bin/python3
def no_c(my_string):
    res_str = ""
    for x in my_string:
	if x != 'c' and x != 'C':
	    res_str += x
    return (res_str)
