import pytest # type: ignore
from src.snake import Snake
from src.coordinate import Coordinate

class TestSnake:
    def get_snake(self):
        return Snake({
            'body': [(10,15),(11,15),(11,16),(11,17)],
            'health': 100,
            'id': 'abcd1234',
        })

    def test_create_snake(self):
        assert type(Snake({})).__name__ == 'Snake'

    def test_snake_has_head(self):
        assert self.get_snake().head == Coordinate(10,15)

    def test_snake_has_body(self):
        assert self.get_snake().body == [
            Coordinate(11,15),
            Coordinate(11,16),
            Coordinate(11,17)
        ]

    def test_snake_has_health(self):
        assert self.get_snake().health == 100

    def test_snake_has_id(self):
        assert self.get_snake().id == 'abcd1234'

    def test_snake_has_coordinates(self):
        snake = self.get_snake()
        assert snake.coordinates == [
            Coordinate(10,15),
            Coordinate(11,15),
            Coordinate(11,16),
            Coordinate(11,17)
        ]

    def test_snake_can_tell_if_contains_coordinates(self):
        snake = self.get_snake()

        coordinate = Coordinate(9,15)
        assert snake.contains_coordinate(coordinate) == False

        coordinate = Coordinate(10,14)
        assert snake.contains_coordinate(coordinate) == False

        coordinate = Coordinate(10,15)
        assert snake.contains_coordinate(coordinate) == True

    def test_snake_can_get_all_moves(self):
        snake = self.get_snake()

        all_moves = [
            Coordinate(9,15),
            Coordinate(11,15),
            Coordinate(10,14),
            Coordinate(10,16)
        ]

        assert snake.get_all_moves() == all_moves


