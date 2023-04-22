import config
from bot_setup import setup_bot
from rs3_api import Runemetrics

bot = setup_bot()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.load_extension("cogs.runescape_stats")
bot.load_extension("cogs.openai_ask")

bot.run(config.DISCORD_TOKEN)
