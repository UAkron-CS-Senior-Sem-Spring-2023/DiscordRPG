class Boar:
    #constructor
    def __init__(self, level):
        self._name = "boar"
        self._level = level
        self._vigor = 4 + (self._level*2)
        self._str = 3 + (self._level*2)
        self._dex = 2
        self._int = 1
        self._health = self._vigor * 4 

    #methods

class Wolf:
    #constructor
    def __init__(self, level):
        self._name = "wolf"
        self._level = level
        self._vigor = 4 + self._level
        self._str = 3 + (self._level*2)
        self._dex = 2 + self._level
        self._int = 2
        self._health = self._vigor * 4 

    #methods

class Goblin:
    #constructor
    def __init__(self, level):
        self._name = "goblin"
        self._level = level
        self._vigor = 5 + self._level
        self._str = 3 + self._level
        self._dex = 5 + (self._level*2)
        self._int = 3
        self._health = self._vigor * 4 

    #methods
