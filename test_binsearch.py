import unittest
from pytest import raises
import numpy as np
from binsearch import binary_search


class Test(unittest.TestCase):

	def foundElement(self):
		self.assertEqual(binary_search(list(range(5), 2), 2)

ttest = unittest.TestLoader().loadTestsFromModule(MyTest())
unittest.TextTestRunner().run(ttest)
