#!/usr/bin/python3

"""
this code will convert an object to
json and will save it to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj(list): the object that will be converted
        filename(txt): file that object will be saved
    """
    json_file = json.dumps(my_obj)
    with open(filename, mode="w+",  encoding="utf-8") as f:
        file_to_save = f.write(json_file)
