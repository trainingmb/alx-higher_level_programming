#!/usr/bin/python3


def weight_average(my_list=[]):
    ws = 0.0
    s = 0.0
    for (i,j) in my_list:
        print(str(i), "     " + str(j))
        ws = ws + i*j
        s = s + j
    print(ws)
    print(s)
    return ws/s
