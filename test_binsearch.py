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

	def noElement(self):
		self.assertEqual(binary_search([], 1), -1)
	
	def singleElement(self):
		self.assertEqual(binary_search([1], 1), 0)

	def sameElements(self):
		self.assertEqual(binary_search([1,2,5,6,7,8,2,2], 2), 7)

	def needleTest1(self):
		self.assertEqual(binary_search([1,2,3,4,5], 3,1,2), -1)

	def needleTest2(self):
		self.assertEqual(binary_search([1,2,3,4,5], 3,1,4), 2)

	def needleTest3(self):
		self.assertEqual(binary_search([1,2,3,4,5], 3,3,4), -1)

	def inf(self):
		self.assertEqual(binary_search([1,2, np.inf, 3,4], 3), 3)

	def nan(self):
		self.assertEqual(binary_search([1,2, np.nan, 3,4], 3), 2)

	def listwithIntsAndStrings(self):
		self.assertEqual(binary_search([1,2, "dad", 3,4], 3), -1)

	def notArray(self):
		try:
			self.assertEqual(binary_search('1 2 3 4 dad 5 6 7 8',5), 5)
		except:
			print("Please input an array!")
			
	

t = unittest.TestLoader().loadTestsFromModule(Test())
unittest.TextTestRunner().run(t)
