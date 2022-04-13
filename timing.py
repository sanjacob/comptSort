#! /usr/env/python3

"""Sorting algorithms timing test."""

import timeit

setup = 'from comptSort import comptSort'
test_list = list(range(700, 1, -1))
algos = ['bubble', 'insertion', 'bin_insertion', 'merge', 'quick']
timings = []

for algo in algos:
    print(f'Sorting with {algo}')
    timings.append(timeit.timeit(f'comptSort({test_list}, "{algo}")', number=100, setup=setup))

print(f'Timings were {list(zip(algos, timings))}')
