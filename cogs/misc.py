import asyncio
import platform
import random

import disnake
from disnake.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="say", description="A command to repeat what you said but restricted to the dev for now"
    )
    async def say(self, ctx, *, message):
        if ctx.author.id in (760426797418151937, 755085116593799198):  #onlyme
            await ctx.send(f"{message}")
            await ctx.message.delete()
        else:
            return

    @commands.command(
        name="choose",
        description='For when you wanna settle the score some other way',
        usage="<choice 1> <choice 2>.. <choice n>"
    )
    async def choose(self, ctx, *choices: str):
        await ctx.reply(random.choice(choices), mention_author=False)

    @commands.command(
        name="info", description="General information about the Bot"
    )
    async def info(self, ctx):
        infoEmbed = disnake.Embed(
            description="```fix\nAdditional info about this Bot```\n[Invite Me](https://discord.com/api/oauth2/authorize?client_id=866988399033319445&permissions=532844768326&scope=applications.commands%20bot)\n[View my Documentation](https://workinprogress.com)\n<> indicates an required argument\n[] indicates an optional argument",
            color = random.choice(self.bot.color_list)
        )
        infoEmbed.set_footer(icon_url=ctx.message.author.avatar.url, text="Hope you enjoy using this bot :p")
        await ctx.reply(embed=infoEmbed, mention_author=False)

    @commands.command(
        name="stats", description="A useful command that displays bot statistics."
    )
    async def stats(self, ctx):
        pythonVersion = platform.python_version()
        disnakeVersion = disnake.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        embed = disnake.Embed(
            title=f"{self.bot.user.name} Stats",
            description="\uFEFF",
            colour=random.choice(self.bot.color_list),
            timestamp=ctx.message.created_at,
        )

        embed.add_field(name="Bot Version:", value=self.bot.version)
        embed.add_field(name="Python Version:", value=pythonVersion)
        embed.add_field(name="disnake.Py Version", value=disnakeVersion)
        embed.add_field(name="Total Guilds:", value=serverCount)
        embed.add_field(name="Total Users:", value=memberCount)
        embed.add_field(name="Bot Developers:", value="<@760426797418151937>")

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(name="toggle", description="Enable or disable a command!")
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
