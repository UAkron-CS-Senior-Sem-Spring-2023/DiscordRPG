import discord
import mysql.connector
from mysql.connector import errorcode
import inspect
import classes
import character
import monsters
import os
import random
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

random.seed()
load_dotenv() 
TOKEN = os.getenv("TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(command_prefix='/',intents=intents)
tree = app_commands.CommandTree(client)

# the ready event for the bot
# syncs the commands with the discord Slash Commands
# sets the bots status and game
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('On an adventure!'))
    print("Bot is running")

# create a character
# takes a name and class name as arguments
# stores the character in the database 
@tree.command(name='create_character', description='create your character', guild=discord.Object(id=GUILD_ID))
async def create_character(ctx, name: str, character_class: str):
    match character_class.lower():
        case "cleric":
            test1 = character.Character(name, character_class, ctx.user.id)
            await ctx.response.send_message("Your character has been created")
        case "hunter":
            test1 = character.Character(name, character_class, ctx.user.id)
            await ctx.response.send_message("Your character has been created")
        case "mage":
            test1 = character.Character(name, character_class, ctx.user.id)
            await ctx.response.send_message("Your character has been created")
        case "paladin":
            test1 = character.Character(name, character_class, ctx.user.id)
            await ctx.response.send_message("Your character has been created")
        case "theif":
            test1 = character.Character(name, character_class, ctx.user.id)
            await ctx.response.send_message("Your character has been created")
        case "warrior":
            test1 = character.Character(name, character_class, ctx.user.id)
            await ctx.response.send_message("Your character has been created")
        case _:
            await ctx.response.send_message("Invalid class name. Please choose one of the classes")

# see the list of all starting classes
# returns a response with all classes as a list
@tree.command(name='class_list', description='view the list of starting classes', guild=discord.Object(id=GUILD_ID))
async def class_list(ctx):
    response = f"""
                Cleric
                Hunter
                Mage
                Paladin
                Theif
                Warrior
                """
    await ctx.response.send_message(inspect.cleandoc(response))

# view the stats of a starting class
# takes the class name as an arguments
# returns the class and stat values to the user
@tree.command(name='class_stats', description="view stats of selected class", guild=discord.Object(id=GUILD_ID))
async def class_stats(ctx, name: str):
    match name.lower():
        case "cleric":
            charClass = classes.Cleric()
            await ctx.response.send_message(charClass.displayStats())
        case "hunter":
            charClass = classes.Hunter()
            await ctx.response.send_message(charClass.displayStats())
        case "mage":
            charClass = classes.Mage()
            await ctx.response.send_message(charClass.displayStats())
        case "paladin":
            charClass = classes.Paladin()
            await ctx.response.send_message(charClass.displayStats())
        case "thief":
            charClass = classes.Thief()
            await ctx.response.send_message(charClass.displayStats())
        case "warrior":
            charClass = classes.Warrior()
            await ctx.response.send_message(charClass.displayStats())
        case _:
            await ctx.response.send_message('That is not one of the starting classes.')

# view stats and eqiptment of character with given name
# takes character's name as an argument
# returns the name, class, level, health, and mana of that character stored in the database
@tree.command(name='view_character', description="view selected character's stats and equiptment", guild=discord.Object(id=GUILD_ID))
async def view_character(ctx, name: str):
    try:
        cnx = mysql.connector.connect(user='bot', password='203v2Xm&zXQK', host='45.31.16.49', database='disrpg')
        cursor = cnx.cursor()
        query = ("SELECT CharacterName, CharacterClass, CharacterLevel, HealthCurrent, HealthMax, ManaCurrent, ManaMax FROM characters WHERE UserID=%s AND CharacterName=%s")
        cursor.execute(query, (ctx.user.id, name))
        result = cursor.fetchone()
        if not result:
            await ctx.response.send_message("The selected character does not exist for this user")
        else:
            output = "Character Name: {} Character Class: {} Character Level: {}  Character Health {}/{} Character Mana {}/{}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
            await ctx.response.send_message(output)
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

# view all the monsters based on location
# returns all monster names in list form
@tree.command(name='monster_list', description="view a list of all monsters", guild=discord.Object(id=GUILD_ID))
async def monster_list(ctx):
    response = f"""
                Forest:
                Boar
                Wolf
                Treant
                Elf

                Cave: 
                Giant Spider
                Roper
                Troll
                Goblin
                """
    await ctx.response.send_message(inspect.cleandoc(response))

