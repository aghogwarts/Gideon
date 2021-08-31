from main import DEFAULTPREFIX
import re
import math
import random

import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='help', aliases=['h', 'commands'], description="The help command!"
    )
    async def help(self, ctx, cog="1"):
        helpEmbed = discord.Embed(
            title="Command List to help you ;)", color=random.choice(self.bot.color_list)
        )
        helpEmbed.set_thumbnail(url=self.bot.user.avatar_url)

        # Get a list of all our current cogs & rmeove ones without commands
        cogs = [c for c in self.bot.cogs.keys()]

        totalPages = math.ceil(len(cogs) / 4)

        if re.search(r"\d", str(cog)):
            cog = int(cog)
            if cog > totalPages or cog < 1:
                await ctx.send(f"Invalid page number: `{cog}`. Pick from {totalPages} pages, or just do `;help` to see a list of all commands.")
                return

            helpEmbed.set_footer(
                text=f"Requested by {ctx.author.name} | Page {cog} of {totalPages}"
            )

            neededCogs = []
            for i in range(4):
                x = i + (int(cog) - 1) * 4
                try:
                    neededCogs.append(cogs[x])
                except IndexError:
                    pass

            for cog in neededCogs:
                commandList = ""
                for command in self.bot.get_cog(cog).walk_commands():
                    if command.hidden:
                        continue

                    elif command.parent != None:
                        continue

                    commandList += f"`{command.name}` - {command.description}\n"
                commandList += "\n"

                helpEmbed.add_field(name=cog, value=commandList, inline=False)

        elif re.search(r"[a-zA-Z]", str(cog)):
            lowerCogs = [c.lower() for c in cogs]
            if cog.lower() not in lowerCogs:
                await ctx.send(f"Invalid Page: `{cog}`\nPick from {totalPages} pages or run `help` to see the whole list of commands.")
                return

            helpEmbed.set_footer(
                text=f"Requested by {ctx.author.name} | Category {(lowerCogs.index(cog.lower())+1)} of {len(lowerCogs)}"
            )

            helpText = ""

            for command in self.bot.get_cog(cogs[lowerCogs.index(cog.lower())]).walk_commands():
                if command.hidden:
                    continue

                elif command.parent != None:
                    continue

                helpText += f"`{command.name}`\n✎ {command.description}"

                if len(command.aliases) > 0:
                    helpText += f'\n**Aliases: ** `{", ".join(command.aliases)}`'
                helpText += '\n'

                prefix = DEFAULTPREFIX

                helpText += f'**Format:** `{prefix}{command.name} {command.usage if command.usage is not None else ""}`\n\n'
            helpEmbed.description=f"```fix\nChal gaya gandu```\n{helpText}"

        else:
            await ctx.reply(f"Invalid Page: `{cog}`\nPick from {totalPages} pages or run `help` to see the whole list of commands.", mention_author=False)
            return

        await ctx.reply(embed=helpEmbed, mention_author=False)


def setup(bot):
    bot.add_cog(Help(bot))