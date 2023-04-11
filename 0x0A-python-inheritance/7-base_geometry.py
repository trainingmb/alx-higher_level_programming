#!/usr/bin/python3
"""
bASEgEOMETRY Module
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
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
