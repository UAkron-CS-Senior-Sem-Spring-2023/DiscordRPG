import discord
import inspect
import classes
import monsters
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv() 
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='/',intents=intents)

@bot.command(name='createCharacter', help='create your character')
async def createCharacter(ctx, name: str, characterClass: str):
    test1 = classes.Character(name, characterClass)
    await ctx.send("Your character has been created")

@bot.command(name='classList', help='view the list of starting classes')
async def classList(ctx):
    response = f"""
                Cleric
                Hunter
                Mage
                Paladin
                Theif
                Warrior
                """
    await ctx.send(inspect.cleandoc(response))
    
@bot.command(name='classStats', help="view stats of selected class")
async def classStats(ctx, name):
    if(name == 'Cleric' or name == 'cleric'):
        charClass = classes.Cleric()
        await ctx.send(charClass.displayStats())
    elif(name == 'Hunter' or name == 'hunter'):
        charClass = classes.Hunter()
        await ctx.send(charClass.displayStats())
    elif(name == 'Mage' or name == 'mage'):
        charClass = classes.Mage()
        await ctx.send(charClass.displayStats())
    elif(name == 'Paladin' or name == 'paladin'):
        charClass = classes.Paladin()
        await ctx.send(charClass.displayStats())
    elif(name == 'Theif' or name == 'thief'):
        charClass = classes.Thief()
        await ctx.send(charClass.displayStats())
    elif(name == 'Warrior' or name == 'warrior'):
        charClass = classes.Warrior()
        await ctx.send(charClass.displayStats())
    else:
        await ctx.send('That is not one of the starting classes.')

@bot.command(name='viewCharacter', help="view selected character's stats and equiptment")
async def viewCharacter(ctx, name):
    test1 = classes.Character(name, "Warrior")
    await ctx.send(test1.viewCharacter())

# @bot.command(name='monsterList', help="view a list of all monsters")
# async def viewCharacter(ctx, name):
#     test1 = classes.Character(name, "Warrior")
#     await ctx.send(test1.viewCharacter())

# {message.author.display_name}

# '/help':
#  List of commands:
#  /createCharacter - create your character
#  /viewCharacter [name] - view selected character's stats and equiptment 
#  /classList - view list of classes
#  /classStats [className] - view stats of selected class

bot.run(TOKEN)
