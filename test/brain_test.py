import pytest # type: ignore
from src.brain import Brain
from src.board import Board
from src.coordinate import Coordinate

class TestBrain:
    def get_brain(self):
        width: int = 15
        snakes = [{
            "coords": [(2, 2), (2,3), (3,3)],
            "health": 10,
            "id": "asdf1234"
        }]
        foods = [
            ((10, 5)),
            ((6, 12))
        ]
        board = Board({
            "snakes" : snakes,
            "food"  : foods,
            "width" : width,
            "height" : width,
        })
        return Brain("asdf1234", board)

    def test_brain_can_get_nearest_food(self):
        brain = self.get_brain()
        assert brain.get_nearest_food() == Coordinate((10,5))

    def test_brain_can_get_valid_moves(self):
        brain = self.get_brain()
        assert brain.get_valid_moves() == ["left", "right", "up"]
