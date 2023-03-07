class Goblin:
    #constructor
    def __init__(self, level):
        self._name = Goblin
        self._level = level
        self._vigor = 3 + level
        self._str = 2 + level
        self._dex = 4 + (level*2)
        self._int = 1
        self._health = self._vigor * 4 

    #methods
