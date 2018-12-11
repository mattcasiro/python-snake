"""Snake Module"""
from typing import List
from src.coordinate import Coordinate

class Snake:
    """Define properties and functionality of a Snake."""
    def __init__(self, data: dict):
        self._data = data
        self._coordinates: List[Coordinate] = []

    def __eq__(self, other: object) -> bool:
        """Return true if the snake id, health, and coordinates match."""
        if not isinstance(other, Snake):
            return NotImplemented
        return self.id == other.id

    def __str__(self) -> str:
        return str(self.id) + "; " + str(self.health)# + "; " + str(self.head.x) +","+ str(self.head.y)

    @property
    def id(self) -> str:
        """Get the id of the snake."""
        return self._data["id"]

    @property
    def coordinates(self) -> List[Coordinate]:
        """Get the List of Coordinates which describes the location of this Snake."""
        if self._coordinates is not None and len(self._coordinates) > 0:
            return self._coordinates

        self._coordinates = []
        for coordinate_tuple in self._data['coords']:
            self._coordinates.append(Coordinate(coordinate_tuple))

        return self._coordinates

    @property
    def head(self) -> Coordinate:
        """Get the coordinate which represents the location of this Snake's head."""
        return self.coordinates[0]

    @property
    def body(self) -> List[Coordinate]:
        """Get the List of Coordinates which respresents this Snake's body (not head)."""
        return self.coordinates[1:]

    @property
    def health(self):
        """Get the number of health points this Snake currently has."""
        return self._data['health']

    def contains_coordinate(self, coordinate) -> bool:
        """Get whether or not the given Coordinate is within this Snake."""
        return coordinate in self.coordinates
