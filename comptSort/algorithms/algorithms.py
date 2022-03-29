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

from enum import Enum

from .binary_insertion import BinaryInsertionSort
from .bubble import BubbleSort
from .insertion import InsertionSort
from .merge import MergeSort
from .quick import QuickSort


class SortingAlgorithm(str, Enum):
  """Types of sorting algorithms."""
  BUBBLE = 'bubble'
  INSERTION = 'insertion'
  BIN_INSERTION = 'bin_insertion'
  MERGE = 'merge'
  QUICK = 'quick'

  def get_sorter(self):
    sorters = {
      self.BUBBLE: BubbleSort,
      self.INSERTION: InsertionSort,
      self.BIN_INSERTION: BinaryInsertionSort,
      self.MERGE: MergeSort,
      self.QUICK: QuickSort
    }
    return sorters[self]
