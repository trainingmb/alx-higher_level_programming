#!/usr/bin/python3
"""
write file function
"""


def write_file(filename="", text=""):
    """
    Write file function
    """
    if len(filename) > 0:
        with open(filename, 'w') as file:
            return (file.write(text))
