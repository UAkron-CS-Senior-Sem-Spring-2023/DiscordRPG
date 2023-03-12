import discord
import inspect
import classes
import monsters
import os

from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv


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
    test1 = classes.Character(name, character_class)
    await ctx.response.send_message("Your character has been created")

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
    if(name == 'Cleric' or name == 'cleric'):
        charClass = classes.Cleric()
        await ctx.response.send_message(charClass.displayStats())
    elif(name == 'Hunter' or name == 'hunter'):
        charClass = classes.Hunter()
        await ctx.response.send_message(charClass.displayStats())
    elif(name == 'Mage' or name == 'mage'):
        charClass = classes.Mage()
        await ctx.response.send_message(charClass.displayStats())
    elif(name == 'Paladin' or name == 'paladin'):
        charClass = classes.Paladin()
        await ctx.response.send_message(charClass.displayStats())
    elif(name == 'Theif' or name == 'thief'):
        charClass = classes.Thief()
        await ctx.response.send_message(charClass.displayStats())
    elif(name == 'Warrior' or name == 'warrior'):
        charClass = classes.Warrior()
        await ctx.response.send_message(charClass.displayStats())
    else:
        await ctx.response.send_message('That is not one of the starting classes.')

# view stats and eqiptment of character with given name
# takes character's name as an argument
# returns the name, class, level, health, and mana of that character stored in the database
@tree.command(name='view_character', description="view selected character's stats and equiptment", guild=discord.Object(id=GUILD_ID))
async def view_character(ctx, name: str):
    test1 = classes.Character(name, "Warrior")
    await ctx.response.send_message(test1.viewCharacter())

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
@tree.command(name='monster_stats', description="view stats of selected monster of given level(default = 1)", guild=discord.Object(id=GUILD_ID))
async def monster_stats(ctx, name: str, level: int = 1):
    if(name == 'Boar' or name == 'Boar'):
        monster = monsters.Boar(level)
        await ctx.response.send_message(monster.displayStats())
    elif(name == 'Wolf' or name == 'wolf'):
        monster = monsters.Wolf(level)
        await ctx.response.send_message(monster.displayStats())
    elif(name == 'Treant' or name == 'mage'):
        monster = monsters.Treant(level)
        await ctx.response.send_message(monster.displayStats())
    elif(name == 'Elf' or name == 'Elf'):
        monster = monsters.Elf(level)
        await ctx.response.send_message(monster.displayStats())
    elif(name == 'Giant Spider' or name == 'Giant spider' or name == 'giant Spider' or name == 'giant spider'):
        monster = monsters.GiantSpider(level)
        await ctx.response.send_message(monster.displayStats())
    elif(name == 'Roper' or name == 'roper'):
        monster = monsters.Roper(level)
        await ctx.response.send_message(monster.displayStats())
    elif(name == 'Troll' or name == 'troll'):
        monster = monsters.Troll(level)
        await ctx.response.send_message(monster.displayStats())
    elif(name == 'Goblin' or name == 'goblin'):
        monster = monsters.Goblin(level)
        await ctx.response.send_message(monster.displayStats())
    else:
        await ctx.response.send_message('That is not currently a monster.')

client.run(TOKEN)
