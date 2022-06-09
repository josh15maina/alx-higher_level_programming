#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for y in list(a_dictionary.keys()):
        if a_dictionary[y] is value:
            del a_dictionary[y]
    return a_dictionary
