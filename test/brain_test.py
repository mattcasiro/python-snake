import pytest
from src.brain import Brain
from src.snake import Snake
from src.board import Board
from src.coordinate import Coordinate

class TestBrain:
    def get_brain(self):
        board = Board(
            #TODO: import sample board init data from separate file.
        )
        brain = Brain({
            board.snakes[0],
            board.get_other_snakes(board.snakes[0].id),
            board.foods,
            board
         })

    def test_brain_can_get_nearest_food(self):
        brain = self.get_brain()
        assert brain.get_nearest_food() == Coordinate((0,1))

    def test_brain_can_get_valid_moves(self):
        brain = self.get_brain()
        assert brain.get_valid_moves() == ["left", "right", "up"]
        #TODO: replace expected valid moves with something legit.
