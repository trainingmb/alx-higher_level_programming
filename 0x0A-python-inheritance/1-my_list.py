#!/usr/bin/python3
"""
Mylist Module
"""

class MyList(list):
    """
    Docstring for MyList
    Inherits from list
    """
    def __init__(self):
        """
        Initializer
        """
        pass
    def print_sorted(self):
        """
        Prints a sorted list of ascending order
        """
        print(sorted(self))
