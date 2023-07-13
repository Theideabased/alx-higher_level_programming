#!/usr/bin/python3
""" A function that load a file from a json file """
import json


def load_from_json_file(filename):
    """
    Args:
        filename(json): the json file that the object will load
    """
    with open(filename, encoding="utf") as myfile:
        json.load(myfile)
        
