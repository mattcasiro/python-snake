import pytest # type: ignore
from src.brain import Brain
from src.board import Board
from src.coordinate import Coordinate

class TestBrain:
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

    def get_brain(self, snakes, foods, width):
        board = Board({
            "snakes": snakes,
            "food": foods,
            "width": width,
            "height": width,
        })
        return Brain(board.snakes[0].id, board)

    def test_brain_can_get_nearest_food(self):
        brain = self.get_brain(self.snakes, self.foods, self.width)
        assert brain.get_nearest_food() == Coordinate((10,5))

        brain_no_food = self.get_brain(self.snakes, [], self.width)
        assert brain_no_food.get_nearest_food() is None

    def test_brain_can_get_valid_moves(self):
        brain = self.get_brain(self.snakes, self.foods, self.width)
        assert brain.get_valid_moves() == ["left", "right", "up"]
