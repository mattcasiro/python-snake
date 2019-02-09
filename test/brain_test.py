import pytest # type: ignore
from src.brain import Brain
from src.board import Board
from src.coordinate import Coordinate

class TestBrain:
    width: int = 15
    main_snake = [{
        "body": [(2, 2), (2,3), (3,3)],
        "health": 10,
        "id": "asdf1234"
    }]
    #don't try to use equal_snake and smol_snek in the same game (they're in the same spot)
    equal_snake = [{
        "body": [(3, 1), (4,1), (4,2)],
        "health": 10,
        "id": "fdfdssdsssdfd"
    }]
    smol_snek = [{
        "body": [(3, 1), (4,1)],
        "health": 10,
        "id": "fdfdssds"
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
        brain = self.get_brain(self.main_snake, self.foods, self.width)
        assert brain.get_nearest_food() == Coordinate(10,5)

        brain_no_food = self.get_brain(self.main_snake, [], self.width)
        assert brain_no_food.get_nearest_food() is None

    def test_brain_can_get_valid_moves(self):
        brain = self.get_brain(self.main_snake, self.foods, self.width)
        assert brain.get_valid_moves() == ["left", "right", "up"]

    def test_brain_can_avoid_headons(self):

        two_close_snakes = self.main_snake + self.equal_snake
        brain = self.get_brain(two_close_snakes, self.foods, self.width)

        assert brain.get_threatening_snakes_moves() == [
            Coordinate(2,1),
            Coordinate(4,1),
            Coordinate(3,0),
            Coordinate(3,2),
        ]
        assert brain.get_valid_moves() == ["left"]

        snake_and_smol_snek = self.main_snake + self.smol_snek
        unthreatened_brain = self.get_brain(snake_and_smol_snek , self.foods, self.width)
        assert unthreatened_brain.get_threatening_snakes_moves() == []
        assert unthreatened_brain.get_valid_moves() == ["left", "right", "up"]

    def test_brain_can_path_to_nearest_food(self):
        brain = self.get_brain(self.main_snake, self.foods, self.width)
        assert brain.get_moves_for_nearest_food() == ["right", "down"]

    def test_brain_can_make_decision(self):
        brain = self.get_brain(self.main_snake + self.equal_snake, self.foods, self.width)
        assert brain.get_decision() == "left"

        brain = self.get_brain(self.main_snake, self.foods, self.width)
        assert brain.get_decision() == "right"

    def test_brain_dies_when_stuck(self):
        stuck_snake = list(self.main_snake)
        stuck_snake[0]["body"] = [(1,0), (0,0), (0,1)]

        blocking_snake = list(self.equal_snake)
        blocking_snake[0]["body"] = [(0,2),(1,2),(1,1),(2,1),(2,0),(3,0)] 

        brain = self.get_brain(stuck_snake + blocking_snake, self.foods, self.width)
        assert brain.get_decision() == "left"
