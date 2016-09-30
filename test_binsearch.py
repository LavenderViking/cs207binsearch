import unittest
import numpy as n
from pytest import raises
from binsearch import binary_search


class Test(unittest.TestCase):

	def foundElement(self):
		self.assertEqual(binary_search(list(range(5), 2), 2)



	#def notFoundElement(self):
	#	self.assertEqual(binary_search(list(range(5), 7), -1)


t = unittest.TestLoader().loadTestsFromModule(Test())
unittest.TextTestRunner().run(t)
