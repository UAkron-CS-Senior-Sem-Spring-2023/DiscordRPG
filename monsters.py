# All monster classes
# All locations will have four different monster types
# Locations have different difficulties(Easy, Medium, Hard)
#
# Easy Locations(Forest, Cave)
# 2 - 15(level 1) + 4(per level) - "weaker" than player
# 1 - 20(level 1) + 5(per level) - "on par" with player
# 1 - 25(level 1) + 7(per level) - "area miniboses"
#
# Medium Locations
#
# Hard Locations
#

# Location - Forest(Easy)
# Weaker - Boar and Wolf
# On Par - Elf
# Miniboss - Treant

class Boar:
    # constructor
    def __init__(self, level):
        self._location = "Forest"
        self._name = "Boar"
        self._level = level
        self._vigor = 4 + (self._level*2)
        self._str = 3 + (self._level*2)
        self._dex = 2
        self._int = 1
        self._health = self._vigor * 4 

    # methods
    def displayStats(self):
        return (self._name + " Level: " + str(self._level) + "\nHealth: " + str(self._health) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))
    
class Wolf:
    # constructor
    def __init__(self, level):
        self._location = "Forest"
        self._name = "Wolf"
        self._level = level
        self._vigor = 4 + self._level
        self._str = 3 + (self._level*2)
        self._dex = 2 + self._level
        self._int = 2
        self._health = self._vigor * 4 

    # methods
    def displayStats(self):
        return (self._name + " Level: " + str(self._level) + "\nHealth: " + str(self._health) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Treant:
    # constructor
    def __init__(self, level):
        self._location = "Forest"
        self._name = "Treant"
        self._level = level
        self._vigor = 8 + (self._level*4)
        self._str = 4 + (self._level*3)
        self._dex = 4
        self._int = 2
        self._health = self._vigor * 4 

    #methods
    def displayStats(self):
        return (self._name + " Level: " + str(self._level) + "\nHealth: " + str(self._health) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Elf:
    # constructor
    def __init__(self, level):
        self._location = "Forest"
        self._name = "Elf"
        self._level = level
        self._vigor = 4 + self._level
        self._str = 3
        self._dex = 4 + (self._level*2)
        self._int = 2 + (self._level*2)
        self._health = self._vigor * 4 

    # methods
    def displayStats(self):
        return (self._name + " Level: " + str(self._level) + "\nHealth: " + str(self._health) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

# Location - Cave
# Weaker - Giant Spider and Roper
# On Par - Goblin
# Miniboss - Troll

class GiantSpider:
    # constructor
    def __init__(self, level):
        self._location = "Cave"
        self._name = "Giant Spider"
        self._level = level
        self._vigor = 4 + self._level
        self._str = 2
        self._dex = 4 + (self._level*2)
        self._int = 2
        self._health = self._vigor * 4 

    # methods
    def displayStats(self):
        return (self._name + " Level: " + str(self._level) + "\nHealth: " + str(self._health) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Roper:
    # constructor
    def __init__(self, level):
        self._location = "Cave"
        self._name = "Roper"
        self._level = level
        self._vigor = 4 + self._level
        self._str = 3 + self._level
        self._dex = 3 + self._level
        self._int = 2
        self._health = self._vigor * 4 

    # methods
    def displayStats(self):
        return (self._name + " Level: " + str(self._level) + "\nHealth: " + str(self._health) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Troll:
    # constructor
    def __init__(self, level):
        self._location = "Cave"
        self._name = "Troll"
        self._level = level
        self._vigor = 8 + (self._level*3)
        self._str = 5 + (self._level*3)
        self._dex = 3 + self._level
        self._int = 2
        self._health = self._vigor * 4 

    # methods
    def displayStats(self):
        return (self._name + " Level: " + str(self._level) + "\nHealth: " + str(self._health) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))

class Goblin:
    # constructor
    def __init__(self, level):
        self._location = "Cave"
        self._name = "Goblin"
        self._level = level
        self._vigor = 5 + self._level
        self._str = 3 + (self._level*2)
        self._dex = 5 + (self._level*2)
        self._int = 3
        self._health = self._vigor * 4 

    # methods
    def displayStats(self):
        return (self._name + " Level: " + str(self._level) + "\nHealth: " + str(self._health) + "\nSTR: " + str(self._str) + "\nDEX: " + str(self._dex) + "\nINT: " + str(self._int))
