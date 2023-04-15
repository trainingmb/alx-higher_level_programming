#!/usr/bin/python3
"""
Test Base Class
"""
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
	"""
	Docstring for TestBaseClass
	"""
	def test_id(self):
		correctid = 43
		nb = Base(correctid)
		self.assertEqual(nb.id, correctid)

	def test_noid(self):
		otherbase = Base()
		self.assertEqual(otherbase.id, 1)

	def test_2noid(self):
		otherbase1 = Base()
		otherbase2 = Base()
		self.assertEqual(otherbase2.id, 2)

if __name__ == '__main__':
    unittest.main()