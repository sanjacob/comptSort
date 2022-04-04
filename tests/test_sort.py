from typing import Any

import pytest
from comptSort import SortingAlgorithm as Sorting
from comptSort import comptSort
from hypothesis import assume, example, given
from hypothesis import strategies as st

unsorted_lists = st.lists(st.integers())

@given(unsorted_lists, st.booleans())
def test_bubble(uData: list[Any], asc: bool):
  expect = sorted(uData, reverse=not asc)
  result = comptSort(uData, Sorting.BUBBLE, asc=asc)
  assert result == expect

@given(unsorted_lists, st.booleans())
def test_insertion(uData: list[Any], asc: bool):
  expect = sorted(uData, reverse=not asc)
  result = comptSort(uData, Sorting.INSERTION, asc=asc)
  assert result == expect

@given(unsorted_lists, st.booleans())
def test_binary_insertion(uData: list[Any], asc: bool):
  expect = sorted(uData, reverse=not asc)
  result = comptSort(uData, Sorting.BIN_INSERTION, asc=asc)
  assert result == expect
