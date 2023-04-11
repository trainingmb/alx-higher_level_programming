#!/usr/bin/python3
"""
BaseGeometry Module
"""


class BaseGeometry():
    """
    Base Geometry class
    """
    def area(self):
        """
        Raises an area exception
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Integer validator
        Args:
            name (str): The name of the parameter to test
            value (int): The parameter to validate
        Raises:
            TypeError: Raised if value is not of type int
            ValueError: Raised if value is less than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
