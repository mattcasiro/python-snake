"""Brain Module"""
import math # type: ignore
from typing import List, Optional
from src.snake import Snake
from src.board import Board
from src.coordinate import Coordinate


class Brain:
    """Control which move the snake makes."""
    def __init__(self, my_id: str, board: Board):
        self.board: Board = board
        self.my_id: str = my_id
        self.other_snakes: List[Snake] = self.board.get_other_snakes(my_id)
        self.me: Snake = next((snake for snake in self.board.snakes if snake.id == my_id))

    def get_valid_moves(self) -> List[str]:
        """Return the moves which won't immediately get the snake killed."""
        moves = ["left", "right", "up", "down"]
        valid_moves = []
        collision_coordinates = [coordinate for snake in self.board.snakes for coordinate in snake.coordinates]
        collision_coordinates = collision_coordinates + self.get_threatening_snakes_moves()

        for move in moves:
            move_coordinate = getattr(self.me.head, "get_"+move)()
            if self.board.is_coordinate_in_bounds(move_coordinate) and move_coordinate not in collision_coordinates:
                valid_moves.append(move)

        return valid_moves

    def get_nearest_food(self) -> Optional[Coordinate]:
        """Get the food item which has coordinates closest to this snake's head."""
        closest_food = (Coordinate((0,0)), 9999.0)

        for food in self.board.foods:
            x_diff = self.me.head.x - food.x
            y_diff = self.me.head.y - food.y
            distance = math.sqrt( x_diff * x_diff + y_diff * y_diff )

            if distance < closest_food[1]:
                closest_food = (food, distance)

        if closest_food[1] == 9999.0:
            return None

        return closest_food[0]

    def get_threatening_snakes_moves(self) -> List[Coordinate]:
        """Get the coordinates which will result in head-on collisions.""" 
        #note, we can ignore snakes smaller than us.
        danger_snakes = [snake for snake in self.board.get_other_snakes(self.my_id) if len(snake.coordinates) >= len(self.me.coordinates)]
        return [snake_moves for snake in danger_snakes for snake_moves in snake.get_all_moves()]
