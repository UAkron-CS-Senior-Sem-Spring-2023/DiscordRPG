class Character:
    #constructor
    def __init__(self, name, characterClass):
        self._name = name
        self._charcterClass = characterClass
        self._level = 1

    #methods
    def viewCharacter(self):
        return (self._name + "\n" + self._charcterClass + " Level " + str(self._level))

    def levelUp(self):
        self.level = self.level + 1

class Cleric:
    #Constructor
    def __init__(self):
        self._vigor = 6
        self._str = 6
        self._dex = 2
        self._int = 6

    #methods

class Hunter:
    #Constructor
    def __init__(self):
        self._vigor = 5
        self._str = 5
        self._dex = 8
        self._int = 2

    #methods

class Mage:
    #Constructor
    def __init__(self):
        self._vigor = 5
        self._str = 2
        self._dex = 3
        self._int = 10

    #methods

class Paladin:
    #Constructor
    def __init__(self):
        self._vigor = 7
        self._str = 7
        self._dex = 2
        self._int = 4

    #methods

class Thief:
    #Constructor
    def __init__(self):
        self._vigor = 4
        self._str = 2
        self._dex = 8
        self._int = 6

    #methods

class Warrior:
    #Constructor
    def __init__(self):
        self._vigor = 6
        self._str = 8
        self._dex = 4
        self._int = 2

    #methods
