#!/usr/bin/python3

"""
This code will append the last line of a
document and it will print the len of the
appended line
"""


def append_write(filename="", text=""):
    with open(filename, mode="a+", encoding="utf-8") as myfile:
        myfile.write(text)
    with open(filename, encoding="utf-8") as myfile:
        myfile.read()
        return len(text)
