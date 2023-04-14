#!/usr/bin/python3
"""
Append file function
"""


def append_write(filename="", text=""):
    """
    Append file function
    """
    if len(filename) > 0:
        with open(filename, 'a') as file:
            return (file.write(text))
