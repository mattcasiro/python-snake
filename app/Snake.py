#!/usr/bin/env python

# Battlesnake 2017 
# Casiro, Chan, Middleton
# Snake Class file 

class Snake:
    def __init__(self, data):
        #parse data array for snake indormation
        self.coords = data['coords']
        self.health = data['health']
        self.id = data['id']
        self.name = data['name']
        self.taunt = data['taunt']
        self.length = len(coords)

        #create a head
        self.head = self.coords[0]

        #assign left, right, up, and down variables
        self.moves = {
            [self.head[0] - 1, head[1]] : 'left', 
            [self.head[0] + 1, head[1]] : 'right',
            [head[0], head[1] - 1] : 'up',
            [head[0], head[1] + 1] : 'down',
        }
