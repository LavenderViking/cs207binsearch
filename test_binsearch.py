from pytest import raises
from doctest import run_docstring_examples as dtest
from binsearch import binary_search



def test_binsearch():
    dtest(binary_search, globals(), verbose=True)
    #assert myaverage([9,3]) == 6

