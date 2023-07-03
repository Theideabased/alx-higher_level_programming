#!/usr/bin/python3
"""
Here I want to print two line after '.', '?' or ':'
is in the file
"""


def text_indentation(text):
    """
    text must be a string else it will
    raise an error
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    punctuation_mark = ['.', '?', ':']
    for char in text:
        if char in punctuation_mark:
            print("\n" * 2, end="")
