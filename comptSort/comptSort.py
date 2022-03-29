#!/usr/bin/env python3

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.
# Also available at https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

from typing import Any, Union

from .algorithms import SortingAlgorithm


def comptSort(uData: list[Any], sort: SortingAlgorithm, asc: bool = True) -> list[Any]:
  """
  Return a sorted copy of a list.
  :param list[Any] uData: The original, unsorted data.
  :param str sort: A string specifying the sorting algorithm to be used.
  :param bool asc: If true, sort will be performed in ascending order.
  """
  dataCopy = uData.copy()
  sort.get_sorter().sort(dataCopy, asc)
  return dataCopy

def comptSortInPlace(uData: list[Any], sort: SortingAlgorithm, asc: bool = True) -> None:
  """
  Sort a list in place.
  :param list[Any] uData: The original, unsorted data.
  :param str sort: A string specifying the sorting algorithm to be used.
  :param bool asc: If true, sort will be performed in ascending order.
  """
  sort.get_sorter().sort(dataCopy, asc)


def from_file(filename: str):
  with open(filename) as f:
    print(f.read().splitlines())
