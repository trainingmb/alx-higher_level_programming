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
        if type(size) != type(0):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
