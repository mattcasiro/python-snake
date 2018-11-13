from src.coordinate import Coordinate
from typing import List

class Snake:
    def __init__(self, data):
        self._data = data

    @property
    def id(self):
        return self._data['id']

    @property
    def coordinates(self):
        if self.coordinates is not None:
            return self.coordinates

        coordinates = []
        for coordinate_tuple in self._data['coords']:
            coordinates.append(Coordinate(coordinate_tuple))

        return coordinates

    @property
    def head(self):
        return Coordinate(self.coordinates[0])

    @property
    def body(self):
        return self.coordinates[1:]

    @property
    def health(self):
        return self._data['health_points']

    def contains_coordinate(self, coordinate):
        return coordinate in self.coordinates
