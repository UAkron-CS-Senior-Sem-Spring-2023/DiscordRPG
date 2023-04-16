import discord
import mysql.connector
import classes
import character
import monsters
import os
import random

from mysql.connector import errorcode
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
            if test1.addCharacter():
                await ctx.response.send_message("Your character has been created")
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists")
        case "hunter":
            test1 = character.Character(name, character_class, ctx.user.id)
            if test1.addCharacter():
                await ctx.response.send_message("Your character has been created")
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists")
        case "mage":
            test1 = character.Character(name, character_class, ctx.user.id)
            if test1.addCharacter():
                await ctx.response.send_message("Your character has been created")
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists")
        case "paladin":
            test1 = character.Character(name, character_class, ctx.user.id)
            if test1.addCharacter():
                await ctx.response.send_message("Your character has been created")
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists")
        case "theif":
            test1 = character.Character(name, character_class, ctx.user.id)
            if test1.addCharacter():
                await ctx.response.send_message("Your character has been created")
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists")
        case "warrior":
            test1 = character.Character(name, character_class, ctx.user.id)
            if test1.addCharacter():
                await ctx.response.send_message("Your character has been created")
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists")
        case _:
            await ctx.response.send_message("Invalid class name. Please choose one of the classes")

# see the list of all starting classes
# returns a response with all classes as a list
@tree.command(name='class_list', description='view the list of starting classes', guild=discord.Object(id=GUILD_ID))
async def class_list(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.user

    # view for class_list
    cleric_button = discord.ui.Button(label = "Cleric", custom_id = 'cleric', style = discord.ButtonStyle.gray, row = 0)
    hunter_button = discord.ui.Button(label = "Hunter", custom_id = 'hunter', style = discord.ButtonStyle.gray, row = 0)
    mage_button = discord.ui.Button(label = "Mage", custom_id = 'mage', style = discord.ButtonStyle.gray, row = 0)
    paladin_button = discord.ui.Button(label = "Paladin", custom_id = 'paladin', style = discord.ButtonStyle.gray, row = 1)
    thief_button = discord.ui.Button(label = "Theif", custom_id = 'theif', style = discord.ButtonStyle.gray, row = 1)
    warrior_button = discord.ui.Button(label = "Warrior", custom_id = 'warrior', style = discord.ButtonStyle.gray, row = 1)
    view = discord.ui.View()
    view.add_item(cleric_button)
    view.add_item(hunter_button)
    view.add_item(mage_button)
    view.add_item(paladin_button)
    view.add_item(thief_button)
    view.add_item(warrior_button)
    
    # button callbacks
    async def cleric_callback(interaction):
        charClass = classes.Cleric()
        button_embed = discord.Embed(title = "Cleric", description = "Starting stats for a cleric", color = discord.Color.from_rgb(255, 255, 255))
        button_embed.add_field(name = charClass.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    async def hunter_callback(interaction):
        charClass = classes.Hunter()
        button_embed = discord.Embed(title = "Hunter", description = "Starting stats for a hunter", color = discord.Color.from_rgb(0, 51, 0))
        button_embed.add_field(name = charClass.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)
    
    async def mage_callback(interaction):
        charClass = classes.Mage()
        button_embed = discord.Embed(title = "Mage", description = "Starting stats for a mage", color = discord.Color.from_rgb(0, 0, 153))
        button_embed.add_field(name = charClass.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    async def paladin_callback(interaction):
        charClass = classes.Paladin()
        button_embed = discord.Embed(title = "Paladin", description = "Starting stats for a paladin", color = discord.Color.from_rgb(153, 0, 0))
        button_embed.add_field(name = charClass.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    async def thief_callback(interaction):
        charClass = classes.Thief()
        button_embed = discord.Embed(title = "Thief", description = "Starting stats for a thief", color = discord.Color.from_rgb(0, 0, 0))
        button_embed.add_field(name = charClass.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    async def warrior_callback(interaction):
        charClass = classes.Warrior()
        button_embed = discord.Embed(title = "Warrior", description = "Starting stats for a warrior", color = discord.Color.from_rgb(64, 64, 64))
        button_embed.add_field(name = charClass.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    cleric_button.callback = cleric_callback
    hunter_button.callback = hunter_callback
    mage_button.callback = mage_callback
    paladin_button.callback = paladin_callback
    thief_button.callback = thief_callback
    warrior_button.callback = warrior_callback

    # embed for class_list
    embed = discord.Embed(title = "Class List", description = "List of starting classes\nPress a button to view starting stats", color = discord.Color.from_rgb(255, 255, 0))
    embed.set_footer(text = f"{member.display_name} created this list")

    await ctx.response.send_message(embed = embed, view = view)

# view stats and eqiptment of character with given name
# takes character's name as an argument
# returns the name, class, level, health, and mana of that character stored in the database
@tree.command(name='view_character', description="view selected character's stats and equiptment", guild=discord.Object(id=GUILD_ID))
async def view_character(ctx, name: str):
    test = character.Character(name, "", ctx.user.id)
    if test.getCharacter(ctx.user.id, name):
        output = "Name: {} \nClass: {} Level: {}  \nHealth {}/{} Mana {}/{}".format(test._name, test._characterClass, test._level, test._health, test._maxHealth, test._mana, test._maxMana)
    else:
        output = "Could not a find character with that name assigned to you"
    await ctx.response.send_message(output)

# view all the monsters based on location
# returns all monster names in list form
@tree.command(name='monster_list', description="view a list of all monsters", guild=discord.Object(id=GUILD_ID))
async def monster_list(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.user
    
    # view for monster_list
    boar_button = discord.ui.Button(label = "Boar", custom_id = 'boar', style = discord.ButtonStyle.green, row = 0)
    wolf_button = discord.ui.Button(label = "Wolf", custom_id = 'wolf', style = discord.ButtonStyle.green, row = 0)
    elf_button = discord.ui.Button(label = "Elf", custom_id = 'elf', style = discord.ButtonStyle.green, row = 0)
    treant_button = discord.ui.Button(label = "Treant", custom_id = 'treant', style = discord.ButtonStyle.green, row = 0)
    spider_button = discord.ui.Button(label = "Giant Spider", custom_id = 'spider', style = discord.ButtonStyle.gray, row = 1)
    roper_button = discord.ui.Button(label = "Roper", custom_id = 'roper', style = discord.ButtonStyle.gray, row = 1)
    goblin_button = discord.ui.Button(label = "Goblin", custom_id = 'goblin', style = discord.ButtonStyle.gray, row = 1)
    troll_button = discord.ui.Button(label = "Troll", custom_id = 'troll', style = discord.ButtonStyle.gray, row = 1)
    view = discord.ui.View()
    view.add_item(boar_button)
    view.add_item(wolf_button)
    view.add_item(elf_button)
    view.add_item(treant_button)
    view.add_item(spider_button)
    view.add_item(roper_button)
    view.add_item(goblin_button)
    view.add_item(troll_button)

    # button callbacks
    async def boar_callback(interaction):
        level = 1
        monster = monsters.Boar(level)
        button_embed = discord.Embed(title = "Boar", description = "Stats for a level " + str(level) + " boar", color = discord.Color.from_rgb(51, 25, 0))
        button_embed.add_field(name = monster.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    async def wolf_callback(interaction):
        level = 1
        monster = monsters.Wolf(level)
        button_embed = discord.Embed(title = "Wolf", description = "Stats for a level " + str(level) + " wolf", color = discord.Color.from_rgb(64, 64, 64))
        button_embed.add_field(name = monster.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    async def elf_callback(interaction):
        level = 1
        monster = monsters.Elf(level)
        button_embed = discord.Embed(title = "Elf", description = "Stats for a level " + str(level) + " elf", color = discord.Color.from_rgb(0, 102, 0))
        button_embed.add_field(name = monster.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    async def treant_callback(interaction):
        level = 1
        monster = monsters.Treant(level)
        button_embed = discord.Embed(title = "Treant", description = "Stats for a level " + str(level) + " treant", color = discord.Color.from_rgb(102, 51, 0))
        button_embed.add_field(name = monster.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    async def spider_callback(interaction):
        level = 1
        monster = monsters.GiantSpider(level)
        button_embed = discord.Embed(title = "Giant Spider", description = "Stats for a level " + str(level) + " giant spider", color = discord.Color.from_rgb(32, 32, 32))
        button_embed.add_field(name = monster.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    async def roper_callback(interaction):
        level = 1
        monster = monsters.Roper(level)
        button_embed = discord.Embed(title = "Roper", description = "Stats for a level " + str(level) + " roper", color = discord.Color.from_rgb(51, 0, 51))
        button_embed.add_field(name = monster.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    async def goblin_callback(interaction):
        level = 1
        monster = monsters.Goblin(level)
        button_embed = discord.Embed(title = "Goblin", description = "Stats for a level " + str(level) + " goblin", color = discord.Color.from_rgb(7, 50, 27))
        button_embed.add_field(name = monster.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    async def troll_callback(interaction):
        level = 1
        monster = monsters.Troll(level)
        button_embed = discord.Embed(title = "Troll", description = "Stats for a level " + str(level) + " troll", color = discord.Color.from_rgb(39, 58, 43))
        button_embed.add_field(name = monster.displayStats(), value = "")
        await interaction.response.send_message(embed = button_embed)

    boar_button.callback = boar_callback
    wolf_button.callback = wolf_callback
    elf_button.callback = elf_callback
    treant_button.callback = treant_callback
    spider_button.callback = spider_callback
    roper_button.callback = roper_callback
    goblin_button.callback = goblin_callback
    troll_button.callback = troll_callback

    # embed for monster_list
    embed = discord.Embed(title = "Monster List", description = "List of all current monsters\nSelect a button to view starting stats for the monster", color = discord.Color.from_rgb(51, 0, 102))
    embed.add_field(name = "Locations:", value = "", inline = False)
    embed.add_field(name = "Forest", value = "", inline = False)
    embed.add_field(name = "Cave", value = "", inline = False)
    embed.set_footer(text = f"{member.display_name} created this list")

    await ctx.response.send_message(embed = embed, view = view)

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

@tree.command(name='adventure2', description='Start an adventure', guild=discord.Object(id=GUILD_ID))
async def adventure2(ctx, name: str, member: discord.Member = None):
    if member == None:
        member = ctx.user
    
    player = character.Character(name, "", ctx.user.id)
    player.getCharacter(ctx.user.id, name)

    # view for adventure
    forest_button = discord.ui.Button(label = "Forest", custom_id = 'forest', style = discord.ButtonStyle.green, row = 0)
    cave_button = discord.ui.Button(label = "Cave", custom_id = 'cave', style = discord.ButtonStyle.gray, row = 0)
    view = discord.ui.View()
    view.add_item(forest_button)
    view.add_item(cave_button)

    # button callbacks
    async def forest_callback(interaction):
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
                await interaction.response.send_message(encounter)
            else:
                encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                await interaction.response.send_message(encounter)

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
                await interaction.response.send_message(encounter)
            else:
                encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                await interaction.response.send_message(encounter)

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
                await interaction.response.send_message(encounter)
            else:
                encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                await interaction.response.send_message(encounter)

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
                await interaction.response.send_message(encounter)
            else:
                encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                await interaction.response.send_message(encounter)

    async def cave_callback(interaction):
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
                await interaction.response.send_message(encounter)
            else:
                encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                await interaction.response.send_message(encounter)

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
                await interaction.response.send_message(encounter)
            else:
                encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                await interaction.response.send_message(encounter)

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
                await interaction.response.send_message(encounter)
            else:
                encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                await interaction.response.send_message(encounter)

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
                await interaction.response.send_message(encounter)
            else:
                encounter = encounter + "\n\nYou were defeated by the " + monster_name + "!"
                await interaction.response.send_message(encounter)

    forest_button.callback = forest_callback
    cave_button.callback = cave_callback

    # embed for adventure
    embed = discord.Embed(title = "Adventure", description = "Select the location you would like to adventure to\n", color = discord.Color.from_rgb(204, 102, 0))
    embed.set_footer(text = f"{member.display_name} created this list")

    await ctx.response.send_message(embed = embed, view = view)

client.run(TOKEN)
