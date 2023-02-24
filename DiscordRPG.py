import discord
import inspect
import class

import os
from dotenv import load_dotenv

load_dotenv() 

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():

    print('We have successfully loggged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:

        return

#    if message.content.lower() == 'hello':
#        await message.channel.send(f'Hello, {message.author.display_name}!')

#        return

    if message.content.lower() == '/help':
        commandList = f"""
                      List of commands:
                      /createCharacter - create your character
                      /viewCharacter [name] - view selected character's stats and equiptment 
                      /classList - view list of classes
                      /classStats [className] - view stats of selected class
                      """
        await message.channel.send(inspect.cleandoc(commandList))

        return

client.run(TOKEN)
