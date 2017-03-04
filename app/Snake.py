#!/usr/bin/env python

# Battlesnake 2017 
# Casiro, Chan, Middleton
# Snake Class file 

class Snake:
    def get_moves(self, head):
        #assign left, right, up, and down variables
        moves = {
            'left': [head[0] - 1, head[1]], 
            'right': [head[0] + 1, head[1]],
            'up': [head[0], head[1] - 1],
            'down': [head[0], head[1] + 1],
        }

        return moves

    def __init__(self, data):
        #parse data array for snake indormation
        self.coords = data['coords']
        self.health = data['health_points']
        self.id = data['id']
        self.name = data['name']
        self.taunt = data['taunt']
        self.length = len(self.coords)

        #create a head
        self.head = self.coords[0]
        self.moves = self.get_moves(self.head)
