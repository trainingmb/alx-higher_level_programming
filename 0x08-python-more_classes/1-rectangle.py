#!/usr/bin/python3

class Rectangle:
    """
    Defines a class that defines a rectangle

    """
    self.__width = 0
    self.__height = 0

    def __init__(self, width=0, height=0):
        """
        Constructor

        Args:
            width  (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width  = width
        self.height = height
    @classmethod
    def checkint(var, name):
        """
        Check if var is an integer and >= 0

        Args:
            var  (int): The integer to check
            name (str): Name to place in exception
        """
        if not isinstance(var, int):
            raise TypeError("{} must be an integer".format(name))
        if var < 0:
            raise ValueError("{} must be >= 0".format(name))
    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width
    @width.setter
    def width(nwidth):
        """
        Setter for the width

        Args:
            nwidth (int): The new width to set as width
        """
        Rectangle.checkint(nwidth, "width")
        self.__width = nwidth
    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height
    @height.setter
    def height(nheight):
        """
        Setter for the height

        Args:
            height (int): The new height to set as height
        """
        Rectangle.checkint(nheight, "height")
        self.__height = nheight