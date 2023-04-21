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

# delete a character
# takes a name
# removes character with that name from the database if they exist
@tree.command(name='delete_character', description='delete your charater', guild=discord.Object(id=GUILD_ID))
async def delete_character(ctx, name: str):
    player = character.Character(name, "", ctx.user.id)
    player.deleteCharacter()
    await ctx.response.send_message(content = "Your character has been deleted.", ephemeral = True)

# see the list of all starting classes
# returns a response with all classes as a list
@tree.command(name='class_list', description='view the list of starting classes', guild=discord.Object(id=GUILD_ID))
async def class_list(ctx):
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
    
    # return view
    return_button = discord.ui.Button(label = "Return", custom_id = 'return', style = discord.ButtonStyle.red)
    return_view = discord.ui.View()
    return_view.add_item(return_button)

    # button callbacks
    async def cleric_callback(interaction):
        if(interaction.user == member):
            charClass = classes.Cleric()
            button_embed = discord.Embed(title = "Cleric", description = "Starting stats for a cleric", color = discord.Color.from_rgb(255, 255, 255))
            button_embed.add_field(name = charClass.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def hunter_callback(interaction):
        if(interaction.user == member):
            charClass = classes.Hunter()
            button_embed = discord.Embed(title = "Hunter", description = "Starting stats for a hunter", color = discord.Color.from_rgb(0, 51, 0))
            button_embed.add_field(name = charClass.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)
    
    async def mage_callback(interaction):
        if(interaction.user == member):
            charClass = classes.Mage()
            button_embed = discord.Embed(title = "Mage", description = "Starting stats for a mage", color = discord.Color.from_rgb(0, 0, 153))
            button_embed.add_field(name = charClass.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def paladin_callback(interaction):
        if(interaction.user == member):
            charClass = classes.Paladin()
            button_embed = discord.Embed(title = "Paladin", description = "Starting stats for a paladin", color = discord.Color.from_rgb(153, 0, 0))
            button_embed.add_field(name = charClass.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def thief_callback(interaction):
        if(interaction.user == member):
            charClass = classes.Thief()
            button_embed = discord.Embed(title = "Thief", description = "Starting stats for a thief", color = discord.Color.from_rgb(0, 0, 0))
            button_embed.add_field(name = charClass.displayStats(), value = "")
            await interaction.response.edit_message(embed = button_embed, view = return_view)
        else:
            # Not the same user
            await interaction.response.send_message(content = "This is not your list", ephemeral = True)

    async def warrior_callback(interaction):
        if(interaction.user == member):
            charClass = classes.Warrior()
            button_embed = discord.Embed(title = "Warrior", description = "Starting stats for a warrior", color = discord.Color.from_rgb(64, 64, 64))
            button_embed.add_field(name = charClass.displayStats(), value = "")
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

    cleric_button.callback = cleric_callback
    hunter_button.callback = hunter_callback
    mage_button.callback = mage_callback
    paladin_button.callback = paladin_callback
    thief_button.callback = thief_callback
    warrior_button.callback = warrior_callback
    return_button.callback = return_callback

    # embed for class_list
    embed = discord.Embed(title = "Class List", description = "List of starting classes\nPress a button to view starting stats", color = discord.Color.from_rgb(255, 255, 0))
    embed.set_footer(text = f"{member.display_name} created this list")

    await ctx.response.send_message(embed = embed, view = view)

# view stats and eqiptment of character with given name
# takes character's name as an argument
# returns the name, class, level, health, and mana of that character stored in the database
@tree.command(name='view_character', description="view selected character's stats and equiptment", guild=discord.Object(id=GUILD_ID))
async def view_character(ctx, name: str):
    member = ctx.user
    test = character.Character(name, "", ctx.user.id)

    if test.getCharacter(ctx.user.id, name):
        output = f"""{test._name}
Level {test._level} {test._characterClass}
Health {test._health}/{test._maxHealth} Mana {test._mana}/{test._maxMana}\n
VIG: {test._vigor} STR: {test._str}
DEX: {test._dex} INT: {test._int}
Gold: {test._gold} XP: {test._xp}\n
Health Potions: {test._healthPotions}
Mana Potions: {test._manaPotions}"""

        # embed for view_character
        embed = discord.Embed(title = "Character View", description = "", color = discord.Color.from_rgb(0, 0, 0))
        embed.add_field(name = output, value = "")
        embed.set_footer(text = f"{member.display_name} created this list")

        await ctx.response.send_message(embed = embed)
    else:
        await ctx.response.send_message(content = "Could not a find character with that name assigned to you", ephemeral = True)

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

# a shop to purchase items
# takes the character's name
# opens a shop for the user to buy items using the gold the character has earned
@tree.command(name='shop', description="Open the item shop", guild=discord.Object(id=GUILD_ID))
async def shop(ctx, name:str):
    member = ctx.user

    player = character.Character(name, "", ctx.user.id)
    player.getCharacter(ctx.user.id, name)
    pockets = f"You have {player._gold} gold on your person."
    inventory = "Health Potion - 50 gold \nMana Potion - 50 gold"

    # view for shop
    healthpot_button = discord.ui.Button(label = "Health Potion", custom_id = 'healthpot', style = discord.ButtonStyle.red, row = 0)
    manapot_button = discord.ui.Button(label = "Mana Potion", custom_id = 'manapot', style = discord.ButtonStyle.blurple, row = 0)
    view = discord.ui.View()
    view.add_item(healthpot_button)
    view.add_item(manapot_button)

    # button callbacks
    async def healthpot_callback(interaction):
        if(interaction.user == member):
            if(player._gold < 50):
                poor = "You can not afford a health potion."
                pockets = f"You have {player._gold} gold on your person."

                # poor embed
                poor_embed = discord.Embed(title = "Shop", description = f"Purchase an item by clicking on it's button", color = discord.Color.from_rgb(255, 255, 255))
                poor_embed.add_field(name = poor, value = "", inline = False)
                poor_embed.add_field(name = pockets, value = "", inline = False)
                poor_embed.add_field(name = inventory, value = "", inline = False)
                poor_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = poor_embed)

            else:
                # update character
                player._gold = player._gold - 50
                player._healthPotions = player._healthPotions + 1
                player.updateCharacter()

                purchase = "You have purchased a health potion."
                pockets = f"You have {player._gold} gold on your person."

                # purchase embed
                purchase_embed = discord.Embed(title = "Shop", description = f"Purchase an item by clicking on it's button", color = discord.Color.from_rgb(255, 255, 255))
                purchase_embed.add_field(name = purchase, value = "", inline = False)
                purchase_embed.add_field(name = pockets, value = "", inline = False)
                purchase_embed.add_field(name = inventory, value = "", inline = False)
                purchase_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = purchase_embed)
        else:
            await interaction.response.send_message(content = "This merchant is busy.", ephemeral = True)

    async def manapot_callback(interaction):
        if(interaction.user == member):
            if(player._gold < 50):
                poor = "You can not afford a mana potion."
                pockets = f"You have {player._gold} gold on your person."

                # poor embed
                poor_embed = discord.Embed(title = "Shop", description = f"Purchase an item by clicking on it's button", color = discord.Color.from_rgb(255, 255, 255))
                poor_embed.add_field(name = poor, value = "", inline = False)
                poor_embed.add_field(name = pockets, value = "", inline = False)
                poor_embed.add_field(name = inventory, value = "", inline = False)
                poor_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = poor_embed)

            else:
                # update character
                player._gold = player._gold - 50
                player._manaPotions = player._manaPotions + 1
                player.updateCharacter()

                purchase = "You have purchased a mana potion."
                pockets = f"You have {player._gold} gold on your person."

                # purchase embed
                purchase_embed = discord.Embed(title = "Shop", description = f"Purchase an item by clicking on it's button", color = discord.Color.from_rgb(255, 255, 255))
                purchase_embed.add_field(name = purchase, value = "", inline = False)
                purchase_embed.add_field(name = pockets, value = "", inline = False)
                purchase_embed.add_field(name = inventory, value = "", inline = False)
                purchase_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = purchase_embed)
        else:
            await interaction.response.send_message(content = "This merchant is busy.", ephemeral = True)

    healthpot_button.callback = healthpot_callback
    manapot_button.callback = manapot_callback

    # embed for shop
    embed = discord.Embed(title = "Shop", description = f"Purchase an item by clicking on it's button", color = discord.Color.from_rgb(255, 255, 255))
    embed.add_field(name = pockets, value = "", inline = False)
    embed.add_field(name = inventory, value = "", inline = False)
    embed.set_footer(text = f"{member.display_name} created this")

    await ctx.response.send_message(embed = embed, view = view)

