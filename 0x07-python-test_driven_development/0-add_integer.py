#!/usr/bin/python3

""" This code will add different integers
and it will convert when neccesary and raise
the alarm when neccesary
"""
def add_integer(a,b=98):
    """ this will add a and b together
    if b is not given it will use the default 
    b value but if a is not given it will 
    raise a typeerror also if wrong values 
    are given it will also raise a 
    typeerror
    """
    if (( not isinstance(a,int) and not isinstance(a, float))):
        raise TypeError ('a must be an integer')
    if (( not isinstance(b,int) and not isinstance(b, float))):
        raise TypeError('b must be an integer')
    return (int(a) +int(b))
