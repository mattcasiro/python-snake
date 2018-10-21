""" Board Module """

class Board:
    """Track the cooardinates for all snakes and food in the game."""
    def __init__(self, data):
        self._data = data

    @property
    def snakes(self):
        """Retreive the list of snakes from the board data."""
        return self._data['snakes']

    @property
    def foods(self):
        """Retreive the list of food from the board data."""
        return self._data['food']
