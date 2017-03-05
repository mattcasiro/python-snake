#!/usr/bin/env python

import Snake
import Food

# Battlesnake 2017 
# Casiro, Chan, Middleton
# Board Class file 

class Board:
    def get_live_snakes(self, raw_snakes):
        snakes = []
        for raw_snake in raw_snakes:
            if raw_snake['id'] == self.our_id:
                our_snake = Snake.Snake(raw_snake)
            else:
                snakes.append(Snake.Snake(raw_snake))

        return snakes, our_snake

    def get_dead_snakes(self, raw_snakes):
        dead_snakes = []
        for raw_snake in raw_snakes:
            dead_snakes.append(Snake.Snake(raw_snake))

        return dead_snakes

    def get_bad_squares(self):
        # Don't hit ourselves
        bad = self.our_snake.coords
        for snake in self.snakes:
            # Don't hit other snakes
            bad += snake.coords
            # Avoid head-on collisions
            bad += snake.moves.values()

        # Left/Right walls are bad!
        for i in range(self.height):
            bad += [[-1, i], [self.width, i]]

        # Top/Bottom walls are bad!
        for i in range(self.width):
            bad += [[i, -1], [self.height, i]]

        # DEBUG:
        #print bad

        return bad

    def associate_nearest_foods(self, snakes, our_snake, foods):
        all_snakes = snakes + [our_snake]
        # check for nulls
        if not foods or not all_snakes:
            print("foods or all_snakes null")
            return

        nearest_foods = {}
        for snake in all_snakes:
            #calculate nearest food for current snake:
            i=0
            nearest_index = 0
            nearest_distance = 999999
            for food in foods:
                #calculate absolute val of differences between head and food x & y
                distance = abs(snake.head[0] - food[0]) + abs(snake.head[1] - food[1])
                #compare distance of current food to other foods
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_index = i
                i += 1
            #put current snake's nearest food in dictionary of snake:nearestfoods
            nearest_foods[snake.id] = foods[nearest_index]
        print nearest_foods
        return nearest_foods


    def __init__(self, data):
        # Extract basics
        self.game_id = data['game_id']
        self.height = data['height']
        self.width = data['width']
        self.game_turn = data['turn']
        self.our_id = data['you']

        # Extract arrays
        self.snakes, self.our_snake = self.get_live_snakes(data['snakes'])
        self.dead_snakes = self.get_dead_snakes(data['dead_snakes'])
        self.foods = data['food']
        self.nearest_foods = self.associate_nearest_foods(self.snakes, self.our_snake, self.foods)
