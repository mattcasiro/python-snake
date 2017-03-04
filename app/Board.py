#!/usr/bin/env python

# Battlesnake 2017 
# Casiro, Chan, Middleton
# Board Class file 

class Board:
    def __init__(self, data):
        # Extract basics
        self.game_id = data['game_id']
        self.height = data['height']
        self.width = data['width']
        self.game_turn = data['turn']
        self.our_id = data['you']

        # Extract arrays
        self.snakes, self.our_snake = get_live_snakes(data['snakes'])
        self.dead_snakes = get_dead_snakes(data['dead_snakes'])
        self.foods = data['food']

    def get_live_snakes(self, raw_snakes):
        snakes = []
        for raw_snake in raw_snakes:
            if raw_snake['id'] == self.our_id:
                our_snake = Snake(raw_snake)
            else:
                snakes.append(Snake(raw_snake))

        return snakes, our_snake

    def get_dead_snakes(self, raw_snakes):
        dead_snakes = []
        for raw_snake in raw_snakes:
            dead_snakes.append(Snake(raw_snake))

        return dead_snakes
