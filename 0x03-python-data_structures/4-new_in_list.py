#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    copy_list = None
    if my_list is not None:
        copy_list = my_list.copy()        
    if (my_list is not None) and (idx >= 0) and (idx < len(my_list)):
        copy_list[idx] = element
    return(copy_list)
