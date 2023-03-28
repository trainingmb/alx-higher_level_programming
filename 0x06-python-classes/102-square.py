#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represent a square."""
    __size = None
    
    def __init__(self, size=0):
        """
        Initialize a square instance

        Args:
            size (int): Size of the square
        """
        self.size = size

    def area(self):
        """
        Returns the area of the current
        square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Size getter
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Size getter

        Args:
            value (int): New size of square
        """
        if type(value) != type(0):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """=="""
        return self.area() == other.area()

    def __ne__(self, other):
        """!="""
        return self.area() != other.area()

    def __lt__(self, other):
        """<"""
        return self.area() < other.area()

    def __le__(self, other):
        """<="""
        return self.area() <= other.area()

    def __gt__(self, other):
        """>"""
        return self.area() > other.area()

    def __ge__(self, other):
        """>="""
        return self.area() >= other.area()
