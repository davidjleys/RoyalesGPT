from discord import Intents
from discord.ext import commands

def setup_bot():
    intents = Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    return bot
