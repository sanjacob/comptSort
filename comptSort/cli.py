#!/usr/bin/env python3

"""comptSort CLI module."""


import argparse
from typing import Sequence

from . import comptSort

algorithms = ['bubble', 'insertion', 'bin_insertion', 'merge', 'quick']


def _from_file(filename: str, as_ints: bool = False):
    """Read items from file, each per line."""
    items = []

    with open(filename) as f:
        for line in f:
            item = line.strip()
            if as_ints:
                item = int(item)
            items.append(item)

    return items


def main(argv: Sequence[str] | None = None) -> int:
    """Sorting Function comptSort Command Line Interface."""
    parser = argparse.ArgumentParser(
        'comptSort', description='Test the comptSort library by sorting lines of files.')

    parser.add_argument('file', help='file containing items to sort')
    parser.add_argument('-a', '--algorithm', help='algorithm to sort with',
                        choices=algorithms, default='merge')
    parser.add_argument('-d', '--descending', '--reverse',
                        help='order sequence in descending order', action='store_true')
    parser.add_argument('-i', '--force-integers',
                        help='parse lines from files as integers (by default strings)',
                        action='store_true')

    args = parser.parse_args()

    if args.file is not None:
        try:
            uData = _from_file(args.file, args.force_integers)
        except ValueError as e:
            print('Error while parsing file: File must contain only integers')
            print(e)
        except OSError as e:
            print(e)
        else:
            c = comptSort(uData, sort=args.algorithm, asc=not args.descending)
            print(c)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
