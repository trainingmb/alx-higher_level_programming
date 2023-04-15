#!/usr/bin/python3
"""
Append after function
"""


def append_after(filename="", search_string="", new_string=""):
    '''
    A function that
    inserts a line of text to a file,
    after each line containing a specific string
    '''
    with open(filename, 'r+') as file:
        lines = file.readlines()
        linecount = 0
        for line in lines:
            if line.find(search_string) is not -1:
                lines.insert(linecount + 1, new_string)
            linecount += 1
        file.seek(0)
        file.write("".join(lines))
