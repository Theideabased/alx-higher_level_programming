#!/usr/bin/python3
""" instance of a class to json """
import json


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name(str)
            last_name(str)
            age(int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        with open(self, encoding = 'utf-8') as f:
            json.dump(self, f)
            return f
