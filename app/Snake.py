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
        self.head = coords[0]

        #assign left, right, up, and down variables
        self.left = head[0] - 1
        self.right = head[0] + 1
        self.up = head[1] - 1
        self.down = head[1] + 1
