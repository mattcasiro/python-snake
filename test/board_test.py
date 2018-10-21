import pytest
from src.board import Board

class TestBoard:
    def get_board(self):
        snakes = [
            {
                "coords": [{2, 2}, {2,3}, {3,3}],
                "health": 10,
                "id": "asdf1234"
            }
        ]
        foods = [
            {10, 5},
            {6, 12}
        ]
        return Board(
            {
                "snakes" : snakes,
                "food"  : foods
            })

    def test_create_board(self):
        assert type(Board({})).__name__ == "Board"

    def test_board_has_snakes(self):
        assert self.get_board().snakes == [{
            "coords": [{2, 2}, {2,3}, {3,3}],
            "health": 10,
            "id": "asdf1234"
        }]
    def test_board_has_foods(self):
        assert self.get_board().foods == [
            {10, 5},
            {6, 12}
        ]
