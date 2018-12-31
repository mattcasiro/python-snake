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

    def test_brain_can_avoid_headons(self):
        equal_snake = [{
            "coords": [(3, 1), (4,1), (4,2)],
            "health": 10,
            "id": "fdfdssdsssdfd"
        }]

        two_close_snakes = self.snakes + equal_snake
        brain = self.get_brain(two_close_snakes, self.foods, self.width)

        assert brain.get_threatening_snakes_moves() == [
            Coordinate((2,1)),
            Coordinate((4,1)),
            Coordinate((3,0)),
            Coordinate((3,2)),
        ]
        assert brain.get_valid_moves() == ["left"]

        smol_snek = [{
            "coords": [(3, 1), (4,1)],
            "health": 10,
            "id": "fdfdssdsssdfd"
        }]
        snake_and_smol_snek = self.snakes + smol_snek
        unthreatened_brain = self.get_brain(snake_and_smol_snek , self.foods, self.width)
        assert unthreatened_brain.get_threatening_snakes_moves() == []
        assert unthreatened_brain.get_valid_moves() == ["left", "right", "up"]

