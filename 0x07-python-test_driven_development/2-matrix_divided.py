#!/usr/bin/python3
"""
Matrix divided
"""

def matrix_divided(matrix, div):
    """
    Divides all values of a matrix [matrix] by the value [div]
    to 2 decimal places
    Args:
        matrix (list of lists): A matrix expresed as a list of
        lists of integers or floats
        div (int, float): The divisor
    Return:
    A matrix holding the result of the division
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"
    if not (isinstance(matrix, list)):
        raise TypeError(err1)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError(err3)
    if len(matrix) == 0:
        return ([])
    if div == 0:
        raise ZeroDivisionError(err4)
    rowlen = len(matrix[0])
    divmat = []
    for i in matrix:
        divmatrow = []
        rlc = 0
        for j in i:
            if not (isinstance(j, int) or isinstance(j, float)):
                raise TypeError(err1)
            divmatrow.append(round(j/float(div), 2))
            rlc += 1
        if rlc != rowlen:
            raise TypeError(err2)
        divmat.append(divmatrow)
    return (divmat)
