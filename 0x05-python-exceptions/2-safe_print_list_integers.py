#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
	index = 0
	while True:
		try:
			if index < x:
				print(my_list[index], end='')
				index += 1
			else:
				print("", end='\n')
				return index
		except IndexError as err:
			raise err
			return
		except (ValueError, TypeError):
			index += 1
