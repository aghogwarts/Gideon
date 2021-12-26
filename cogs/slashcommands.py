import disnake
from disnake.ext import commands

import random
from tabulate import tabulate

class SlashCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command(
        name="ping",
        description="Check the Bot Host's Latency"
    )
    async def ping(self,inter):
        await inter.response.send_message(f"{round(self.bot.latency * 1000, 2)}ms")


def setup(bot):
    bot.add_cog(SlashCommands(bot))