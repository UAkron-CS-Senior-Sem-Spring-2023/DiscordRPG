import mysql.connector
from mysql.connector import errorcode

class Character:
    # constructor
    def __init__(self, name, characterClass, userID):
        self._name = name
        self._charcterClass = characterClass.lower()
        self._userID = userID
        self._level = 0
        self._vigor = 0
        self._str = 0
        self._dex = 0
        self._int = 0
        self._health = self._vigor * 4
        self._mana = self._int * 5
        self._maxHealth = self._health
        self._maxMana = self._mana
        match characterClass.lower():
            case "cleric":
                self._vigor = 6
                self._str = 6
                self._dex = 2
                self._int = 6
                self._health = self._vigor * 4
                self._mana = self._int * 5
                self._maxHealth = self._health
                self._maxMana = self._mana
            case "hunter":
                self._vigor = 5
                self._str = 2
                self._dex = 8
                self._int = 5
                self._health = self._vigor * 4
                self._mana = self._int * 5
                self._maxHealth = self._health
                self._maxMana = self._mana
            case "mage":
                self._vigor = 5
                self._str = 2
                self._dex = 3
                self._int = 10
                self._health = self._vigor * 4
                self._mana = self._int * 5
                self._maxHealth = self._health
                self._maxMana = self._mana
            case "paladin":
                self._vigor = 7
                self._str = 7
                self._dex = 2
                self._int = 4
                self._health = self._vigor * 4
                self._mana = self._int * 5
                self._maxHealth = self._health
                self._maxMana = self._mana
            case "theif":
                self._vigor = 4
                self._str = 2
                self._dex = 8
                self._int = 6
                self._health = self._vigor * 4
                self._mana = self._int * 5
                self._maxHealth = self._health
                self._maxMana = self._mana
            case "warrior":
                self._vigor = 6
                self._str = 8
                self._dex = 4
                self._int = 2
                self._health = self._vigor * 4
                self._mana = self._int * 5
                self._maxHealth = self._health
                self._maxMana = self._mana
            case _:
                print("Invalid class name. Please choose one of the classes")
        try:
            cnx = mysql.connector.connect(user='bot', password='203v2Xm&zXQK', host='45.31.16.49', database='disrpg')
            cursor = cnx.cursor()
            query = ("INSERT INTO characters (UserID, CharacterName, CharacterClass, CharacterLevel, VigorBase, VigorCurrent, StrBase, StrCurrent, DexBase, DexCurrent, IntBase, IntCurrent, HealthBaseMax, HealthMax, HealthCurrent, ManaBaseMax, ManaMax, ManaCurrent) VALUES (%(UserID)s, %(CharacterName)s, %(CharacterClass)s, %(CharacterLevel)s, %(VigorBase)s, %(VigorCurrent)s, %(StrBase)s, %(StrCurrent)s, %(DexBase)s, %(DexCurrent)s, %(IntBase)s, %(IntCurrent)s, %(HealthBaseMax)s, %(HealthMax)s, %(HealthCurrent)s, %(ManaBaseMax)s, %(ManaMax)s, %(ManaCurrent)s)")
            data = {
                'UserID': userID,
                'CharacterName': name,
                'CharacterClass': characterClass,
                'CharacterLevel': 1,
                'VigorBase': self._vigor,
                'VigorCurrent': self._vigor,
                'StrBase': self._str,
                'StrCurrent': self._str,
                'DexBase': self._dex,
                'DexCurrent': self._dex,
                'IntBase': self._int,
                'IntCurrent': self._int,
                'HealthBaseMax': self._health,
                'HealthMax': self._health,
                'HealthCurrent': self._health,
                'ManaBaseMax': self._mana,
                'ManaMax': self._mana,
                'ManaCurrent': self._mana,
            }
            cursor.execute(query, data)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()

    # methods
    def viewCharacter(self):
        return (self._name + "\n" + self._charcterClass + " Level " + str(self._level))
        
    def getCharacter(self, userID, name):
        print("In getCharacter function")
        try:
            cnx = mysql.connector.connect(user='bot', password='203v2Xm&zXQK', host='45.31.16.49', database='disrpg')
            cursor = cnx.cursor()
            query = ("SELECT CharacterName, CharacterClass, CharacterLevel, VigorCurrent, StrCurrent, DexCurrent, IntCurrent, HealthMax, HealthCurrent, ManaMax, ManaCurrent FROM characters WHERE UserID=%s AND CharacterName=%s")
            cursor.execute(query, (userID, name))
            result = cursor.fetchone()
            if not result:
                return
            else:
                self._name = result[0]
                self._charcterClass = result[1]
                self._userID = userID
                self._level = result[2]
                self._vigor = result[3]
                self._str = result[4]
                self._dex = result[5]
                self._int = result[6]
                self._health = result[8]
                self._mana = result[10]
                self._maxHealth = result[7]
                self._maxMana = result[9]
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()

    def levelUp(self):
        self._level = self._level + 1