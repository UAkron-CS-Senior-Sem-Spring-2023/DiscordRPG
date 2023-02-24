import discord
import inspect
import classes
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
    await ctx.send(test1.viewCharacter())

#{message.author.display_name}

# if message.content.lower() == '/help':
#     commandList = f"""
#                   List of commands:
#                   /createCharacter - create your character
#                   /viewCharacter [name] - view selected character's stats and equiptment 
#                   /classList - view list of classes
#                   /classStats [className] - view stats of selected class
#                   """
#     await message.channel.send(inspect.cleandoc(commandList))

#     return

bot.run(TOKEN)
