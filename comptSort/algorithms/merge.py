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

from .sorter import Sorter, in_order


class MergeSort(Sorter):
  """Recursively split array, sort each half, then merge"""

  @staticmethod
  def sort(uData: Sequence[Any], asc: bool = True) -> None:
    # Two arrays are required, one to sort elements into
    # and the other one to merge elements to
    MergeSort._split(uData.copy(), 0, len(uData), uData, asc)

  @classmethod
  def _split(cls, b, lo, hi, a, asc: bool = True):
    """Recursive method that splits the sequence in two,
    sorts both parts and then merges them."""
    n = hi - lo
    if n <= 1:
      return
    # Find middle point
    m = n // 2
    # Split first half
    cls._split(a, lo, lo+m, b, asc)
    # Split second half
    cls._split(a, lo+m, hi, b, asc)
    # Merge both halfs
    cls._merge(b, lo, m, hi, a, asc)

  @staticmethod
  def _merge(a, lo, m, hi, b, asc: bool = True):
    """Merge two sorted sequences into a single one."""
    head_x, head_y = lo, (lo + m)

    for i in range(hi-lo):
      # If second half empty or next element is in first half
      if (head_x < lo+m and (head_y >= hi or in_order(a[head_x], a[head_y], asc))):
        # Use first half
        b[lo+i] = a[head_x]
        head_x += 1
      else:
        # Use second half
        b[lo+i] = a[head_y]
        head_y += 1
