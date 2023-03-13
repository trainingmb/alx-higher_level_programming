#!/usr/bin/python3


def no_c(my_string):
    newstring = ""
    for i in my_string:
        i = str(i)
        if (i != 'c') and (i != 'C'):
            newstring += i
    return newstring
