import config
import openai
import json
from urllib.parse import quote
from discord.ext import commands
from utils.rs3_utils import get_player_stats

class OpenAiAskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        openai.api_key = config.OPENAI_API_KEY

    @commands.slash_command(name="ask", description="Ask the bot a question")
    async def ask(self, ctx, user_input: str, player_name: str = None):
        await ctx.defer()

        messages = [
            {
                "role": "system",
                "content": "You are an AI-powered assistant bot specifically designed to help clan members with every aspect of RuneScape 3. Utilize your knowledge and understanding of the game to provide accurate information, suggestions, and support for various in-game activities such as leveling, questing, bossing, and skilling. Be friendly, engaging, and helpful to all users.  Assume every user query relates to the game RuneScape 3 by Jagex.  The XP of each skill needs to be divided by 10."
            }
        ]

        if player_name:
            stats = get_player_stats(player_name)
            if stats:
                user_message = f"The user's stats: " + ", ".join([f"{stat['skillname']}: L{stat['level']} (XP {stat['xp']})" for stat in stats])
                messages.append({"role": "system", "content": user_message})
            else:
                print("Error fetching player stats")
        messages.append({"role": "user", "content": user_input})
         
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = response['choices'][0]['message']['content']
        await ctx.followup.send(answer)

def setup(bot):
    bot.add_cog(OpenAiAskCog(bot))
