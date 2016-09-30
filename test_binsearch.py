import unittest
import numpy as np
from pytest import raises
from doctest import run_docstring_examples as dtest
from binsearch import binary_search


class MyTest(unittest.TestCase):

	def test_foundd(self):
		sorted_num_list = list(range(15))
		self.assertEqual(binary_search(sorted_num_list, 2), 2)
