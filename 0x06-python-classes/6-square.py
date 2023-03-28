#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represent a square."""
    __size = None
    __position = None
    
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square instance

        Args:
            size (int): Size of the square
        """
        self.size = size
        self.position = position

    def my_print(self):
        """
        Print the square
        """
        s = '#' * self.__size
        s = ' ' * self.position[0] + s
        s += '\n'
        s *= self.__size
        s = '\n'*self.position[1] + s
        print(s)

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Position getter
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Position setter
        """
        if ((isinstance(value, tuple)) and
                (len(value) == 2) and
                (value[0] >= 0 and isinstance(value[0], int)) and
                (value[1] >= 0 and isinstance(value[0], int))):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
