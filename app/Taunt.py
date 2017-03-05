#!/usr/bin/env python

# Battlesnake 2017 
# Casiro, Chan, Middleton
# Board Class file

from random import randint

class Taunt:
    def populate_array(self):
        taunt_file = open('taunts.txt', 'r')
        for line in taunt_file:
            self.taunt_array.append(line)
        taunt_file.close()

    def grab_taunt(self):
        choice = randint(0,len(self.taunt_array) - 1)
        return self.taunt_array[choice]

    def __init__(self):
        self.taunt_array = []
        self.populate_array()
        
