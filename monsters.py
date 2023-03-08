class Goblin:
    #constructor
    def __init__(self, level):
        self._name = "goblin"
        self._level = level
        self._vigor = 3 + self._level
        self._str = 2 + self._level
        self._dex = 4 + (self._level*2)
        self._int = 2
        self._health = self._vigor * 4 

    #methods

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
