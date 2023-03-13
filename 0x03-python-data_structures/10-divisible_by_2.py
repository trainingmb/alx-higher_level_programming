#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    cpy = None
    if (my_list is None):
        cpy = None
    elif (my_list < 1):
        cpy = []
    elif:
        for i in range(len(my_list)):
            cpy[i] = ((my_list[i]%2) == 0)
    return cpy
