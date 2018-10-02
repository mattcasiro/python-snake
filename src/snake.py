class Snake:
    def __init__(self, data):
        self._data = data

        # Initialize properties, but lets not bother setting them yet
        self._coordinates = None
        self._head        = None
        self._body        = None
        self._health      = None
        self._id          = None
        self._name        = None
        self._taunt       = None
        self._length      = None

    @property
    def id(self):
        if not self._id:
            self._id = self._data['id']

        return self._id

    @property
    def coordinates(self):
        if not self._coordinates:
            self._coordinates = self._data['coords']

        return self._coordinates

    @property
    def head(self):
        if not self._head:
            self._head = self.coordinates[0]

        return self._head

    @property
    def body(self):
        if not self._body:
            self._body = self.coordinates[1:]

        return self._body

    @property
    def health(self):
        if not self._health:
            self._health = self._data['health_points']

        return self._health
