#!/usr/bin/python3
"""
Rectangle class.
"""


class Rectangle:
    """
    Defines a class that defines a rectangle

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor

        Args:
            width  (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        The string representation of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return ("")
        s = str(self.print_symbol) * self.width
        s += '\n'
        s *= self.height
        return (s[:-1])

    def __repr__(self):
        """
        Return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """
        Destructor of the rectangle class object
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
        return (self.height+self.width) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returs the biggest rectangle
        based on the area

        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return (rect_1)

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size
        """
        return (Rectangle(size, size))
