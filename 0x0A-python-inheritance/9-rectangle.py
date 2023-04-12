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

    def area(self):
        """
        Calculate area
        """
        return self.__width * self.__height

    def __str__(self):
        """ String rep  """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
