"""Coordinate module"""
from __future__ import annotations
from typing import Tuple, Optional, Any


class Coordinate(object):
    """Abstract each board position."""

    def __init__(self, coordinate: Any, secondCoord: Optional[int]) -> None:
        """Instantiate Coordinate with x and y values."""
        #self._coordinate: Tuple[int, int] = coordinate
        if isinstance(coordinate, tuple): 
            self.fromTuple(coordinate)
        elif isinstance(coordinate, int) and secondCoord is not None:
            self.fromInts(coordinate, secondCoord)
        elif isinstance(coordinate, dict):
            self.fromDict(coordinate)
        else:
            raise Exception('cannot initialize coordinate from parameters: ' + coordinate + '; ' + secondCoord)



    def fromDict(self, coordinate: dict) -> None:
        """Instantiate Coordinate from object"""
        if coordinate["x"] is not None and coordinate["y"] is not None:
            self._coordinate: Tuple[int, int] = (coordinate["x"], coordinate["y"])
        else:
            raise ValueError('Coordinate constructor from object didn\'t have valid properties.')

    def fromInts(self, x: int, y: int)-> None:
        """Instantiate Coordinate from two ints"""
        self._coordinate: Tuple[int, int] = (x, y)

    def fromTuple(self, coordinate: Tuple[Any, ...]) -> None:
        """Instantiate Coordinate from Tuple"""
        if isinstance(coordinate[0], int) and isinstance(coordinate[1], int):
            self._coordinate: Tuple[int, int] = (coordinate[0], coordinate[1])
        else:
            raise ValueError('Coordinate tuple values weren\'t ints.')


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

    def __str__(self) -> str:
        return "(" + str(self.x) +","+ str(self.y) + ")"

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
        return Coordinate((self.x, self.y - 1), None)

    def get_down(self) -> Coordinate:
        """Return the Coordinate below this Coordinate."""
        return Coordinate((self.x, self.y + 1), None)

    def get_right(self) -> Coordinate:
        """Return the Coordinate to the right of this Coordinate."""
        return Coordinate((self.x + 1, self.y), None)

    def get_left(self) -> Coordinate:
        """Return the Coordinate to the left of this Coordinate."""
        return Coordinate((self.x - 1, self.y), None)
