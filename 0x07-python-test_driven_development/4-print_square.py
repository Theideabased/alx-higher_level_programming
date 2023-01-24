#!/usr/bin/python3
"""
we want to print a square with any given instance
size will be the variable where size is the lenght of the square
and this code will raise error if the variable is not an 
integer. 
also if the variable is 0 the python will raise a ValueError
lastly if the value is less than 0 it will raise a ValueError
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for n in range(0, size):
        for m in range (size):
            print('#', end = "")
        print("")
