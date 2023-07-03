#!/usr/bin/python3

"""
this code will print a first name and a last name
both must be a string else it will print a typeerror
"""


def say_my_name(first_name, last_name=""):
    """
    Here the first_name must be string and
    the last_name must also be string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    # last_name must be a string too
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    result = print(f'My name is {first_name} {last_name}')
    return result
