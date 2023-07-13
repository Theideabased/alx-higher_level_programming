#!/usr/bin/python3

"""
this will open a file, create one if it
doesn't exist and will overwrite the on that
exist with the one the text given
"""


def write_file(filename="", text=""):
    """
    Args:
        filename(str): this is the name of the create file
        text(str): this is the word that will be in the file
    """
    with open(filename, mode="w+", encoding="utf-8") as myfile:
        myfile.write(text)
    with open(filename, encoding="utf-8") as myfile:
        read_file = myfile.read()
        return len(read_file)
