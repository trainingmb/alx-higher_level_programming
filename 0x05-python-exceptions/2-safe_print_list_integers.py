#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
	i = 0
	c = 0
	while True:
		try:
			if i < x:
				print("{:d}".format(my_list[i]), end='')
				i += 1
				c += 1
			else:
				print("", end='\n')
				return c
		except (ValueError, TypeError):
			i += 1
