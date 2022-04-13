"""Contains implementation of insertion sort."""

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


class InsertionSort(Sorter):
    """Sort elements one at a time."""

    @staticmethod
    def sort(uData: Sequence[Any], asc: bool = True) -> None:
        """Sort a sequence using insertion sort."""
        # Index and element in list
        for i, x in enumerate(uData):
            j = i - 1
            # Step backwards, swapping until right position found
            while j >= 0 and not in_order(uData[j], x, asc):
                uData[j+1] = uData[j]
                j -= 1
            # Move current element to right position
            uData[j+1] = x
