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

from collections.abc import Sequence
from typing import Any

from .binary_search import binary_search
from .sorter import Sorter, in_order


class BinaryInsertionSort(Sorter):
  """Insertion sort with a binary search optimisation."""

  @staticmethod
  def sort(uData: Sequence[Any], asc: bool = True) -> None:
    for i, x in enumerate(uData):
      if i:
        j = i - 1
        # Get insertion index using binary search
        insert_i = binary_search(uData, x, 0, i, asc=asc)
        # Swap until in right position
        while j >= insert_i:
          uData[j+1] = uData[j]
          j -= 1
        uData[j+1] = x
