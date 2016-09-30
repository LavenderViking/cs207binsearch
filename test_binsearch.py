import unittest
import numpy as np
from pytest import raises
from binsearch import binary_search


class Test(unittest.TestCase):

	def foundElement(self):
		self.assertEqual(binary_search(list(range(5), 2), 2)

	#def notFoundElement(self):
	#	self.assertEqual(binary_search(list(range(5), 7), -1)

	#def foundElementInRange(self):
	#	self.assertEqual(binary_search(list(range(10), 5,1,8), 6)

	#def notFoundElementInRange(self):
	#	self.assertEqual(binary_search(list(range(10), 2,5,8), -1)
	

t = unittest.TestLoader().loadTestsFromModule(Test())
unittest.TextTestRunner().run(t)
