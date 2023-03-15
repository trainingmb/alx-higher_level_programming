#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) != type("") or roman_string is None:
        return 0
    rms = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    value = 0
    values = list(map(lambda x: rms[x], roman_string))
    l = len(values)
    i = 0
    while i < l:
        if (i+1) < l and values[i] < values[i+1]:
            value = value - values[i] + values[i+1]
            i = i + 2
        else:
            value = value + values[i]
            i = i + 1
    return value
