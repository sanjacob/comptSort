from bisect import bisect

from comptSort import binary_search
from hypothesis import given
from hypothesis.strategies import composite, integers, lists


@composite
def list_and_index(draw, elements=integers()):
    xs = draw(lists(elements, min_size=1))
    i = draw(integers(min_value=0, max_value=len(xs) - 1))
    return (xs, i)


@given(list_and_index())
def test_bisect(list_index):
    """Compare the results of custom binary search function against bisect"""
    assert binary_search(*list_index) == bisect(*list_index)
