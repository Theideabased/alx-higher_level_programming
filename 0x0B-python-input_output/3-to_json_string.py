#!/usr/bin/python3

"""
this code will turn my object into
json strings
"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj(json)
    """
    result = json.dumps(my_obj)
    return result
