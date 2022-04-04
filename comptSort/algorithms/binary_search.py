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

import math
from collections.abc import Callable

from .sorter import in_order


def binary_search(a, x, lo: int = 0, hi: int = None, *, key: Callable = None, asc: bool = True) -> int:
  """For the most part acts like bisect, with the added feature of asc/desc ordering."""
  # By default, high limit is the length of the sequence
  if hi is None:
    hi = len(a)

  while lo < hi:
    # Calculate middle of list
    mid = (lo+hi) // 2
    if in_order(x, a[mid], asc):
      # Use lower half of list
      hi = mid
    else:
      # Use higher half of list
      lo = mid + 1
  return hi
