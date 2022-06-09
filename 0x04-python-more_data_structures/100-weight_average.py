#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    h = sum(x[0] * x[1] for x in my_list)
    k = sum(z[1] for z in my_list)
    return (h / k)
