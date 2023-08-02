import discord 
from discord import * 

bot = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(bot)

def botstart(token):
    bot.run(token)

async def onready():
    print(f"loged in to {bot.user.name}")
    try:
        await tree.sync()
        print("synced to discord")
    except Exception as e:
        print({e})

event = bot.event
command = tree.command

CustomColor = discord.Color.from_rgb
