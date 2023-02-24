class Character:
    #constructor
    def __init__(self, name, characterClass):
        self._name = name
        self._charcterClass = characterClass
        self._level = 1

    #methods
    def viewCharacter(self):
        print(self._name + self._charcterClass + self._level)

    def levelUp(self):
        self.level = self.level + 1