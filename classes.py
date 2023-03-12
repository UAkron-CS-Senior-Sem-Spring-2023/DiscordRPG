# All character classes
# All start with 20 points distributed amonf the stats
# All gain 5 skill points to be distributed after level up

#class Character:
    # constructor
    #def __init__(self, name, characterClass):
        #self._name = name
        #self._charcterClass = characterClass
        #self._level = 1

    # methods
    #def viewCharacter(self):
        #return (self._name + "\n" + self._charcterClass + " Level " + str(self._level))

    #def levelUp(self):
        #self.level = self.level + 1

class Cleric:
    # constructor
    def __init__(self):
        self._name = "Cleric"
        self._vigor = 6
        self._str = 6
        self._dex = 2
        self._int = 6
        self._health = self._vigor * 4
        self._mana = self._int * 5

    # methods
    def displayStats(self):
        return (self._name + "\nHealth: " + str(self._health) + "   Mana: " + str(self._mana) + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))
    
class Hunter:
    # constructor
    def __init__(self):
        self._name = "Hunter"
        self._vigor = 5
        self._str = 2
        self._dex = 8
        self._int = 5
        self._health = self._vigor * 4
        self._mana = self._int * 5

    # methods
    def displayStats(self):
        return (self._name + "\nHealth: " + str(self._health) + "   Mana: " + str(self._mana) + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Mage:
    # constructor
    def __init__(self):
        self._name = "Mage"
        self._vigor = 5
        self._str = 2
        self._dex = 3
        self._int = 10
        self._health = self._vigor * 4
        self._mana = self._int * 5

    #methods
    def displayStats(self):
        return (self._name + "\nHealth: " + str(self._health) + "   Mana: " + str(self._mana) + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Paladin:
    # constructor
    def __init__(self):
        self._name = "Paladin"
        self._vigor = 7
        self._str = 7
        self._dex = 2
        self._int = 4
        self._health = self._vigor * 4
        self._mana = self._int * 5

    # methods
    def displayStats(self):
        return (self._name + "\nHealth: " + str(self._health) + "   Mana: " + str(self._mana) + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Thief:
    # constructor
    def __init__(self):
        self._name = "Theif"
        self._vigor = 4
        self._str = 2
        self._dex = 8
        self._int = 6
        self._health = self._vigor * 4
        self._mana = self._int * 5

    # methods
    def displayStats(self):
        return (self._name + "\nHealth: " + str(self._health) + "   Mana: " + str(self._mana) + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Warrior:
    # constructor
    def __init__(self):
        self._name = "Warrior"
        self._vigor = 6
        self._str = 8
        self._dex = 4
        self._int = 2
        self._health = self._vigor * 4
        self._mana = self._int * 5

    # methods
    def displayStats(self):
        return (self._name + "\nHealth: " + str(self._health) + "   Mana: " + str(self._mana) + "\nVIG: " + str(self._vigor) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))
