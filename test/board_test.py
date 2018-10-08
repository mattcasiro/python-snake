import pytest
from src.board import Board

class TestBoard:
    def get_board(self):
        snake_list = [
            {
                "coords": [{2, 2}, {2,3}, {3,3}],
                "health": 10,
                "id": "asdf1234"
            }
        ]
        food_list = [
            {10, 5},
            {6, 12}
        ]
        return Board(
            {
                "snakes" : snake_list,
                "food"  : food_list
            })

    def test_create_board(self):
        assert type(Board({})).__name__ == "Board"

    def test_board_has_snakes(self):
        assert self.get_board().snake_list == [{
            "coords": [{2, 2}, {2,3}, {3,3}],
            "health": 10,
            "id": "asdf1234"
        }]
    def test_board_has_food(self):
        assert self.get_board().food_list == [
            {10, 5},
            {6, 12}
        ]
