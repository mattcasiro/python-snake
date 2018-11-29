"""Coordinate module"""
from __future__ import annotations
from typing import Tuple


class Coordinate(object):
    """Abstract each board position."""

    def __init__(self, coordinate: Tuple[int, int]) -> None:
        """Instantiate Coordinate with x and y values."""
        #TODO: add overload constructor which just takes two ints instead of a tuple?
        self._coordinate: Tuple[int, int] = coordinate

    def __eq__(self, other: object) -> bool:
        """Return true if the x and y coordinate match."""
        if not isinstance(other, Coordinate):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: object) -> bool:
        """Return true if the x or y coordinates don't match."""
        if not isinstance(other, Coordinate):
            return NotImplemented
        return self.x != other.x or self.y != other.y

    @property
    def x(self) -> int:
        """Return the x value of the coordinate."""
        return self._coordinate[0]

    @property
    def y(self) -> int:
        """Return the y value of the coordinate."""
        return self._coordinate[1]

    def get_up(self) -> Coordinate:
        """Return the Coordinate above this Coordinate."""
        return Coordinate((self.x, self.y - 1))

    def get_down(self) -> Coordinate:
        """Return the Coordinate below this Coordinate."""
        return Coordinate((self.x, self.y + 1))

    def get_right(self) -> Coordinate:
        """Return the Coordinate to the right of this Coordinate."""
        return Coordinate((self.x + 1, self.y))

    def get_left(self) -> Coordinate:
        """Return the Coordinate to the left of this Coordinate."""
        return Coordinate((self.x - 1, self.y))
