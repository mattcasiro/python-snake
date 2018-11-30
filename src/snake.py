"""Snake Module"""
from src.coordinate import Coordinate
#from src.brain import Brain
from src.board import Board
from typing import List

class Snake:
    """Define properties and functionality of a Snake."""
    def __init__(self, data, board: Board):
        self._data = data
        other_snakes = board.get_other_snakes(self.id)
        #self.brain = Brain(self, other_snakes, board.foods, board)
        #TODO: implement get_move_decision using brain

    @property
    def id(self):
        """Get the id of the snake."""
        return self._data['id']

    @property
    def coordinates(self) -> List[Coordinate]:
        """Get the List of Coordinates which describes the location of this Snake."""
        if self.coordinates is not None:
            return self.coordinates

        coordinates = []
        for coordinate_tuple in self._data['coords']:
            coordinates.append(Coordinate(coordinate_tuple))

        return coordinates

    @property
    def head(self) -> Coordinate:
        """Get the coordinate which represents the location of this Snake's head."""
        return Coordinate(self.coordinates[0])

    @property
    def body(self) -> Coordinate:
        """Get the List of Coordinates which respresents this Snake's body (not head)."""
        return self.coordinates[1:]

    @property
    def health(self):
        """Get the number of health points this Snake currently has."""
        return self._data['health_points']

    def contains_coordinate(self, coordinate) -> bool:
        """Get whether or not the given Coordinate is within this Snake."""
        return coordinate in self.coordinates
