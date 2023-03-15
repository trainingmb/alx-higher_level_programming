#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    cpy = []
    for i in matrix:
        temp = []
        for j in i:
            temp.append(j*j)
        cpy.append(temp)
    return cpy
