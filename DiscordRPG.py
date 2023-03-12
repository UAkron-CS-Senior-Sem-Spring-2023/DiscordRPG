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

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(command_prefix='/',intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1077380188767256647))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('On an adventure!'))
    print("Bot is running")

@tree.command(name='create_character', description='create your character', guild=discord.Object(id=1077380188767256647))
async def create_character(ctx, name: str, character_class: str):
    test1 = classes.Character(name, character_class)
    await ctx.send("Your character has been created")

@tree.command(name='class_list', description='view the list of starting classes', guild=discord.Object(id=1077380188767256647))
async def class_list(ctx):
    response = f"""
                Cleric
                Hunter
                Mage
                Paladin
                Theif
                Warrior
                """
    await ctx.send(inspect.cleandoc(response))
    
@tree.command(name='class_stats', description="view stats of selected class", guild=discord.Object(id=1077380188767256647))
async def class_stats(ctx, name: str):
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

@tree.command(name='view_character', description="view selected character's stats and equiptment", guild=discord.Object(id=1077380188767256647))
async def view_character(ctx, name: str):
    test1 = classes.Character(name, "Warrior")
    await ctx.send(test1.viewCharacter())

@tree.command(name='monster_list', description="view a list of all monsters", guild=discord.Object(id=1077380188767256647))
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
    await ctx.send(inspect.cleandoc(response))

@tree.command(name='monster_stats', description="view stats of selected monster of given level(default = 1)", guild=discord.Object(id=1077380188767256647))
async def monster_stats(ctx, name: str, level: int = 1):
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

client.run(TOKEN)