# view the stats of selected monster
# takes the monster's name and level as arguments
# returns the stats of the chosen monster with selected level (default of 1)
@tree.command(name='monster_stats', description="view stats of selected monster of given level (default = 1)", guild=discord.Object(id=GUILD_ID))
async def monster_stats(ctx, name: str, level: int = 1):
    match name.lower():
        case "boar":
            monster = monsters.Boar(level)
            await ctx.response.send_message(monster.displayStats())
        case "wolf":
            monster = monsters.Wolf(level)
            await ctx.response.send_message(monster.displayStats())
        case "treant":
            monster = monsters.Treant(level)
            await ctx.response.send_message(monster.displayStats())
        case "elf":
            monster = monsters.Elf(level)
            await ctx.response.send_message(monster.displayStats())
        case "giant spider":
            monster = monsters.GiantSpider(level)
            await ctx.response.send_message(monster.displayStats())
        case "roper":
            monster = monsters.Roper(level)
            await ctx.response.send_message(monster.displayStats())
        case "troll":
            monster = monsters.Troll(level)
            await ctx.response.send_message(monster.displayStats())
        case "goblin":
            monster = monsters.Goblin(level)
            await ctx.response.send_message(monster.displayStats())
        case _:
            await ctx.response.send_message('This is not one of the current monsters.')

