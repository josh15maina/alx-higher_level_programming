#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_1 = set(a)
    set_2 = set(b)

    if len(set_1.intersection(set_2)) > 0:
        return (set_1.intersection(set_2))
    else:
        return("No common elements")
