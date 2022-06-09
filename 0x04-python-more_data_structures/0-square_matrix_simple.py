#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[y ** 2 for y in z] for z in matrix]
    return (new_matrix)
