#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {j: 2 * a_dictionary[j] for j in a_dictionary} 
    return (new_dict)
