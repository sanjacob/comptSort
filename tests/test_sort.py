from hypothesis import given
from hypothesis import strategies as st

from comptSort import SortingAlgorithm as Sorting
from comptSort import comptSort

# Test with lists of integers and characters
unsorted_lists = st.one_of(st.lists(st.integers()), st.lists(st.characters()))


@given(unsorted_lists, st.booleans())
def test_bubble(uData, asc):
    expect = sorted(uData, reverse=not asc)
    result = comptSort(uData, Sorting.BUBBLE, asc=asc)
    assert result == expect


@given(unsorted_lists, st.booleans())
def test_insertion(uData, asc):
    expect = sorted(uData, reverse=not asc)
    result = comptSort(uData, Sorting.INSERTION, asc=asc)
    assert result == expect


@given(unsorted_lists, st.booleans())
def test_binary_insertion(uData, asc):
    expect = sorted(uData, reverse=not asc)
    result = comptSort(uData, Sorting.BIN_INSERTION, asc=asc)
    assert result == expect


@given(unsorted_lists, st.booleans())
def test_merge(uData, asc):
    expect = sorted(uData, reverse=not asc)
    result = comptSort(uData, Sorting.MERGE, asc=asc)
    assert result == expect


@given(unsorted_lists, st.booleans())
def test_quick(uData, asc):
    expect = sorted(uData, reverse=not asc)
    result = comptSort(uData, Sorting.QUICK, asc=asc)
    assert result == expect
