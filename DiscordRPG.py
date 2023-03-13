import discord
import mysql.connector
from mysql.connector import errorcode
import inspect
import classes
import character
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





@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('On an adventure!'))
    print("Bot is running")

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

@tree.command(name='monster_stats', description="view stats of selected monster of given level(default = 1)", guild=discord.Object(id=GUILD_ID))
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

@tree.command(name='adventure', description='Start an adventure', guild=discord.Object(id=GUILD_ID))
async def adventure(ctx, name: str, location: str):
    match location.lower():
        case "forest":
            pass
        case "cave":
            pass

client.run(TOKEN)