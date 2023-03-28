#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    ret = []
    index = 0
    if list_length <= 0:
        print("out of range")
        return ret
    while index < list_length:
        try:
            ret.append(my_list_1[index] / my_list_2[index])
        except TypeError:
            print("wrong type")
            ret.append(0)
        except ZeroDivisionError:
            print("division by 0")
            ret.append(0)
        except IndexError:
            print("out of range")
            ret.append(0)
        finally:
            index += 1
    return ret   
