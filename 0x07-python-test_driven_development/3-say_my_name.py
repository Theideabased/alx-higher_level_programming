#!/usr/bin/python3
"""
this code will print out your name
"""


def say_my_name(first_name, last_name=""):
    """
    The first_name will print out the first input while the last_name
    will print out the last input
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    return (f'my name is {first_name} {last_name}')
