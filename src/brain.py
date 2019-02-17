"""Brain Module"""
import math # type: ignore
from operator import itemgetter#attrgetter
from typing import List, Optional
from src.snake import Snake
from src.board import Board
from src.coordinate import Coordinate


class Brain:
    """Control which move the snake makes."""
    def __init__(self, my_id: str, board: Board) -> None:
        self.hunger_threshold = 45
        self.board: Board = board
        self.my_id: str = my_id
        self.other_snakes: List[Snake] = self.board.get_other_snakes(my_id)
        self.me: Snake = next((snake for snake in self.board.snakes if snake.id == my_id))

    def get_decision(self) -> str:
        """Get the move which the snake will make this turn."""
        moves_to_food = self.get_moves_for_nearest_food()
        valid_moves = self.get_valid_moves()
        decision = None

        # in case the head is right next to the tail, if there aren't any valid moves, move towards tail
        if not valid_moves:
            return self.follow_tail()[0]

        if self.me.health < self.hunger_threshold:
            if moves_to_food:
                decision = next((move for move in moves_to_food if move in valid_moves), None)
        else:
            loop_moves = self.follow_tail()#self.circle_perimeter()#self.follow_tail()
            if loop_moves:
                decision = next((move for move in loop_moves if move in valid_moves), None)
 
        if not decision:
            decision = valid_moves[0]
 
        return decision


    def get_valid_moves(self) -> List[str]:
        """Return the moves which won't immediately get the snake killed."""
        moves = self.get_valid_moves_helper(True)

        if not moves or not len(moves):
            moves = self.get_valid_moves_helper(False)
            #print("resorted to not avoiding headons")

        return moves


    def get_valid_moves_helper(self, avoid_collisions: bool) -> List[str]:
        """Return moves which are deemed valid, option to not avoid headons"""
        moves = ["left", "right", "up", "down"]
        valid_moves = []
        collision_coordinates = [coordinate for snake in self.board.snakes for coordinate in snake.coordinates] #snake.coordinates[:-1]]
        if avoid_collisions:
            collision_coordinates = collision_coordinates + self.get_threatening_snakes_moves()

        #remove this snake's tail from array of "invalid moves"
        tail = self.me.coordinates[-1]
        if tail in collision_coordinates:
            collision_coordinates.remove(tail)

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

    def get_moves_for_nearest_food(self) -> Optional[List[str]]:
        """Get move options for getting to nearest food"""
        nearest_food = self.get_nearest_food()
        if nearest_food is None:
            return None

        options = []
        x_diff = nearest_food.x - self.me.head.x
        y_diff = nearest_food.y - self.me.head.y

        if x_diff != 0:
            options.append("left" if x_diff < 0 else "right")
        if y_diff != 0:
            options.append("up" if y_diff < 0 else "down")
        if not options:
            return None

        return options

    def follow_tail(self) -> List[str]:
        """Get moves for getting to tail."""
        tail = self.me.coordinates[len(self.me.coordinates) - 1]
        return self.get_moves_to(tail)

#    def circle_perimeter(self) -> List[str]:
#        """Do some laps."""
#        #change this to an or, and it'll go to nearest corner and loop there
#        if (self.me.head.x != 0 and self.me.head.x != self.board.width -1) and \
#           (self.me.head.y != 0 and self.me.head.y != self.board.width -1):
#            move = self.go_to_nearest_wall()
#            print('go_to_wall')
#        else:
#            move = self.follow_wall()
#            print('follow_to_wall')
# 
#        return [move]

    def go_to_nearest_wall(self) -> str:
        """Find the nearest wall that you're not already at."""
        left_dist = ("left", self.me.head.x)
        right_dist = ("right", (self.board.width - 1) - self.me.head.x)
        up_dist = ("up", self.me.head.y)
        down_dist = ("down", (self.board.width -1) - self.me.head.y)

        distances = [left_dist, right_dist, up_dist, down_dist]
        distances = [distance for distance in distances if distance[1] != 0]
        least_dist = min(distances, key=itemgetter(1))
        return least_dist[0]

#    def follow_wall(self) -> str:
#        """Follow wall which the snake is currently on."""
#
#        second = None
#        third = None
#
#        print("wall: " + str(self.board.width))
#        print("head: (" + str(self.me.head.x) + ", " + str(self.me.head.y) + ")")
#
#        if len(self.me.coordinates) > 1:
#            second = self.me.coordinates[1]
#            print("second: (" + str(second.x) + ", " + str(second.y) + ")")
#            if len(self.me.coordinates) > 2:
#                third = self.me.coordinates[2]
#                print("third: (" + str(third.x) + ", " + str(third.y) + ")")
#
#        if self.me.head.x == 0 or self.me.head.x == self.board.width -1:
#            if second is not None and second.y > self.me.head.y or second is None:
#                return 'up'
#            elif second is not None and second.y < self.me.head.y:
#                return 'down'
#            else:
#                if third is not None:
#                    if third.y > self.me.head.y:
#                        return 'up'
#                    else:
#                        return 'down'
# 
#        if self.me.head.y == 0 or self.me.head.y == self.board.width - 1:
#            if second is not None and second.x > self.me.head.x or second is None:
#                return 'left'
#            elif second is not None and second.x < self.me.head.x:
#                return 'right'
#            else:
#                if third is not None:
#                    if third.x > self.me.head.x:
#                        return 'left'
#                    else:
#                        return 'right'
#        print("Reached unexpected condition in follow_wall")
#        return "left"

    def get_moves_to(self, coord: Coordinate) -> List[str]:
        """Get move options for getting to given coordinate."""
        options = []
        x_diff = self.me.head.x - coord.x
        y_diff = self.me.head.y - coord.y

        #print(str(self.me.head.x) + "," + str(self.me.head.y))
        #print(str(y_diff) + "; " + str(x_diff))
        if x_diff > 0:
            options.append('left')
        elif x_diff < 0:
            options.append('right')

        if y_diff > 0:
            options.append('up')
        elif y_diff < 0:
            options.append('down')

        if abs(y_diff) > abs(x_diff):
            options.reverse()
        return options