# level up
# takes the character's name
# lets the user increase their character's stats
@tree.command(name='level_up', description='Level up your character', guild=discord.Object(id=GUILD_ID))
async def level_up(ctx, name: str):
    member = ctx.user

    player = character.Character(name, "", ctx.user.id)
    player.getCharacter(ctx.user.id, name)

    xp = f"{player._name} is Level {player._level} and has {player._xp} xp"
    xp_required = pow(2, (player._level - 1)) * 250
    required = f"You require {xp_required} xp to level up"

    # view for level up
    level_button = discord.ui.Button(label = "Level Up", custom_id = 'level', style = discord.ButtonStyle.green)
    view = discord.ui.View()
    view.add_item(level_button)

    # button callbacks
    async def level_callback(interaction):
        if(interaction.user == member):
            if(player._xp >= xp_required):
                # view for stats
                vig_button = discord.ui.Button(label = "Vigor", custom_id = 'vigor', style = discord.ButtonStyle.grey, row = 0)
                str_button = discord.ui.Button(label = "Strength", custom_id = 'strength', style = discord.ButtonStyle.grey, row = 0)
                dex_button = discord.ui.Button(label = "Dexterity", custom_id = 'dexterity', style = discord.ButtonStyle.grey, row = 0)
                int_button = discord.ui.Button(label = "Intelligence", custom_id = 'intelligence', style = discord.ButtonStyle.grey, row = 0)
                stats_view = discord.ui.View()
                stats_view.add_item(vig_button)
                stats_view.add_item(str_button)
                stats_view.add_item(dex_button)
                stats_view.add_item(int_button)

                # button callbacks
                async def vig_callback(interaction):
                    if(interaction.user == member):
                        player._index = player._index + 1
                        player._vigor = player._vigor + 1

                        if(player._index < 3):
                            # embed for stats
                            stats_embed = discord.Embed(title = "Increase Stats", description = f"Select the stat you want to upgrade.", color = discord.Color.from_rgb(0, 255, 0))
                            stats_embed.add_field(name = f"You have {3 - player._index} choice(s) left.", value = "", inline = False)
                            stats_embed.set_footer(text = f"{member.display_name} created this")
                            
                            await interaction.response.edit_message(embed = stats_embed, view = stats_view)
                        else:
                            player._level = player._level + 1
                            player._xp = player._xp - xp_required
                            player.updateCharacter()

                            # embed for finished
                            finished_embed = discord.Embed(title = "Level Up Complete", description = f"Your character has successfully leveled up.", color = discord.Color.from_rgb(0, 255, 0))
                            finished_embed.add_field(name = f"{player._name} has increased to Level {player._level}.", value = "", inline = False)
                            finished_embed.add_field(name = f"{player._name} now has {player._xp} xp.", value = "", inline = False)
                            finished_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = finished_embed, view = None)

                    else:
                        await interaction.response.send_message(content = "This is not your character", ephemeral = True)

                async def str_callback(interaction):
                    if(interaction.user == member):
                        player._index = player._index + 1
                        player._str = player._str + 1

                        if(player._index < 3):
                            # embed for stats
                            stats_embed = discord.Embed(title = "Increase Stats", description = f"Select the stat you want to upgrade.", color = discord.Color.from_rgb(0, 255, 0))
                            stats_embed.add_field(name = f"You have {3 - player._index} choice(s) left.", value = "", inline = False)
                            stats_embed.set_footer(text = f"{member.display_name} created this")
                            
                            await interaction.response.edit_message(embed = stats_embed, view = stats_view)
                        else:
                            player._level = player._level + 1
                            player._xp = player._xp - xp_required
                            player.updateCharacter()

                            # embed for finished
                            finished_embed = discord.Embed(title = "Level Up Complete", description = f"Your character has successfully leveled up.", color = discord.Color.from_rgb(0, 255, 0))
                            finished_embed.add_field(name = f"{player._name} has increased to Level {player._level}.", value = "", inline = False)
                            finished_embed.add_field(name = f"{player._name} now has {player._xp} xp.", value = "", inline = False)
                            finished_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = finished_embed, view = None)

                    else:
                        await interaction.response.send_message(content = "This is not your character", ephemeral = True)

                async def dex_callback(interaction):
                    if(interaction.user == member):
                        player._index = player._index + 1
                        player._dex = player._dex + 1

                        if(player._index < 3):
                            # embed for stats
                            stats_embed = discord.Embed(title = "Increase Stats", description = f"Select the stat you want to upgrade.", color = discord.Color.from_rgb(0, 255, 0))
                            stats_embed.add_field(name = f"You have {3 - player._index} choice(s) left.", value = "", inline = False)
                            stats_embed.set_footer(text = f"{member.display_name} created this")
                            
                            await interaction.response.edit_message(embed = stats_embed, view = stats_view)
                        else:
                            player._level = player._level + 1
                            player._xp = player._xp - xp_required
                            player.updateCharacter()

                            # embed for finished
                            finished_embed = discord.Embed(title = "Level Up Complete", description = f"Your character has successfully leveled up.", color = discord.Color.from_rgb(0, 255, 0))
                            finished_embed.add_field(name = f"{player._name} has increased to Level {player._level}.", value = "", inline = False)
                            finished_embed.add_field(name = f"{player._name} now has {player._xp} xp.", value = "", inline = False)
                            finished_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = finished_embed, view = None)

                    else:
                        await interaction.response.send_message(content = "This is not your character", ephemeral = True)

                async def int_callback(interaction):
                    if(interaction.user == member):
                        player._index = player._index + 1
                        player._int = player._int + 1

                        if(player._index < 3):
                            # embed for stats
                            stats_embed = discord.Embed(title = "Increase Stats", description = f"Select the stat you want to upgrade.", color = discord.Color.from_rgb(0, 255, 0))
                            stats_embed.add_field(name = f"You have {3 - player._index} choice(s) left.", value = "", inline = False)
                            stats_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = stats_embed, view = stats_view)
                        else:
                            player._level = player._level + 1
                            player._xp = player._xp - xp_required
                            player.updateCharacter()

                            # embed for finished
                            finished_embed = discord.Embed(title = "Level Up Complete", description = f"Your character has successfully leveled up.", color = discord.Color.from_rgb(0, 255, 0))
                            finished_embed.add_field(name = f"{player._name} has increased to Level {player._level}.", value = "", inline = False)
                            finished_embed.add_field(name = f"{player._name} now has {player._xp} xp.", value = "", inline = False)
                            finished_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = finished_embed, view = None)

                    else:
                        await interaction.response.send_message(content = "This is not your character", ephemeral = True)

                vig_button.callback = vig_callback
                str_button.callback = str_callback
                dex_button.callback = dex_callback
                int_button.callback = int_callback

                # embed for stats
                stats_embed = discord.Embed(title = "Increase Stats", description = f"Select the stat you want to upgrade.", color = discord.Color.from_rgb(0, 255, 0))
                stats_embed.add_field(name = f"You have {3 - player._index} choice(s) left.", value = "", inline = False)
                stats_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = stats_embed, view = stats_view)

            else:
                # embed for failed
                failed_embed = discord.Embed(title = "Level Up Failed", description = f"{player._name} does not have enough xp to level up.", color = discord.Color.from_rgb(255, 0, 0))
                failed_embed.set_footer(text = f"{member.display_name} created this")

                await interaction.response.edit_message(embed = failed_embed, view = None)

        else:
            await interaction.response.send_message(content = "This is not your character", ephemeral = True)

    level_button.callback = level_callback

    # embed for level up
    embed = discord.Embed(title = "Level Up", description = f"Use xp to increase your characters stats. \nOne level allows you to increase three stats.", color = discord.Color.from_rgb(0, 0, 255))
    embed.add_field(name = required, value = "", inline = False)
    embed.add_field(name = xp, value = "", inline = False)
    embed.set_footer(text = f"{member.display_name} created this")

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
                            gold_lost = round(player._gold * 0.05)
                            lost = f"You have dropped {gold_lost} gold."
                            player._gold = player._gold - gold_lost
                            player._health = player._maxHealth
                            player.updateCharacter()

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.add_field(name = lost, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            gold_earned = monster.calculateGold()
                            drops = f"You have received {monster._xp} xp.\nYou have received {gold_earned} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)
                            player._xp = player._xp + monster._xp
                            player._gold = player._gold + gold_earned
                            player.updateCharacter()

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
                            gold_lost = round(player._gold * 0.05)
                            lost = f"You have dropped {gold_lost} gold."
                            player._gold = player._gold - gold_lost
                            player._health = player._maxHealth
                            player.updateCharacter()

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.add_field(name = lost, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            gold_earned = monster.calculateGold()
                            drops = f"You have received {monster._xp} xp.\nYou have received {gold_earned} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)
                            player._xp = player._xp + monster._xp
                            player._gold = player._gold + gold_earned
                            player.updateCharacter()

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
                            gold_lost = round(player._gold * 0.05)
                            lost = f"You have dropped {gold_lost} gold."
                            player._gold = player._gold - gold_lost
                            player._health = player._maxHealth
                            player.updateCharacter()

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.add_field(name = lost, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            gold_earned = monster.calculateGold()
                            drops = f"You have received {monster._xp} xp.\nYou have received {gold_earned} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)
                            player._xp = player._xp + monster._xp
                            player._gold = player._gold + gold_earned
                            player.updateCharacter()

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
                            gold_lost = round(player._gold * 0.05)
                            lost = f"You have dropped {gold_lost} gold."
                            player._health = player._maxHealth
                            player._gold = player._gold - gold_lost
                            player.updateCharacter()

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.add_field(name = lost, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            gold_earned = monster.calculateGold()
                            drops = f"You have received {monster._xp} xp.\nYou have received {gold_earned} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)
                            player._xp = player._xp + monster._xp
                            player._gold = player._gold + gold_earned
                            player.updateCharacter()

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
                            gold_lost = round(player._gold * 0.05)
                            lost = f"You have dropped {gold_lost} gold."
                            player._gold = player._gold - gold_lost
                            player._health = player._maxHealth
                            player.updateCharacter()

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.add_field(name = lost, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            gold_earned = monster.calculateGold()
                            drops = f"You have received {monster._xp} xp.\nYou have received {gold_earned} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)
                            player._xp = player._xp + monster._xp
                            player._gold = player._gold + gold_earned
                            player.updateCharacter()

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
                            gold_lost = round(player._gold * 0.05)
                            lost = f"You have dropped {gold_lost} gold."
                            player._gold = player._gold - gold_lost
                            player._health = player._maxHealth
                            player.updateCharacter()

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.add_field(name = lost, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            gold_earned = monster.calculateGold()
                            drops = f"You have received {monster._xp} xp.\nYou have received {gold_earned} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)
                            player._xp = player._xp + monster._xp
                            player._gold = player._gold + gold_earned
                            player.updateCharacter()

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
                            gold_lost = round(player._gold * 0.05)
                            lost = f"You have dropped {gold_lost} gold."
                            player._gold = player._gold - gold_lost
                            player._health = player._maxHealth
                            player.updateCharacter()

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.add_field(name = lost, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            gold_earned = monster.calculateGold()
                            drops = f"You have received {monster._xp} xp.\nYou have received {gold_earned} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)
                            player._xp = player._xp + monster._xp
                            player._gold = player._gold + gold_earned
                            player.updateCharacter()

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
                            gold_lost = round(player._gold * 0.05)
                            lost = f"You have dropped {gold_lost} gold."
                            player._gold = player._gold - gold_lost
                            player._health = player._maxHealth
                            player.updateCharacter()

                            # loss embed
                            loss_embed = discord.Embed(title = "Defeat", description = f"You have lost the battle against the {monster._name}.", color = discord.Color.from_rgb(255, 0, 0))
                            loss_embed.set_thumbnail(url = "https://cdn.vectorstock.com/i/1000x1000/62/84/skull-and-crossbones-black-coin-vector-19416284.webp")
                            loss_embed.add_field(name = damage, value = "", inline = False)
                            loss_embed.add_field(name = health, value = "", inline = False)
                            loss_embed.add_field(name = lost, value = "", inline = False)
                            loss_embed.set_footer(text = f"{member.display_name} created this")

                            await interaction.response.edit_message(embed = loss_embed, view = None)

                        elif(monster._health <= 0):
                            gold_earned = monster.calculateGold()
                            drops = f"You have received {monster._xp} xp.\nYou have received {gold_earned} gold."
                            health = player._name + " Health: " + str(player._health) + "/" + str(player._maxHealth)
                            player._xp = player._xp + monster._xp
                            player._gold = player._gold + gold_earned
                            player.updateCharacter()

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
