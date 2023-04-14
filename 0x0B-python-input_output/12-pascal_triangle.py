#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    Pascal Triangle
    """
    list_list = [[1]]
    curr_list = []
    indx = 0
    if n <= 0:
        return (curr_list)
    elif n == 1:
        return (list_list)
    for _ in range(n - 1):
        for indx in range(1 + len(list_list[-1])):
            if indx == 0:
                curr_list.append(1)
            else:
                s = list_list[-1][indx] + list_list[-1][indx - 1]
                curr_list.append(s)
            if indx == (len(list_list[-1]) - 1):
                curr_list.append(1)
                break
        list_list.append(curr_list.copy())
        curr_list = []
    return (list_list)
