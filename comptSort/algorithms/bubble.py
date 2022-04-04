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


class BubbleSort(Sorter):
  """Repeatedly swap adjacent elements if in wrong order."""

  @staticmethod
  def sort(uData: Sequence[Any], asc: bool = True) -> None:
    n = len(uData)

    while n > 0:
      last_swapped = 0

      # Iterate over list
      for i in range(n - 1):
        # Not in order
        if not in_order(uData[i], uData[i + 1], asc):
          # Swap
          uData[i], uData[i+1] = uData[i+1], uData[i]
          last_swapped = i + 1
      # Only iterate until last swapped element
      # for better efficiency
      n = last_swapped
