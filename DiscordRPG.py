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

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('On an adventure!'))
    print("Bot is running")

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

@bot.command(name='monsterList', help="view a list of all monsters")
async def monsterList(ctx):
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
    await ctx.send(inspect.cleandoc(response))

@bot.command(name='monsterStats', help="view stats of selected monster of given level(default = 1)")
async def classStats(ctx, name, level = 1):
    if(name == 'Boar' or name == 'Boar'):
        monster = monsters.Boar(level)
        await ctx.send(monster.displayStats())
    elif(name == 'Wolf' or name == 'wolf'):
        monster = monsters.Wolf(level)
        await ctx.send(monster.displayStats())
    elif(name == 'Treant' or name == 'mage'):
        monster = monsters.Treant(level)
        await ctx.send(monster.displayStats())
    elif(name == 'Elf' or name == 'Elf'):
        monster = monsters.Elf(level)
        await ctx.send(monster.displayStats())
    elif(name == 'Giant Spider' or name == 'Giant spider' or name == 'giant Spider' or name == 'giant spider'):
        monster = monsters.GiantSpider(level)
        await ctx.send(monster.displayStats())
    elif(name == 'Roper' or name == 'roper'):
        monster = monsters.Roper(level)
        await ctx.send(monster.displayStats())
    elif(name == 'Troll' or name == 'troll'):
        monster = monsters.Troll(level)
        await ctx.send(monster.displayStats())
    elif(name == 'Goblin' or name == 'goblin'):
        monster = monsters.Goblin(level)
        await ctx.send(monster.displayStats())
    else:
        await ctx.send('That is not currently a monster.')

# {message.author.display_name}

# '/help':
#  List of commands:
#  /createCharacter - create your character
#  /viewCharacter [name] - view selected character's stats and equiptment 
#  /classList - view list of classes
#  /classStats [className] - view stats of selected class

bot.run(TOKEN)
