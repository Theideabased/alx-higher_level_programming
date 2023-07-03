#!/usr/bin/python3

"""
we want to print a square with the character #
using size where the size must be an integer
and must not be a negative number
"""


def print_square(size):
    """
    the size is the length of the square
    and it must not be integer
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    # checking that the size is not 0
    if size <= 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
