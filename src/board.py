""" Board Module """

class Board:
    """ This class represents the board which tracks the cooardinates for all
    snakes and food in a game"""
    def __init__(self, data):
        self._data = data

    @property
    def snake_list(self):
        """snake_list retreives the list of snakes from the board data"""
        return self._data['snakes']

    @property
    def food_list(self):
        """food_list retreives the list of food from the board data"""
        return self._data['food']
