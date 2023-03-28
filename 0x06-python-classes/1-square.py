#!/usr/bin/python3

"""Define a class Square."""

class Square:
	"""Represent a square."""
	__size = None
	
	def __init__(self, size):
		"""
		Initialize a square instance

		Args:
			size (int): Size of the square
		"""
		self.__size = size
