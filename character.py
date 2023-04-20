import mysql.connector
from mysql.connector import errorcode
import monsters

class Character:
    # constructor
    def __init__(self, name, characterClass, userID):
        self._name = name
        self._characterClass = characterClass.lower()
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
        self._xp = 0
        self._gold = 0
        self._healthPotions = 0
        self._manaPotions = 0
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
            #case _:
                #print("Invalid class name. Please choose one of the classes")
        

    # methods
    def viewCharacter(self):
        return (self._name + "\n" + self._characterClass + " Level " + str(self._level))
    
    # Adds or updates the character from object to the database
    def addCharacter(self):
        try:
            cnx = mysql.connector.connect(user='bot', password='203v2Xm&zXQK', host='45.31.16.49', database='disrpg')
            cursor = cnx.cursor()
            query = ("INSERT INTO characters (UserID, CharacterName, CharacterClass, CharacterLevel, VigorBase, VigorCurrent, StrBase, StrCurrent, DexBase, DexCurrent, IntBase, IntCurrent, HealthBaseMax, HealthMax, HealthCurrent, ManaBaseMax, ManaMax, ManaCurrent, Xp, Gold, HealthPotions, ManaPotions) VALUES (%(UserID)s, %(CharacterName)s, %(CharacterClass)s, %(CharacterLevel)s, %(VigorBase)s, %(VigorCurrent)s, %(StrBase)s, %(StrCurrent)s, %(DexBase)s, %(DexCurrent)s, %(IntBase)s, %(IntCurrent)s, %(HealthBaseMax)s, %(HealthMax)s, %(HealthCurrent)s, %(ManaBaseMax)s, %(ManaMax)s, %(ManaCurrent)s, %(Xp)s, %(Gold)s, %(HealthPotions)s, %(ManaPotions)s)")
            data = {
                'UserID': self._userID,
                'CharacterName': self._name,
                'CharacterClass': self._characterClass,
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
                'Xp' : self._xp,
                'Gold' : self._gold,
                'HealthPotions' : self._healthPotions,
                'ManaPotions' : self._manaPotions
            }
            cursor.execute(query, data)
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return False
        else:
            cnx.close()
            return False
        
    #gets a character with a certain name and user from the database and puts values into object returns true if character found and false if it isn't
    def getCharacter(self, userID, name):
        try:
            cnx = mysql.connector.connect(user='bot', password='203v2Xm&zXQK', host='45.31.16.49', database='disrpg')
            cursor = cnx.cursor()
            query = ("SELECT CharacterName, CharacterClass, CharacterLevel, VigorCurrent, StrCurrent, DexCurrent, IntCurrent, HealthMax, HealthCurrent, ManaMax, ManaCurrent, Xp, Gold, HealthPotions, ManaPotions FROM characters WHERE UserID=%s AND CharacterName=%s")
            cursor.execute(query, (userID, name))
            result = cursor.fetchone()
            if not result:
                return False
            else:
                self._name = result[0]
                self._characterClass = result[1]
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
                self._xp = result[11]
                self._gold = result[12]
                self._healthPotions = result[13]
                self._manaPotions = result[14]
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return False
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return False
            else:
                print(err)
                return False
        else:
            cnx.close()
            return False
            
    def levelUp(self):
        self._level = self._level + 1
        
    #updates a character in the database from object
    def updateCharacter(self):
        try:
            cnx = mysql.connector.connect(user='bot', password='203v2Xm&zXQK', host='45.31.16.49', database='disrpg')
            cursor = cnx.cursor()
            query = ("REPLACE INTO characters (UserID, CharacterName, CharacterClass, CharacterLevel, VigorBase, VigorCurrent, StrBase, StrCurrent, DexBase, DexCurrent, IntBase, IntCurrent, HealthBaseMax, HealthMax, HealthCurrent, ManaBaseMax, ManaMax, ManaCurrent, Xp, Gold, HealthPotions, ManaPotions) VALUES (%(UserID)s, %(CharacterName)s, %(CharacterClass)s, %(CharacterLevel)s, %(VigorBase)s, %(VigorCurrent)s, %(StrBase)s, %(StrCurrent)s, %(DexBase)s, %(DexCurrent)s, %(IntBase)s, %(IntCurrent)s, %(HealthBaseMax)s, %(HealthMax)s, %(HealthCurrent)s, %(ManaBaseMax)s, %(ManaMax)s, %(ManaCurrent)s, %(Xp)s, %(Gold)s, %(HealthPotions)s, %(ManaPotions)s)")
            data = {
                'UserID': self._userID,
                'CharacterName': self._name,
                'CharacterClass': self._characterClass,
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
                'HealthMax': self._maxHealth,
                'HealthCurrent': self._health,
                'ManaBaseMax': self._mana,
                'ManaMax': self._maxMana,
                'ManaCurrent': self._mana,
                'Xp' : self._xp,
                'Gold' : self._gold,
                'HealthPotions' : self._healthPotions,
                'ManaPotions' : self._manaPotions
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
            
    def deleteCharacter(self):
        try:
            cnx = mysql.connector.connect(user='bot', password='203v2Xm&zXQK', host='45.31.16.49', database='disrpg')
            cursor = cnx.cursor()
            query = ("DELETE FROM characters WHERE UserID=%s AND CharacterName=%s")
            cursor.execute(query, (self._userID, self._name))
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
