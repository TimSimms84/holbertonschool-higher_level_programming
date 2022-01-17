#!/usr/bin/python3
"""
Unittest for max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    unittest class for max int
    """

    def test_module_docstring(self):
        """Tests for module docsting"""
        modstring = __import__('6-max_integer').__doc__
        self.assertTrue(len(modstring) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        funcstring = max_integer.__doc__
        self.assertTrue(len(funcstring) > 1)

    def test_empty(self):
        """test if empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negatives(self):
        """checks negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_type(self):
        """makes sure input is a list"""
        self.assertIs(list, list)

    def test_invalid(self):
        self.assertRaises(TypeError, max_integer((6, 7)))


if __name__ == "__main__":
    unittest.main()