# runs the battles against a monster (demo version)
# takes character name and location as arguments
# returns outcome of battle
@tree.command(name='adventure', description='Start an adventure', guild=discord.Object(id=GUILD_ID))
async def adventure(ctx, name: str, location: str):
    match location.lower():
        case "forest":
            chance = random.randint(1, 100)
            if(chance < 36):
                player_health = 24
                player_str = 8
                monster_name = "Boar"
                monster_health = 24
                monster_str = 5
                encounter = "You have encountered a " + monster_name + "\n" + name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                while(monster_health > 0 and player_health > 0):
                    player_damage = random.randint(1, player_str)
                    monster_damage = random.randint(1, monster_str)
                    damage = "You did " + str(player_damage) + " damage the " + monster_name + " did " + str(monster_damage) + " damage"
                    player_health = player_health - monster_damage
                    monster_health = monster_health - player_damage
                    health = name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                    encounter = encounter + "\n\n" + damage + "\n" + health
                if(monster_health <= 0):
                    encounter = encounter + "\n\nYou have defeated the " + monster_name + "!"
                    await ctx.response.send_message(encounter)
                else:
                    encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                    await ctx.response.send_message(encounter)

            elif(chance < 71):
                player_health = 24
                player_str = 8
                monster_name = "Wolf"
                monster_health = 20
                monster_str = 5
                encounter = "You have encountered a " + monster_name + "\n" + name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                while(monster_health > 0 and player_health > 0):
                    player_damage = random.randint(1, player_str)
                    monster_damage = random.randint(1, monster_str)
                    damage = "You did " + str(player_damage) + " damage the " + monster_name + " did " + str(monster_damage) + " damage"
                    player_health = player_health - monster_damage
                    monster_health = monster_health - player_damage
                    health = name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                    encounter = encounter + "\n\n" + damage + "\n" + health
                if(monster_health <= 0):
                    encounter = encounter + "\n\nYou have defeated the " + monster_name + "!"
                    await ctx.response.send_message(encounter)
                else:
                    encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                    await ctx.response.send_message(encounter)

            elif(chance < 91):
                player_health = 24
                player_str = 8
                monster_name = "Elf"
                monster_health = 20
                monster_str = 6
                encounter = "You have encountered a " + monster_name + "\n" + name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                while(monster_health > 0 and player_health > 0):
                    player_damage = random.randint(1, player_str)
                    monster_damage = random.randint(1, monster_str)
                    damage = "You did " + str(player_damage) + " damage the " + monster_name + " did " + str(monster_damage) + " damage"
                    player_health = player_health - monster_damage
                    monster_health = monster_health - player_damage
                    health = name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                    encounter = encounter + "\n\n" + damage + "\n" + health
                if(monster_health <= 0):
                    encounter = encounter + "\n\nYou have defeated the " + monster_name + "!"
                    await ctx.response.send_message(encounter)
                else:
                    encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                    await ctx.response.send_message(encounter)

            else:
                player_health = 24
                player_str = 8
                monster_name = "Treant"
                monster_health = 48
                monster_str = 7
                encounter = "You have encountered a " + monster_name + "\n" + name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                while(monster_health > 0 and player_health > 0):
                    player_damage = random.randint(1, player_str)
                    monster_damage = random.randint(1, monster_str)
                    damage = "You did " + str(player_damage) + " damage the " + monster_name + " did " + str(monster_damage) + " damage"
                    player_health = player_health - monster_damage
                    monster_health = monster_health - player_damage
                    health = name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                    encounter = encounter + "\n\n" + damage + "\n" + health
                if(monster_health <= 0):
                    encounter = encounter + "\n\nYou have defeated the " + monster_name + "!"
                    await ctx.response.send_message(encounter)
                else:
                    encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                    await ctx.response.send_message(encounter)

        case "cave":
            chance = random.randint(1, 100)
            if(chance < 36):
                player_health = 24
                player_str = 8
                monster_name = "Giant Spider"
                monster_health = 20
                monster_str = 6
                encounter = "You have encountered a " + monster_name + "\n" + name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                while(monster_health > 0 and player_health > 0):
                    player_damage = random.randint(1, player_str)
                    monster_damage = random.randint(1, monster_str)
                    damage = "You did " + str(player_damage) + " damage the " + monster_name + " did " + str(monster_damage) + " damage"
                    player_health = player_health - monster_damage
                    monster_health = monster_health - player_damage
                    health = name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                    encounter = encounter + "\n\n" + damage + "\n" + health
                if(monster_health <= 0):
                    encounter = encounter + "\n\nYou have defeated the " + monster_name + "!"
                    await ctx.response.send_message(encounter)
                else:
                    encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                    await ctx.response.send_message(encounter)

            elif(chance < 71):
                player_health = 24
                player_str = 8
                monster_name = "Roper"
                monster_health = 20
                monster_str = 4
                encounter = "You have encountered a " + monster_name + "\n" + name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                while(monster_health > 0 and player_health > 0):
                    player_damage = random.randint(1, player_str)
                    monster_damage = random.randint(1, monster_str)
                    damage = "You did " + str(player_damage) + " damage the " + monster_name + " did " + str(monster_damage) + " damage"
                    player_health = player_health - monster_damage
                    monster_health = monster_health - player_damage
                    health = name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                    encounter = encounter + "\n\n" + damage + "\n" + health
                if(monster_health <= 0):
                    encounter = encounter + "\n\nYou have defeated the " + monster_name + "!"
                    await ctx.response.send_message(encounter)
                else:
                    encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                    await ctx.response.send_message(encounter)

            elif(chance < 91):
                player_health = 24
                player_str = 8
                monster_name = "Goblin"
                monster_health = 24
                monster_str = 7
                encounter = "You have encountered a " + monster_name + "\n" + name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                while(monster_health > 0 and player_health > 0):
                    player_damage = random.randint(1, player_str)
                    monster_damage = random.randint(1, monster_str)
                    damage = "You did " + str(player_damage) + " damage the " + monster_name + " did " + str(monster_damage) + " damage"
                    player_health = player_health - monster_damage
                    monster_health = monster_health - player_damage
                    health = name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                    encounter = encounter + "\n\n" + damage + "\n" + health
                if(monster_health <= 0):
                    encounter = encounter + "\n\nYou have defeated the " + monster_name + "!"
                    await ctx.response.send_message(encounter)
                else:
                    encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                    await ctx.response.send_message(encounter)

            else:
                player_health = 24
                player_str = 8
                monster_name = "Troll"
                monster_health = 48
                monster_str = 8
                encounter = "You have encountered a " + monster_name + "\n" + name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                while(monster_health > 0 and player_health > 0):
                    player_damage = random.randint(1, player_str)
                    monster_damage = random.randint(1, monster_str)
                    damage = "You did " + str(player_damage) + " damage the " + monster_name + " did " + str(monster_damage) + " damage"
                    player_health = player_health - monster_damage
                    monster_health = monster_health - player_damage
                    health = name + " Health: " + str(player_health) + "  " + monster_name + " Health: " + str(monster_health)
                    encounter = encounter + "\n\n" + damage + "\n" + health
                if(monster_health <= 0):
                    encounter = encounter + "\n\nYou have defeated the " + monster_name + "!"
                    await ctx.response.send_message(encounter)
                else:
                    encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                    await ctx.response.send_message(encounter)

client.run(TOKEN)