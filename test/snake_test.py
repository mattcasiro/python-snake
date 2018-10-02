import pytest
from src.snake import Snake

class TestSnake:
    def get_snake(self):
        return Snake({
            'coords': [(10,15),(11,15),(11,16),(11,17)],
            'health_points': 100,
            'id': 'abcd1234',
        })

    def test_create_snake(self):
        assert type(Snake({})).__name__ == 'Snake'

    def test_snake_has_head(self):
        assert self.get_snake().head == (10,15)

    def test_snake_has_body(self):
        assert self.get_snake().body == [(11,15),(11,16),(11,17)]

    def test_snake_has_health(self):
        assert self.get_snake().health == 100

    def test_snake_has_id(self):
        assert self.get_snake().id == 'abcd1234'

    def test_snake_has_coordinates(self):
        snake = self.get_snake()
        assert snake.coordinates == [(10,15),(11,15),(11,16),(11,17)]
