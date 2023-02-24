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
        self._name = "Cleric"
        self._vigor = 6
        self._str = 6
        self._dex = 2
        self._int = 6

    #methods
    def displayStats(self):
        return (self._name + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))
    
class Hunter:
    #Constructor
    def __init__(self):
        self._name = "Hunter"
        self._vigor = 5
        self._str = 5
        self._dex = 8
        self._int = 2

    #methods
    def displayStats(self):
        return (self._name + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Mage:
    #Constructor
    def __init__(self):
        self._name = "Mage"
        self._vigor = 5
        self._str = 2
        self._dex = 3
        self._int = 10

    #methods
    def displayStats(self):
        return (self._name + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Paladin:
    #Constructor
    def __init__(self):
        self._name = "Paladin"
        self._vigor = 7
        self._str = 7
        self._dex = 2
        self._int = 4

    #methods
    def displayStats(self):
        return (self._name + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Thief:
    #Constructor
    def __init__(self):
        self._name = "Theif"
        self._vigor = 4
        self._str = 2
        self._dex = 8
        self._int = 6

    #methods
    def displayStats(self):
        return (self._name + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Warrior:
    #Constructor
    def __init__(self):
        self._name = "Warrior"
        self._vigor = 6
        self._str = 8
        self._dex = 4
        self._int = 2

    #methods
    def displayStats(self):
        return (self._name + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))
