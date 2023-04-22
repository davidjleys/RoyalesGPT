import io
import utils.image_gen
from discord.ext import commands
from discord import File
from utils.rs3_utils import get_player_stats

stats_bg_path = "./resources/stats_function_bg.png"

class RuneScapeRunemetricsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="stats", description="Display player stats")
    async def stats(self, ctx, player_name: str):
        try:
            await ctx.defer()
            stats = get_player_stats(player_name)
            if stats:
                img = utils.image_gen.create_stats_image(player_name, stats, stats_bg_path)
                with io.BytesIO() as output:
                    img.save(output, format="PNG")
                    output.seek(0)
                    await ctx.followup.send(file=File(output, "stats.png"))
            else:
                await ctx.followup.send(f"No stats found for {player_name}.")
        except Exception as e:
            await ctx.followup.send(f"An error occurred: {e}")

def setup(bot):
    bot.add_cog(RuneScapeRunemetricsCog(bot))
