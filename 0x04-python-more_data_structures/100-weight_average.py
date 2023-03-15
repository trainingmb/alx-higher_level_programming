#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == None or len(my_list) < 1:
        return 0
    ws = 0.0
    s = 0.0
    for (i,j) in my_list:
        ws = ws+(i*j)
        s = s+j
    return ws/s
