#!/usr/bin/python3
"""
Rectangle class.
"""


class Rectangle:
    """
    Defines a class that defines a rectangle

    """

    def __init__(self, width=0, height=0):
        """
        Constructor

        Args:
            width  (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, nwidth):
        """
        Setter for the width

        Args:
            nwidth (int): The new width to set as width
        """
        if not isinstance(nwidth, int):
            raise TypeError("{} must be an integer".format("width"))
        if nwidth < 0:
            raise ValueError("{} must be >= 0".format("width"))
        self.__width = nwidth

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, nheight):
        """
        Setter for the height

        Args:
            height (int): The new height to set as height
        """
        if not isinstance(nheight, int):
            raise TypeError("{} must be an integer".format("height"))
        if nheight < 0:
            raise ValueError("{} must be >= 0".format("height"))
        self.__height = nheight

    def area(self):
        """
        Calculate and return the area of the rectangle
        """
        return (self.height*self.width)

    def perimeter(self):
        """
        Calculate and returns the perimeter of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return (0)
        return (self.height+self.width)
