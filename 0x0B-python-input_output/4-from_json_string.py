#!/usr/bin/python3

"""
this code will load a file to
the object required
"""
import json


def from_json_string(my_str):
    result = json.loads(my_str)
    return result
