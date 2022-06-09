#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(1, 4):
        new_matrix = []
        for j in matrix:
            new_matrix.append(j[i])
            new_matrix.append(j ** 2)
        return (new_matrix)
