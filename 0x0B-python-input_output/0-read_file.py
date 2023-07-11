#!/usr/bin/python3

"""
This will code will show how to
open an encoded file with the "with"
statement
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
