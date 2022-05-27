#! /usr/env/python3

"""Sorting algorithms timing test."""

import random
import timeit
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    """Use `timeit` to analyse the running times of the comptSort algorithms."""
    setup = 'from comptSort import comptSort'
    n = 700
    repetitions = 100

    print(f'Generate a range of 1-{n}')
    test_list = list(range(n))

    print('Shuffle it randomly')
    random.shuffle(test_list)

    algos = ['bubble', 'insertion', 'bin_insertion', 'merge', 'quick']
    timings = []

    print('Try sorting the resulting sequence with comptSort')
    for algo in algos:
        print(f'Sorting with {algo}')
        timings.append(timeit.timeit(f'comptSort({test_list}, "{algo}")',
                       number=repetitions, setup=setup))

    print(f'Timings were {list(zip(algos, timings))}')


if __name__ == '__main__':
    raise SystemExit(main())
