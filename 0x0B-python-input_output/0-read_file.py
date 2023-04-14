#!/usr/bin/python3
"""
Read file function
"""


def read_file(filename=""):
    """
    Read file function
    """
    if len(filename) < 1:
        with open(filename) as file:
            print(file.read(), end='')
