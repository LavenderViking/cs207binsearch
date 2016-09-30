import unittest
import numpy as np
from pytest import raises
from doctest import run_docstring_examples as dtest
from binsearch import binary_search


class MyTest(unittest.TestCase):

	def test_found(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 2), 2)


	def test_binsearch():
   		dtest(binary_search, globals(), verbose=True)
    		#assert myaverage([9,3]) == 6

