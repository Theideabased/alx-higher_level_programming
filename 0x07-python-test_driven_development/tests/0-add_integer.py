#!/usr/bin/python3

# We want to write a function that can add only two
# two integers together


def add_integer(a, b=98):
    """ this function will add two inetgers together,
    firstly will turn amy float tp integer before adding
    amd raise and error if integer i not providfed or either
    a or b
    """
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError('a must be an integer')
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError('b must be an integer')
    return a + b
