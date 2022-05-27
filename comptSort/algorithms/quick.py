"""Contains implementation of quick sort."""

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
from random import randrange
from typing import Any

from .sorter import Sorter, in_order


class QuickSort(Sorter):
    """Swap elements on both sides of a pivot."""

    @staticmethod
    def sort(uData: Sequence[Any], asc: bool = True) -> None:
        """Sort a sequence using quicksort.

        This implementation uses recursion and thus may experience issues with large lists.
        """
        QuickSort._quicksort(uData, 0, len(uData) - 1, asc)

    @classmethod
    def _partition(cls, a, lo, hi, *, asc: bool = True, random_pivot: bool = True):
        # Random pivotting
        if random_pivot:
            pivot_i = randrange(lo, hi + 1)
            a[hi], a[pivot_i] = a[pivot_i], a[hi]

        pivot = a[hi]
        top = lo

        for i in range(lo, hi):
            if in_order(a[i], pivot, asc):
                a[i], a[top] = a[top], a[i]
                top += 1

        a[hi], a[top] = a[top], a[hi]
        return top

    @classmethod
    def _quicksort(cls, a, lo, hi, asc: bool = True):
        if hi > lo:
            pivot = cls._partition(a, lo, hi, asc=asc)
            cls._quicksort(a, lo, pivot - 1, asc=asc)
            cls._quicksort(a, pivot + 1, hi, asc=asc)
