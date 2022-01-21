#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """
    class with a public area
    """
    def area(self):
        """
        Raises: Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Raises: TypeError if value is not int
                ValueError if value <=0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value < 1:
            raise ValueError("{:s} must be greater than 0".format(name))
