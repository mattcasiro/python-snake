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

        #assign left, right, up, and down variables
        self.left = coords[0][0] - 1
        self.right = coords[0][0] + 1
        self.up = coords[0][1] - 1
        self.down = coords[0][1] + 1
