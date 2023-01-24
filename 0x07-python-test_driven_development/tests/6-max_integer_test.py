#!/usr/bin/python3

""" using unittest to test my max_integer codes """


import unittest
max_integer = __import__('6-max_integer.py').max_integer

class TestMaxInteger(unittest.TestCase):
    """ define the unitest that will test max_integer[...]"""


    def test_ordered_list(self):
        """ test an ordered list """
        ordered = [1,2,3,4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """ test an unordered list """
        unordered = [2, 3, 4, 1]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_beginning(self):
        """ test a list that started from highest"""
        max_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_beginning), 4)

    def test_float(self):
        """ test a list with float """
        float_list = [34.5, 32.6, 12.0, 11]
        self.assertEqual(max_integer(float_list), 34.5)

    def test_string_list(self):
        """ test a list with strings"""
        string_list = ['a', 'b', 'c', 'd']
        self.assertEqual(max_integer(string_list), 'd')

    def test_string(self):
        """ test a string """
        string = "seyman"
        self.assertEqual(max_integer(string), 'r')

    def null_value(self):
        """ give a null value """
        no_value = []
        self.assertEqual(max_integer(no_value), None)

if __name__ ==  '__main__':
    unittest.main()
