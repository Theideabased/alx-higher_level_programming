#!/usr/bin/python3
""" 
This code will print two lines after 
every ":", "." , "?"
and will raise an error if the input given is not 
a text
"""


def text_indentation(text):
    """
    The 'text' here is the words that the code will read through 
    and will but space whenever he sees the given marks
    if the text is not a string it will raise 
    a TypeError: text must be string
    """

    # show error if text is not a string
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    count = 0
    while count < len(text) and text[count] == " ":
        count += 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".:?":
            if text[count]in ".:?":
                print("\n")
            count += 1 
            if count < len(text) and text[count] == " ":
                continue
        count += 1 
