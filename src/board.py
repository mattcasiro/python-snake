"""Board Module"""
from typing import Tuple, List
from src.coordinate import Coordinate
from src.snake import Snake

class Board:
    """Track the cooardinates for all snakes and food in the game."""
    def __init__(self, data):
        self._data = data
        self._snakes = None
        self._foods = None

    @property
    def snakes(self) -> List[Snake]:
        """Retreive the list of snakes from the board data."""
        if self._snakes is None:
            snakes = []
            for snake_data in self._data['snakes']:
                snakes.append(Snake(snake_data))
            self._snakes = snakes
        return self._snakes

    @property
    def foods(self) -> List[Coordinate]:
        """Retreive the list of food from the board data."""
        if not self._foods or len(self.foods) <= 0:
            foods = []
            for food_data in self._data['food']:
                foods.append(Coordinate(food_data))

            self._foods = foods
        return self._foods
        #return self._data['food']

    @property
    def width(self):
        """Get width of the board -- note: it's a square."""
        return self._data['width']

    def is_coordinate_in_bounds(self, coordinate):
        """Check whether or not the Coordinate is within the bounds of the Board."""
        is_wall = (coordinate.x == -1 or coordinate.x == self.width
                   or coordinate.y == -1 or coordinate.y == self.width)
        is_in_bounds = not is_wall
        return is_in_bounds

    def get_other_snakes(self, exclude_id):
        """Get the List of Snakes whose IDs don't match the given ID."""
        return [snake for snake in self.snakes if snake.id != exclude_id]
