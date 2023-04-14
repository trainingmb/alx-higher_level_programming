#!/usr/bin/python3
"""
7. Load, add, save
"""
import json
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """
    Write a script that adds all arguments
    to a Python list, and then save them to a file
    """
    filename = "add_item.json"
    with open(filename, 'w') as file:
        pass
    my_obj = load_from_json_file(filename)
    arg_list = [sys.argv[i] for i in range(1, len(sys.argv))]
    if not isinstance(my_obj, list):
        save_to_json_file(arg_list)
    else:
        for i in arg_list:
            my_obj.append(i)
        save_to_json_file(my_obj, filename)


if __name__ == '__main__':
    main()
