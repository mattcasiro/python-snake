#!/usr/bin/env python

# Battlesnake 2017 
# Casiro, Chan, Middleton
# Board Class file

from random import randint

class Taunt:
    def populate_array(self):
        return ["My food! Bork Bork Bork!",
                "BORK! BORK! BORK! BORK!",
                "Crush! Kill! Destory!",
                "Life sure is ruff.:P",
                "I am a chocolate brown caboose of doom!",
                "Treats, yum yum yum!",
                "I beat cancer, I'll beat you too.",
                "GO FOR THE EYES!",
                "I am the alpha!",
                "Strudel rules!"]

    def grab_taunt(self):
        choice = randint(0,len(self.taunt_array) - 1)
        return self.taunt_array[choice]

    def __init__(self):
        self.taunt_array = populate_array()
        
