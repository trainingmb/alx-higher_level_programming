#!/usr/bin/python3
"""
Rectangle Module
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry



class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        Rectangle initializer
        Args:
            width (int): The width of the object
            height (int): The height of the object
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
