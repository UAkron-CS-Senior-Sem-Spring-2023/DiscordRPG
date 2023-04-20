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
                await ctx.response.send_message("Your character has been created", ephemeral = True)
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists", ephemeral = True)
        case "hunter":
            test1 = character.Character(name, character_class, ctx.user.id)
            if test1.addCharacter():
                await ctx.response.send_message("Your character has been created", ephemeral = True)
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists", ephemeral = True)
        case "mage":
            test1 = character.Character(name, character_class, ctx.user.id)
            if test1.addCharacter():
                await ctx.response.send_message("Your character has been created", ephemeral = True)
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists", ephemeral = True)
        case "paladin":
            test1 = character.Character(name, character_class, ctx.user.id)
            if test1.addCharacter():
                await ctx.response.send_message("Your character has been created", ephemeral = True)
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists", ephemeral = True)
        case "theif":
            test1 = character.Character(name, character_class, ctx.user.id)
            if test1.addCharacter():
                await ctx.response.send_message("Your character has been created", ephemeral = True)
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists", ephemeral = True)
        case "warrior":
            test1 = character.Character(name, character_class, ctx.user.id)
            if test1.addCharacter():
                await ctx.response.send_message("Your character has been created", ephemeral = True)
            else:
                await ctx.response.send_message("Character could not be added, either database error or name already exists", ephemeral = True)
        case _:
            await ctx.response.send_message("Invalid class name. Please choose one of the classes", ephemeral = True)

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
async def monster_list(ctx, level: int = 1,):
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

    # return view
    return_button = discord.ui.Button(label = "Return", custom_id = 'return', style = discord.ButtonStyle.red)
    return_view = discord.ui.View()
    return_view.add_item(return_button)

    # button callbacks
    async def boar_callback(interaction):
        if(interaction.user == member):
            monster = monsters.Boar(level)
            button_embed = discord.Embed(title = "Boar", description = "Stats for a level " + str(level) + " boar", color = discord.Color.from_rgb(51, 25, 0))
            button_embed.add_field(name = monster.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def wolf_callback(interaction):
        if(interaction.user == member):
            monster = monsters.Wolf(level)
            button_embed = discord.Embed(title = "Wolf", description = "Stats for a level " + str(level) + " wolf", color = discord.Color.from_rgb(64, 64, 64))
            button_embed.add_field(name = monster.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def elf_callback(interaction):
        if(interaction.user == member):
            monster = monsters.Elf(level)
            button_embed = discord.Embed(title = "Elf", description = "Stats for a level " + str(level) + " elf", color = discord.Color.from_rgb(0, 102, 0))
            button_embed.add_field(name = monster.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def treant_callback(interaction):
        if(interaction.user == member):
            monster = monsters.Treant(level)
            button_embed = discord.Embed(title = "Treant", description = "Stats for a level " + str(level) + " treant", color = discord.Color.from_rgb(102, 51, 0))
            button_embed.add_field(name = monster.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def spider_callback(interaction):
        if(interaction.user == member):
            monster = monsters.GiantSpider(level)
            button_embed = discord.Embed(title = "Giant Spider", description = "Stats for a level " + str(level) + " giant spider", color = discord.Color.from_rgb(32, 32, 32))
            button_embed.add_field(name = monster.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def roper_callback(interaction):
        if(interaction.user == member):
            monster = monsters.Roper(level)
            button_embed = discord.Embed(title = "Roper", description = "Stats for a level " + str(level) + " roper", color = discord.Color.from_rgb(51, 0, 51))
            button_embed.add_field(name = monster.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def goblin_callback(interaction):
        if(interaction.user == member):
            monster = monsters.Goblin(level)
            button_embed = discord.Embed(title = "Goblin", description = "Stats for a level " + str(level) + " goblin", color = discord.Color.from_rgb(7, 50, 27))
            button_embed.add_field(name = monster.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def troll_callback(interaction):
        if(interaction.user == member):
            monster = monsters.Troll(level)
            button_embed = discord.Embed(title = "Troll", description = "Stats for a level " + str(level) + " troll", color = discord.Color.from_rgb(39, 58, 43))
            button_embed.add_field(name = monster.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def return_callback(interaction):
        if(interaction.user == member):
            await interaction.response.edit_message(embed = embed, view = view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    boar_button.callback = boar_callback
    wolf_button.callback = wolf_callback
    elf_button.callback = elf_callback
    treant_button.callback = treant_callback
    spider_button.callback = spider_callback
    roper_button.callback = roper_callback
    goblin_button.callback = goblin_callback
    troll_button.callback = troll_callback
    return_button.callback = return_callback

    # embed for monster_list
    embed = discord.Embed(title = "Monster List", description = "List of all current monsters\nSelect a button to view starting stats for the monster", color = discord.Color.from_rgb(51, 0, 102))
    embed.add_field(name = "Locations:", value = "", inline = False)
    embed.add_field(name = "Forest", value = "", inline = False)
    embed.add_field(name = "Cave", value = "", inline = False)
    embed.set_footer(text = f"{member.display_name} created this list")

    await ctx.response.send_message(embed = embed, view = view)

# combat against monsters
# user inputs the name of their character
# user is prompted to choose a location
# randomly chooses a monster from location and runs the combat
@tree.command(name='adventure', description='Start an adventure', guild=discord.Object(id=GUILD_ID))
async def adventure(ctx, name: str):
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
        if(interaction.user == member):
            chance = random.randint(1, 100)
            if(chance < 36):
                monster = monsters.Boar(player._level)
                player._health = player._maxHealth
                monster_health = monster._maxHealth
                health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)

                # combat view
                basic_attack_button = discord.ui.Button(label = "Basic Attack", custom_id = 'basic_attack', style = discord.ButtonStyle.red, row = 0)
                combat_view = discord.ui.View()
                combat_view.add_item(basic_attack_button)

                # button callbacks
                async def basic_attack_callback(interaction):
                    if(interaction.user == member):
                        player_damage = random.randint(1, player._str)
                        monster_damage = random.randint(1, monster._str)
                        player._health = player._health - monster_damage
                        monster._health = monster._health - player_damage
                        health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)
                        damage = "You did " + str(player_damage) + " damage using a basic attack.\nThe " + monster._name + " did " + str(monster_damage) + " damage"

                        if(player._health <= 0):
                            health = player._name + " Health: 0/" + str(player._maxHealth)

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            drops = f"You have received {monster._xp} xp.\n You have received {monster.calculateGold()} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)

                            # victory embed
                            victory_embed = discord.Embed(title = "Victory", description = f"You have defeated the {monster._name}.", color = discord.Color.from_rgb(0, 255, 0))
                            victory_embed.add_field(name = health, value = "", inline = False)
                            victory_embed.add_field(name = drops, value = "", inline = False)
                            victory_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = victory_embed, view = None)
                
                        else:
                            # next turn
                            turn_embed = discord.Embed(title = "Combat", description = "Select attack option", color = discord.Color.from_rgb(51, 25, 0))
                            turn_embed.set_thumbnail(url = "https://i.pinimg.com/originals/bb/49/24/bb4924f49fe7df5cf4c9d9123b4b9b86.png")
                            turn_embed.add_field(name = damage, value = "", inline = False)
                            turn_embed.add_field(name = health, value = "", inline = False)
                            turn_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = turn_embed, view = combat_view)
                    else:
                        # Not the same user
                        await interaction.response.send_message(content = "This is not your battle", ephemeral = True)

                basic_attack_button.callback = basic_attack_callback

                # combat embed
                combat_embed = discord.Embed(title = "Combat", description = f"You have encountered a {monster._name}.\nSelect attack option", color = discord.Color.from_rgb(51, 25, 0))
                combat_embed.set_thumbnail(url = "https://i.pinimg.com/originals/bb/49/24/bb4924f49fe7df5cf4c9d9123b4b9b86.png")
                combat_embed.add_field(name = health, value = "")
                combat_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = combat_embed, view = combat_view)

            elif(chance < 71):
                monster = monsters.Wolf(player._level)
                player._health = player._maxHealth
                monster_health = monster._maxHealth
                health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)

                # combat view
                basic_attack_button = discord.ui.Button(label = "Basic Attack", custom_id = 'basic_attack', style = discord.ButtonStyle.red, row = 0)
                combat_view = discord.ui.View()
                combat_view.add_item(basic_attack_button)

                # button callbacks
                async def basic_attack_callback(interaction):
                    if(interaction.user == member):
                        player_damage = random.randint(1, player._str)
                        monster_damage = random.randint(1, monster._str)
                        player._health = player._health - monster_damage
                        monster._health = monster._health - player_damage
                        health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)
                        damage = "You did " + str(player_damage) + " damage using a basic attack.\nThe " + monster._name + " did " + str(monster_damage) + " damage"

                        if(player._health <= 0):
                            health = player._name + " Health: 0/" + str(player._maxHealth)

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            drops = f"You have received {monster._xp} xp.\n You have received {monster.calculateGold()} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)

                            # victory embed
                            victory_embed = discord.Embed(title = "Victory", description = f"You have defeated the {monster._name}.", color = discord.Color.from_rgb(0, 255, 0))
                            victory_embed.add_field(name = health, value = "", inline = False)
                            victory_embed.add_field(name = drops, value = "", inline = False)
                            victory_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = victory_embed, view = None)

                        else:
                            # next turn
                            turn_embed = discord.Embed(title = "Combat", description = "Select attack option", color = discord.Color.from_rgb(64, 64, 64))
                            turn_embed.set_thumbnail(url = "https://static.wikia.nocookie.net/creaturequest/images/2/24/148_DireWolf.png/revision/latest/scale-to-width-down/378?cb=20170315223053")
                            turn_embed.add_field(name = damage, value = "", inline = False)
                            turn_embed.add_field(name = health, value = "", inline = False)
                            turn_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = turn_embed, view = combat_view)
                    else:
                        await interaction.response.send_message(content = "This is not your battle", ephemeral = True)

                basic_attack_button.callback = basic_attack_callback

                # combat embed
                combat_embed = discord.Embed(title = "Combat", description = f"You have encountered a {monster._name}.\nSelect attack option", color = discord.Color.from_rgb(64, 64, 64))
                combat_embed.set_thumbnail(url = "https://static.wikia.nocookie.net/creaturequest/images/2/24/148_DireWolf.png/revision/latest/scale-to-width-down/378?cb=20170315223053")
                combat_embed.add_field(name = health, value = "")
                combat_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = combat_embed, view = combat_view)


            elif(chance < 91):
                monster = monsters.Elf(player._level)
                player._health = player._maxHealth
                monster_health = monster._maxHealth
                health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)

                # combat view
                basic_attack_button = discord.ui.Button(label = "Basic Attack", custom_id = 'basic_attack', style = discord.ButtonStyle.red, row = 0)
                combat_view = discord.ui.View()
                combat_view.add_item(basic_attack_button)

                # button callbacks
                async def basic_attack_callback(interaction):
                    if(interaction.user == member):
                        player_damage = random.randint(1, player._str)
                        monster_damage = random.randint(1, monster._str)
                        player._health = player._health - monster_damage
                        monster._health = monster._health - player_damage
                        health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)
                        damage = "You did " + str(player_damage) + " damage using a basic attack.\nThe " + monster._name + " did " + str(monster_damage) + " damage"

                        if(player._health <= 0):
                            health = player._name + " Health: 0/" + str(player._maxHealth)

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            drops = f"You have received {monster._xp} xp.\n You have received {monster.calculateGold()} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)

                            # victory embed
                            victory_embed = discord.Embed(title = "Victory", description = f"You have defeated the {monster._name}.", color = discord.Color.from_rgb(0, 255, 0))
                            victory_embed.add_field(name = health, value = "", inline = False)
                            victory_embed.add_field(name = drops, value = "", inline = False)
                            victory_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = victory_embed, view = None)
                    
                        else:
                            # next turn
                            turn_embed = discord.Embed(title = "Combat", description = "Select attack option", color = discord.Color.from_rgb(0, 102, 0))
                            turn_embed.set_thumbnail(url = "https://i.pinimg.com/originals/4e/2f/12/4e2f12b4ad01eeaae5b0a3b2f8f7647b.png")
                            turn_embed.add_field(name = damage, value = "", inline = False)
                            turn_embed.add_field(name = health, value = "", inline = False)
                            turn_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = turn_embed, view = combat_view)
                    else:
                        await interaction.response.send_message(content = "This is not your battle", ephemeral = True)

                basic_attack_button.callback = basic_attack_callback

                # combat embed
                combat_embed = discord.Embed(title = "Combat", description = f"You have encountered a {monster._name}.\nSelect attack option", color = discord.Color.from_rgb(0, 102, 0))
                combat_embed.set_thumbnail(url = "https://i.pinimg.com/originals/4e/2f/12/4e2f12b4ad01eeaae5b0a3b2f8f7647b.png")
                combat_embed.add_field(name = health, value = "")
                combat_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = combat_embed, view = combat_view)

            else:
                monster = monsters.Treant(player._level)
                player._health = player._maxHealth
                monster_health = monster._maxHealth
                health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)

                # combat view
                basic_attack_button = discord.ui.Button(label = "Basic Attack", custom_id = 'basic_attack', style = discord.ButtonStyle.red, row = 0)
                combat_view = discord.ui.View()
                combat_view.add_item(basic_attack_button)

                # button callbacks
                async def basic_attack_callback(interaction):
                    if(interaction.user == member):
                        player_damage = random.randint(1, player._str)
                        monster_damage = random.randint(1, monster._str)
                        player._health = player._health - monster_damage
                        monster._health = monster._health - player_damage
                        health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)
                        damage = "You did " + str(player_damage) + " damage using a basic attack.\nThe " + monster._name + " did " + str(monster_damage) + " damage"

                        if(player._health <= 0):
                            health = player._name + " Health: 0/" + str(player._maxHealth)

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            drops = f"You have received {monster._xp} xp.\n You have received {monster.calculateGold()} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)

                            # victory embed
                            victory_embed = discord.Embed(title = "Victory", description = f"You have defeated the {monster._name}.", color = discord.Color.from_rgb(0, 255, 0))
                            victory_embed.add_field(name = health, value = "", inline = False)
                            victory_embed.add_field(name = drops, value = "", inline = False)
                            victory_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = victory_embed, view = None)
                    
                        else:
                            # next turn
                            turn_embed = discord.Embed(title = "Combat", description = "Select attack option", color = discord.Color.from_rgb(102, 51, 0))
                            turn_embed.set_thumbnail(url = "https://www.dndbeyond.com/avatars/thumbnails/30836/130/1000/1000/638063929302059775.png")
                            turn_embed.add_field(name = damage, value = "", inline = False)
                            turn_embed.add_field(name = health, value = "", inline = False)
                            turn_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = turn_embed, view = combat_view)
                    else:
                        await interaction.response.send_message(content = "This is not your battle", ephemeral = True)

                basic_attack_button.callback = basic_attack_callback

                # combat embed
                combat_embed = discord.Embed(title = "Combat", description = f"You have encountered a {monster._name}.\nSelect attack option", color = discord.Color.from_rgb(102, 51, 0))
                combat_embed.set_thumbnail(url = "https://www.dndbeyond.com/avatars/thumbnails/30836/130/1000/1000/638063929302059775.png")
                combat_embed.add_field(name = health, value = "")
                combat_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = combat_embed, view = combat_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your battle", ephemeral = True)

    async def cave_callback(interaction):
        if(interaction.user == member):
            chance = random.randint(1, 100)
            if(chance < 36):
                monster = monsters.GiantSpider(player._level)
                player._health = player._maxHealth
                monster_health = monster._maxHealth
                health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)

                # combat view
                basic_attack_button = discord.ui.Button(label = "Basic Attack", custom_id = 'basic_attack', style = discord.ButtonStyle.red, row = 0)
                combat_view = discord.ui.View()
                combat_view.add_item(basic_attack_button)

                # button callbacks
                async def basic_attack_callback(interaction):
                    if(interaction.user == member):
                        player_damage = random.randint(1, player._str)
                        monster_damage = random.randint(1, monster._str)
                        player._health = player._health - monster_damage
                        monster._health = monster._health - player_damage
                        health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)
                        damage = "You did " + str(player_damage) + " damage using a basic attack.\nThe " + monster._name + " did " + str(monster_damage) + " damage"

                        if(player._health <= 0):
                            health = player._name + " Health: 0/" + str(player._maxHealth)

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            drops = f"You have received {monster._xp} xp.\n You have received {monster.calculateGold()} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)

                            # victory embed
                            victory_embed = discord.Embed(title = "Victory", description = f"You have defeated the {monster._name}.", color = discord.Color.from_rgb(0, 255, 0))
                            victory_embed.add_field(name = health, value = "", inline = False)
                            victory_embed.add_field(name = drops, value = "", inline = False)
                            victory_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = victory_embed, view = None)
                    
                        else:
                            # next turn
                            turn_embed = discord.Embed(title = "Combat", description = "Select attack option", color = discord.Color.from_rgb(32, 32, 32))
                            turn_embed.set_thumbnail(url = "https://freepngimg.com/thumb/spider/35341-9-black-widow-spider-transparent.png")
                            turn_embed.add_field(name = damage, value = "", inline = False)
                            turn_embed.add_field(name = health, value = "", inline = False)
                            turn_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = turn_embed, view = combat_view)
                    else:
                        await interaction.response.send_message(content = "This is not your battle", ephemeral = True)

                basic_attack_button.callback = basic_attack_callback

                # combat embed
                combat_embed = discord.Embed(title = "Combat", description = f"You have encountered a {monster._name}.\nSelect attack option", color = discord.Color.from_rgb(32, 32, 32))
                combat_embed.set_thumbnail(url = "https://freepngimg.com/thumb/spider/35341-9-black-widow-spider-transparent.png")
                combat_embed.add_field(name = health, value = "")
                combat_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = combat_embed, view = combat_view)

            elif(chance < 71):
                monster = monsters.Roper(player._level)
                player._health = player._maxHealth
                monster_health = monster._maxHealth
                health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)

                # combat view
                basic_attack_button = discord.ui.Button(label = "Basic Attack", custom_id = 'basic_attack', style = discord.ButtonStyle.red, row = 0)
                combat_view = discord.ui.View()
                combat_view.add_item(basic_attack_button)

                # button callbacks
                async def basic_attack_callback(interaction):
                    if(interaction.user == member):
                        player_damage = random.randint(1, player._str)
                        monster_damage = random.randint(1, monster._str)
                        player._health = player._health - monster_damage
                        monster._health = monster._health - player_damage
                        health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)
                        damage = "You did " + str(player_damage) + " damage using a basic attack.\nThe " + monster._name + " did " + str(monster_damage) + " damage"

                        if(player._health <= 0):
                            health = player._name + " Health: 0/" + str(player._maxHealth)

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            drops = f"You have received {monster._xp} xp.\n You have received {monster.calculateGold()} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)

                            # victory embed
                            victory_embed = discord.Embed(title = "Victory", description = f"You have defeated the {monster._name}.", color = discord.Color.from_rgb(0, 255, 0))
                            victory_embed.add_field(name = health, value = "", inline = False)
                            victory_embed.add_field(name = drops, value = "", inline = False)
                            victory_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = victory_embed, view = None)
                    
                        else:
                            # next turn
                            turn_embed = discord.Embed(title = "Combat", description = "Select attack option", color = discord.Color.from_rgb(51, 0, 51))
                            turn_embed.set_thumbnail(url = "https://www.dndbeyond.com/avatars/thumbnails/30834/993/1000/1000/638063901980029135.png")
                            turn_embed.add_field(name = damage, value = "", inline = False)
                            turn_embed.add_field(name = health, value = "", inline = False)
                            turn_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = turn_embed, view = combat_view)
                    else:
                        await interaction.response.send_message(content = "This is not your battle", ephemeral = True)

                basic_attack_button.callback = basic_attack_callback

                # combat embed
                combat_embed = discord.Embed(title = "Combat", description = f"You have encountered a {monster._name}.\nSelect attack option", color = discord.Color.from_rgb(51, 0, 51))
                combat_embed.set_thumbnail(url = "https://www.dndbeyond.com/avatars/thumbnails/30834/993/1000/1000/638063901980029135.png")
                combat_embed.add_field(name = health, value = "")
                combat_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = combat_embed, view = combat_view)


            elif(chance < 91):
                monster = monsters.Goblin(player._level)
                player._health = player._maxHealth
                monster_health = monster._maxHealth
                health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)

                # combat view
                basic_attack_button = discord.ui.Button(label = "Basic Attack", custom_id = 'basic_attack', style = discord.ButtonStyle.red, row = 0)
                combat_view = discord.ui.View()
                combat_view.add_item(basic_attack_button)

                # button callbacks
                async def basic_attack_callback(interaction):
                    if(interaction.user == member):
                        player_damage = random.randint(1, player._str)
                        monster_damage = random.randint(1, monster._str)
                        player._health = player._health - monster_damage
                        monster._health = monster._health - player_damage
                        health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)
                        damage = "You did " + str(player_damage) + " damage using a basic attack.\nThe " + monster._name + " did " + str(monster_damage) + " damage"

                        if(player._health <= 0):
                            health = player._name + " Health: 0/" + str(player._maxHealth)

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            drops = f"You have received {monster._xp} xp.\n You have received {monster.calculateGold()} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)

                            # victory embed
                            victory_embed = discord.Embed(title = "Victory", description = f"You have defeated the {monster._name}.", color = discord.Color.from_rgb(0, 255, 0))
                            victory_embed.add_field(name = health, value = "", inline = False)
                            victory_embed.add_field(name = drops, value = "", inline = False)
                            victory_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = victory_embed, view = None)
                    
                        else:
                            # next turn
                            turn_embed = discord.Embed(title = "Combat", description = "Select attack option", color = discord.Color.from_rgb(7, 50, 27))
                            turn_embed.set_thumbnail(url = "https://i.pinimg.com/originals/5b/9a/86/5b9a862f2e584eae40d8851e025847b8.png")
                            turn_embed.add_field(name = damage, value = "", inline = False)
                            turn_embed.add_field(name = health, value = "", inline = False)
                            turn_embed.set_footer(text = f"{member.display_name} created this")
                            await interaction.response.edit_message(embed = turn_embed, view = combat_view)
                    else:
                        await interaction.response.send_message(content = "This is not your battle", ephemeral = True)

                basic_attack_button.callback = basic_attack_callback

                # combat embed
                combat_embed = discord.Embed(title = "Combat", description = f"You have encountered a {monster._name}.\nSelect attack option", color = discord.Color.from_rgb(7, 50, 27))
                combat_embed.set_thumbnail(url = "https://i.pinimg.com/originals/5b/9a/86/5b9a862f2e584eae40d8851e025847b8.png")
                combat_embed.add_field(name = health, value = "")
                combat_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = combat_embed, view = combat_view)

            else:
                monster = monsters.Troll(player._level)
                player._health = player._maxHealth
                monster_health = monster._maxHealth
                health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)

                # combat view
                basic_attack_button = discord.ui.Button(label = "Basic Attack", custom_id = 'basic_attack', style = discord.ButtonStyle.red, row = 0)
                combat_view = discord.ui.View()
                combat_view.add_item(basic_attack_button)

                # button callbacks
                async def basic_attack_callback(interaction):
                    if(interaction.user == member):
                        player_damage = random.randint(1, player._str)
                        monster_damage = random.randint(1, monster._str)
                        player._health = player._health - monster_damage
                        monster._health = monster._health - player_damage
                        health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth) + "   " + monster._name + " Health: " + str(monster._health) + "/" + str(monster._maxHealth)
                        damage = "You did " + str(player_damage) + " damage using a basic attack.\nThe " + monster._name + " did " + str(monster_damage) + " damage"

                        if(player._health <= 0):
                            health = player._name + " Health: 0/" + str(player._maxHealth)

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            drops = f"You have received {monster._xp} xp.\n You have received {monster.calculateGold()} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)

                            # victory embed
                            victory_embed = discord.Embed(title = "Victory", description = f"You have defeated the {monster._name}.", color = discord.Color.from_rgb(0, 255, 0))
                            victory_embed.add_field(name = health, value = "", inline = False)
                            victory_embed.add_field(name = drops, value = "", inline = False)
                            victory_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = victory_embed, view = None)
                    
                        else:
                            # next turn
                            turn_embed = discord.Embed(title = "Combat", description = "Select attack option", color = discord.Color.from_rgb(39, 58, 43))
                            turn_embed.set_thumbnail(url = "https://www.dndbeyond.com/avatars/thumbnails/30836/144/1000/1000/638063929586218907.png")
                            turn_embed.add_field(name = damage, value = "", inline = False)
                            turn_embed.add_field(name = health, value = "", inline = False)
                            turn_embed.set_footer(text = f"{member.display_name} created this")
                            await interaction.response.edit_message(embed = turn_embed, view = combat_view)
                    else:
                        await interaction.response.send_message(content = "This is not your battle", ephemeral = True)

                basic_attack_button.callback = basic_attack_callback

                # combat embed
                combat_embed = discord.Embed(title = "Combat", description = f"You have encountered a {monster._name}.\nSelect attack option", color = discord.Color.from_rgb(39, 58, 43))
                combat_embed.set_thumbnail(url = "https://www.dndbeyond.com/avatars/thumbnails/30836/144/1000/1000/638063929586218907.png")
                combat_embed.add_field(name = health, value = "")
                combat_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = combat_embed, view = combat_view)
        
        else:
            await interaction.response.send_message(content = "This is not your battle", ephemeral = True)

    forest_button.callback = forest_callback
    cave_button.callback = cave_callback

    # embed for adventure
    embed = discord.Embed(title = "Adventure", description = "Select the location you would like to adventure to\n", color = discord.Color.from_rgb(204, 102, 0))
    embed.set_footer(text = f"{member.display_name} created this")

    await ctx.response.send_message(embed = embed, view = view)

client.run(TOKEN)
