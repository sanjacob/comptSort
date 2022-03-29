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

from abc import ABC, abstractmethod
from typing import Any


class Sorter(ABC):
  """Interface that describes a sorting algorithm."""

  @classmethod
  @abstractmethod
  def sort(cls, uData: list[Any], asc: bool = True) -> None:
    """Sorts a list in place"""
    ...


def in_order(a: Any, b: Any, asc: bool = True) -> bool:
  """Compares two items"""
  return ((b < a) and not asc) or ((a < b) and asc)
