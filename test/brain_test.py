import pytest # type: ignore
import copy # type: ignore
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
        nearest_food = brain.get_nearest_food()
        assert brain.get_moves_to(nearest_food) == ["right", "down"]

    def test_brain_can_make_decision(self):
        brain = self.get_brain(self.main_snake + self.equal_snake, self.foods, self.width)
        assert brain.get_decision() == "left"

        brain = self.get_brain(self.main_snake, self.foods, self.width)
        assert brain.get_decision() == "right"

    def test_brain_dies_when_stuck(self):
        stuck_snake = list(copy.deepcopy(self.main_snake))
        stuck_snake[0]["body"] = [(1,0), (0,0), (0,1)]

        blocking_snake = list(copy.deepcopy(self.equal_snake))
        blocking_snake[0]["body"] = [(0,2),(1,2),(1,1),(2,1),(2,0),(3,0)] 

        brain = self.get_brain(stuck_snake + blocking_snake, self.foods, self.width)
        assert brain.get_decision() == "left"

    def test_brain_can_get_moves_to_coord(self):
        brain = self.get_brain(self.main_snake, self.foods, self.width)
        assert brain.get_moves_to(Coordinate(9,0)) == ["right", "up"]
        assert brain.get_moves_to(Coordinate(9,2)) == ["right"]
        assert brain.get_moves_to(Coordinate(9,9)) == ["right", "down"]
        assert brain.get_moves_to(Coordinate(2,9)) == ["down"]
        assert brain.get_moves_to(Coordinate(0,9)) == ["down", "left"]
        assert brain.get_moves_to(Coordinate(0,2)) == ["left"]
        assert brain.get_moves_to(Coordinate(0,0)) == ["left", "up"]

    def test_brain_can_follow_tail(self):
        snake = copy.deepcopy(self.main_snake)
        snake[0]["body"] = [(6,5), (6,6), (7,6), (7,7,)]
        brain = self.get_brain(snake, self.foods, self.width)
        assert brain.follow_tail() == ["down", "right"]

        snake[0]["body"].reverse()
        brain = self.get_brain(snake, self.foods, self.width)
        assert brain.follow_tail() == ["up", "left"]

        snake = copy.deepcopy(self.main_snake)
        snake[0]["body"] = [(6,5), (6,6), (7,6), (7,7,), (7,8), (6,8), (5,8), (4,8)]
        brain = self.get_brain(snake, self.foods, self.width)
        assert brain.follow_tail() == ["down", "left"]

        snake[0]["body"].reverse()
        brain = self.get_brain(snake, self.foods, self.width)
        assert brain.follow_tail() == ["up", "right"]

    def test_brain_can_tell_if_snake_is_greatest_length(self):
        brain = self.get_brain(self.main_snake, self.foods, self.width)
        assert brain.get_snake_is_safe_length() == True

        brain = self.get_brain(self.main_snake+self.smol_snek, self.foods, self.width)
        assert brain.get_snake_is_safe_length() == False

        brain = self.get_brain(self.main_snake+self.equal_snake, self.foods, self.width)
        assert brain.get_snake_is_safe_length() == False

        bigger_snek = copy.deepcopy(self.main_snake)
        bigger_snek[0]["body"] = [(2,2), (2,3), (3,3), (3,4)]
        brain = self.get_brain(bigger_snek+self.smol_snek, self.foods, self.width)
        assert brain.get_snake_is_safe_length() == True

        brain = self.get_brain(self.smol_snek+bigger_snek, self.foods, self.width)
        assert brain.get_snake_is_safe_length() == False

    def test_brain_can_foods_sorted_by_proximity(self):
        additional_foods = [(14,11), (0,7), (0,14)]
        brain = self.get_brain(self.main_snake, self.foods+additional_foods, self.width)
        sorted_foods = brain.get_foods_sorted_by_proximity()
        assert str(sorted_foods[0]) == "(0,7)"
        assert str(sorted_foods[1]) == "(10,5)"
        assert str(sorted_foods[2]) == "(6,12)"
        assert str(sorted_foods[3]) == "(0,14)"
        assert str(sorted_foods[4]) == "(14,11)"


    def test_pathing_with_foods(self):
        foods = [
            (8,0)
        ]

        a = copy.deepcopy(self.main_snake)
        a[0]["body"] = [
            (6,10),
            (6,9),
            (6,8),
            (6,7),
            (5,7),
            (4,7),
            (4,6),
            (4,5),
            (3,5),
            (2,5),
            (2,6),
            (3,6),
            (3,7),
            (3,8),
            (4,8),
            (4,9),
        ]

        b = copy.deepcopy(self.main_snake)
        b[0]["body"] = [
            (1,7),
            (2,7),
            (2,8),
            (2,9),
            (2,10),
            (1,10),
            (0,10),
            (0,9),
            (0,8),
            (0,7),
            (0,6),
            (0,5),
            (0,4),
            (0,3),
            (0,2),
            (0,1)
        ]

        c = copy.deepcopy(self.main_snake)
        c[0]["body"] = [
            (10,8),
            (10,9),
            (9,9),
            (8,9),
            (7,9),
            (7,8),
            (7,7),
            (7,6),
            (7,5)
        ]

        brain = self.get_brain(a+b+c, foods, 11)
        assert brain.get_decision() ==  "left"

    def test_snake_avoids_self(self):
        a = copy.deepcopy(self.main_snake)
        a[0]["body"] = [
            (5,5),
            (6,5),
            (6,5)
        ]
        brain = self.get_brain(a, [], 11)
        assert brain.get_decision() != "right"

    def test_food_path_allows_escape(self):
        foods = [
            # Food:<> Food:<X:2 > Food:<X:5 Y:4 > Food:<X:12 > Food:<X:9 Y:2 > Food:<X:4 Y:5 > Food:<X:13 Y:13 > Food:<X:6 Y:6 > Food:<X:2 Y:6 >
            (0,0), (1,0), (2,0), (12,0),
            (9,2),
            (5,4), (12,4),
            (4,5),
            (6,6),
            (13,13),
        ]

        a = copy.deepcopy(self.main_snake)
        a[0]["body"] = [
        # Body:<X:12 Y:4 > Body:<X:13 Y:4 > Body:<X:12 Y:4 > Body:<X:11 Y:4 > Body:<X:11 Y:5 > Body:<X:12 Y:5 > Body:<X:13 Y:5 > Body:<X:13 Y:6 > Body:<X:12 Y:6 > Body:<X:11 Y:6 > Body:<X:11 Y:7 > Body:<X:12 Y:7 > Body:<X:12 Y:8 > Body:<X:11 Y:8 > Body:<X:11 Y:9 > Body:<X:11 Y:10 > Body:<X:10 Y:10 > Body:<X:9 Y:10 > Body:<X:9 Y:11 > Body:<X:9 Y:12 > Body:<X:8 Y:12 > Body:<X:7 Y:12 > Body:<X:6 Y:12 > Body:<X:5 Y:12 > Body:<X:5 Y:13 > Body:<X:4 Y:13 > Body:<X:3 Y:13 > Body:<X:2 Y:13 > Body:<X:2 Y:14 > Body:<X:3 Y:14 > Body:<X:4 Y:14 > Body:<X:5 Y:14 > Body:<X:6 Y:14 > Body:<X:6 Y:13 > Body:<X:7 Y:13 > Body:<X:8 Y:13 > Body:<X:9 Y:13 > Body:<X:10 Y:13 > Body:<X:10 Y:12 > Body:<X:10 Y:11 > Body:<X:11 Y:11 > Body:<X:12 Y:11 > Body:<X:12 Y:10 > Body:<X:12 Y:9 > Body:<X:13 Y:9 > Body:<X:13 Y:8 > Body:<X:14 Y:8 > Body:<X:14 Y:7 > Body:<X:14 Y:6 > Body:<X:14 Y:5 > Body:<X:14 Y:4 > Body:<X:14 Y:3 > Body:<X:14 Y:2 > Body:<X:13 Y:2 > Body:<X:13 Y:3 > Body:<X:12 Y:3 > Body:<X:11 Y:3 > Body:<X:10 Y:3 > Body:<X:10 Y:4 > Body:<X:10 Y:5 > Body:<X:10 Y:6 > Body:<X:10 Y:7 > Body:<X:10 Y:8 > Body:<X:9 Y:8 > Body:<X:8 Y:8 > Body:<X:7 Y:8 > Body:<X:6 Y:8 > Body:<X:5 Y:8 > Body:<X:4 Y:8 > Body:<X:3 Y:8 > 
            # (12, 4),
            # (13, 4),
            # (12, 4),
            # (11, 4),
            # (11, 5),
            # (12, 5),
            # (13, 5),
            # (13, 6),
            # (12, 6),
            # (11, 6),
            # (11, 7),
            # (12, 7),
            # (12, 8),
            # (11, 8),
            (11, 9),
            (11, 10),
            (10, 10),
            (9, 10),
            (9, 11),
            (9, 12),
            (8, 12),
            (7, 12),
            (6, 12),
            (5, 12),
            (5, 13),
            (4, 13),
            (3, 13),
            (2, 13),
            (2, 14),
            (3, 14),
            (4, 14),
            (5, 14),
            (6, 14),
            (6, 13),
            (7, 13),
            (8, 13),
            (9, 13),
            (10, 13),
            (10, 12),
            (10, 11),
            (11, 11),
            (12, 11),
            (12, 10),
            (12, 9),
            (13, 9),
            (13, 8),
            (14, 8),
            (14, 7),
            (14, 6),
            (14, 5),
            (14, 4),
            (14, 3),
            (14, 2),
            (13, 2),
            (13, 3),
            (12, 3),
            (11, 3),
            (10, 3),
            (10, 4),
            (10, 5),
            (10, 6),
            (10, 7),
            (10, 8),
            (9, 8),
            (8, 8),
            (7, 8),
            (6, 8),
            (5, 8),
            (4, 8),
            (3, 8),
            (2,8), (2, 7), (1,7), (1,8), (0,8), (0,9), (0,10), (0,11), (1,11), (1,10), (2,10), (3,10), (4,10)
        ]

        brain = self.get_brain(a, foods, 15)
        assert brain.get_decision() != "up"
