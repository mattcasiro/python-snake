"""Brain Module"""
from src.snake import Snake
from src.board import Board
from src.coordinate import Coordinate
from typing import List


class Brain:
    """Control which move the snake makes."""
    def __init__(self, me: Snake, other_snakes: List[Snake], foods: List[Coordinate], board: Board):
        self.me = me
        self.other_snakes = other_snakes
        self.foods = foods
        self.board = board

    def get_valid_moves(self) -> List[str]:
        """Return the moves which won't immediately get the snake killed."""
        moves = ["left", "right", "up", "down"]
        valid_moves = []

        for move in moves:
            move_coordinate = getattr(self.me.head, "get_"+move)

            if not self.board.is_coordinate_in_bounds(move_coordinate):
                continue

            is_collision = False
            for snake in self.other_snakes:
                if snake.contains_coordinate(move_coordinate):
                    is_collision = True
                    break

            if is_collision:
                continue

            valid_moves.append(move)

        return valid_moves

    def get_nearest_food(self):
        """Get the food item which has coordinates closest to this snake's head."""
        closest_food = (None, 9999)

        for food in self.foods:
            distance = self.me.head
            if closest_food[0] is None or distance < closest_food[1]:
                closest_food = (food, distance)

        if closest_food[0] is None:
            return None

        return closest_food
