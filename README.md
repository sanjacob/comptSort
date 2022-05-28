# comptSort

A function designed to sort sequences of data with one of 5 different sorting algorithms: Bubble Sort, Insertion Sort, Binary Insertion Sort, Merge Sort and Quicksort.

```python
>>> from comptSort import comptSort
>>> from comptSort import SortingAlgorithm
>>> uData = [9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> sData = comptSort(uData, SortingAlgorithm.MERGE, asc=True)
>>> sData
[1, 2, 3, 4, 5, 6, 7, 8, 9]

```


## Installation

```bash
python3 -m pip install comptSort
```





## Usage

comptSort provides two functions, one that sorts a list in place, and one that returns a sorted copy of a list.

```python
from comptSort import compSort
from comptSort import compSortInPlace
```



comptSort offers 5 different sorting algorithms, all of which are comparison sorts.

```python
>>> from comptSort import SortingAlgorithm
>>> list(SortingAlgorithm)
[<SortingAlgorithm.BUBBLE: 'bubble'>, <SortingAlgorithm.INSERTION: 'insertion'>, <SortingAlgorithm.BIN_INSERTION: 'bin_insertion'>, <SortingAlgorithm.MERGE: 'merge'>, <SortingAlgorithm.QUICK: 'quick'>]
```



### Command Line Interface

It is also possible to sort a file with the CLI.

```bash
$ comptSort -h
usage: comptSort [-h] [-a {bubble,insertion,bin_insertion,merge,quick}] [-d] [-i] [-o OUTPUT] file

Test the comptSort library by sorting lines of files.

positional arguments:
  file                  file containing items to sort

options:
  -h, --help            show this help message and exit
  -a {bubble,insertion,bin_insertion,merge,quick}, --algorithm {bubble,insertion,bin_insertion,merge,quick}
                        algorithm to sort with
  -d, --descending, --reverse
                        order sequence in descending order
  -i, --force-integers  parse lines from files as integers (by default strings)
  -o OUTPUT, --output OUTPUT
                        write sorted lines to file
```



## Authorship

**Jacob Sanchez Perez \<jsanchez-perez@uclan.ac.uk>**



## License

![GPLv2][license-badge]

This software is distributed under the [General Public License v2.0][license], more information available at the [Free Software Foundation][gnu].








[uclan]: https://uclan.ac.uk

[license]: LICENSE "General Public License"
[gnu]: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html "Free Software Foundation"

[license-badge]: https://img.shields.io/github/license/jacobszpz/comptSort
