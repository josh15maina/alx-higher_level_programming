#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Tuple A
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    # Tuple B
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    res_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (res_tuple)