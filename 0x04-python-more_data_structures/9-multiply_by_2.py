#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.update({n: 2 * a_dictionary[n] for n in a_dictionary.items()})
    return (new_dict)
