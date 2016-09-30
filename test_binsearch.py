import unittest
import numpy as np
from pytest import raises
from binsearch import binary_search


class Test(unittest.TestCase):

	def foundElement(self):
		self.assertEqual(binary_search(list(range(5)), 2), 2)

	def notFoundElement(self):
		self.assertEqual(binary_search(list(range(5)), 7), -1)

	def foundElementInRange(self):
		self.assertEqual(binary_search(list(range(10)),5,1,8), 6)

	def notFoundElementInRange(self):
		self.assertEqual(binary_search(list(range(10)), 2,5,8), -1)

	def unsortedList(self):
		self.assertEqual(binary_search([1,6,2,9,8], 9), 3)

	def noElement(self:
		self.assertEqual(binary_search([], 1), -1)
	
	def singleElement(self:
		self.assertEqual(binary_search([1], 1), 0)

	def sameElements(self:
		self.assertEqual(binary_search([1,2,5,6,7,8,2,2], 2), 7)
	
	

	

t = unittest.TestLoader().loadTestsFromModule(Test())
unittest.TextTestRunner().run(t)
