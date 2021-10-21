import asyncio
import platform
import random

import disnake
from disnake.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="say", description="A command to mimic what you said as if the bot has said it",
        usage="<string>"
    )
    async def say(self, ctx, *, message):
        await ctx.send(f"{message}")
        await ctx.message.delete()

    @commands.command(
        name="choose",
        description="Random choose between a list of options",
        usage="<choice 1> <choice 2>.. <choice n>"
    )
    async def choose(self, ctx, *choices: str):
        await ctx.reply(random.choice(choices), mention_author=False)

    # @commands.command(
    #     name="shuffle",
    #     description="Shuffle the order of words in a sequence",
    #     usage="<word1>, <word2>.. <wordn>"
    # )
    # async def shuffle(self, ctx, *, choices: str):
    #     choices = list(choices)
    #     await ctx.reply(random.shuffle(choices))

    @commands.command(
        name="info", description="General information about the Bot"
    )
    async def info(self, ctx):
        infoEmbed = disnake.Embed(
            description="```fix\nSome info about this Bot```\nA simple multipurpose bot with quite some unique features programmed by <@760426797418151937>.\nI was originally made for a private server\n\n**Contributors -**\n<@807655087643557919>\n[Invite Me](https://discord.com/api/oauth2/authorize?client_id=866988399033319445&permissions=532844768326&scope=applications.commands%20bot)\n[View my Documentation](https://workinprogress.com)",
            color = random.choice(self.bot.color_list)
        )
        infoEmbed.set_footer(icon_url=ctx.message.author.avatar.url, text="Hope you enjoy using this bot :p")
        await ctx.reply(embed=infoEmbed, mention_author=False)

    @commands.command(
        name="stats", description="A command to displays bot statistics."
    )
    async def stats(self, ctx):
        pythonVersion = platform.python_version()
        disnakeVersion = disnake.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        embed = disnake.Embed(
            title=f"Bot Statistics",
            description="\uFEFF",
            colour=random.choice(self.bot.color_list),
            timestamp=ctx.message.created_at,
        )

        embed.add_field(name="Bot Version:", value=self.bot.version)
        embed.add_field(name="Python Version:", value=pythonVersion)
        embed.add_field(name="disnake Version", value=disnakeVersion)
        embed.add_field(name="Total Guilds:", value=serverCount)
        embed.add_field(name="Total Users:", value=memberCount)
        embed.add_field(name="Bot Developers:", value="<@760426797418151937>")

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        name="toggle",
        description="Enable or disable a command!",
        usage="<command>"
    )
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.bot.get_command(command)

        if command is None:
            await ctx.send("Lol, sure you've typed an actual command ?")

        elif ctx.command == command:
            await ctx.send("You cannot disable this command.")

        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            await ctx.send(f"Nice {command.qualified_name} is {ternary} for everyone now")


def setup(bot):
    bot.add_cog(Misc(bot))
