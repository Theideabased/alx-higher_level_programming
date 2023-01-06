#!/usr/bin/python3
"""
this function will add all possible integer
"""
def add_integer(a,b=98):
    """ A is the first integer so if the value is a float
    it will convert it to an integer but if it is not a float
    or an integer it will raise a TypeError same as be however b has a 
    default value therefore without giving a value it will use 
    the default value
    """
    #defining a loop that will check the value of a 
    if ((not isinstance(a,int) and not isinstance(a,float))):
        raise TypeError('a must be an integer')

    #defining a loop that will check the value of b
    if ((not isinstance(b,int) and not isinstance(b, float))):
        raise TypeError('b must be an integer')

    #returning the perfect answer and converting any float to integer
    return (int(a)+int(b))
