#!/usr/bin/python3
"""
Read file function
"""


def read_file(filename=""):
    """
    Read file function
    """
    if filename != "":
        with open(filename) as file:
            print(file.read())
