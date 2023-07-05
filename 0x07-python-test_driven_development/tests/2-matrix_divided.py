#!/usr/bin/python3

"""
Here i want to divided a matrix by a number using a
simple python code.
"""


def matrix_divided(matrix, div):
    """ the matrix must be a list of lists, the row
    must be equal and all the element must be either integer
    or float. the div must be an integer or float, and it must
    not be zero
    """
    if not all(isinstance(row, list) and all(isinstance(ele, (int, float)) for ele in row) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    # making sure all the size of the matrix is equal
    row_length = set(len(row) for row in matrix)
    if len(row_length) > 1:
        raise TypeError('Each row of the matrix must have the same size')
    # div must be a number
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    # div must not be zero
    if div == 0:
        raise ZeroDivisionError('division by zero')
    result = [[round(ele / div,2) for ele in row] for row in matrix]
    return result
