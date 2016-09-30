import unittest
from pytest import raises
import numpy as np
from binsearch import binary_search


class MyTest(unittest.TestCase):

	def test_foundd(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 2), 2)


suite = unittest.TestLoader().loadTestsFromModule(MyTest())
unittest.TextTestRunner().run(suite)
