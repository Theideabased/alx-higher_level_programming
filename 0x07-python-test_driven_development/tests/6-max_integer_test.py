#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_none(self):
        self.assertEqual(max_integer([]), None)
    def test_intorder(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_intunorder(self):
        self.assertEqual(max_integer([4, 5, 3, 2]), 5)
    def test_floatorder(self):
        self.assertEqual(max_integer([2.3, 5, 3.6, 5.4]), 5.4)
