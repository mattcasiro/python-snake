class Snake:
    def __init__(self, data):
        self._data = data

    @property
    def id(self):
        return self._data['id']

    @property
    def coordinates(self):
        return self._data['coords']

    @property
    def head(self):
        return self.coordinates[0]

    @property
    def body(self):
        return self.coordinates[1:]

    @property
    def health(self):
        return self._data['health_points']
