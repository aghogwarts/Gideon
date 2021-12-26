from main import DEFAULTPREFIX
import re
import math
import random

import disnake
from disnake.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='help', aliases=['commands'], description="The generic help command"
    )
    async def help(self, ctx, cog="1"):
        helpEmbed = disnake.Embed(
            title="Help - Command List to help you :)", color=random.choice(self.bot.color_list),

        )
        # helpEmbed.set_thumbnail(url=self.bot.user.avatar.url)

        # Get a list of all our current cogs & remove ones without commands
        cogs = [c for c in self.bot.cogs.keys()]
        cogs.remove('Gsheets')
        cogs.remove('SlashCommands')
        cogs.remove('SlashHelp')

        totalPages = math.ceil(len(cogs) / 4)

        if re.search(r"\d", str(cog)):
            cog = int(cog)
            if cog > totalPages or cog < 1:
                await ctx.reply(f"Invalid page number `{cog}`. Pick from {totalPages} pages, or just do `;help` to see a list of all commands.", mention_author=False, delete_after=10)
                return

            helpEmbed.set_footer(
                text=f"Requested by {ctx.author.name} | Page {cog} of {totalPages}",
                icon_url=self.bot.user.avatar.url
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

                    commandList += f"`{command.name}`,"  # - {command.description}\n
                commandList += "\n"

                helpEmbed.description=f"```fix\nDo {DEFAULTPREFIX}help <category> to see more info about a Category of commands```"
                helpEmbed.add_field(name=cog, value=commandList, inline=False)

        elif re.search(r"[a-zA-Z]", str(cog)):
            lowerCogs = [c.lower() for c in cogs]
            if cog.lower() not in lowerCogs:
                await ctx.reply(f"Invalid Category name. Run `help` to see the whole list of commands.", mention_author=False, delete_after=10)
                return

            helpEmbed.set_footer(
                text=f"Requested by {ctx.author.name} | Category {(lowerCogs.index(cog.lower())+1)} of {len(lowerCogs)}",
                icon_url=self.bot.user.avatar.url
            )

            helpText = ""

            for command in self.bot.get_cog(cogs[lowerCogs.index(cog.lower())]).walk_commands():
                if command.hidden:
                    continue

                elif command.parent != None:
                    continue

                helpText += f"✎ `{command.name}`\n{command.description}"

                if len(command.aliases) > 0:
                    helpText += f'\n**Aliases: ** `{", ".join(command.aliases)}`'
                helpText += '\n'

                prefix = DEFAULTPREFIX

                helpText += f'**Format:** `{prefix}{command.name} {command.usage if command.usage is not None else ""}`\n\n'
            helpEmbed.description=f"```fix\nCommand arguments - <required> [optional]```\n{helpText}"

        else:
            await ctx.reply(f"Invalid Page or Category name. Run `help` to see the whole list of commands.", mention_author=False, delete_after=10)
            return

        await ctx.reply(embed=helpEmbed, mention_author=False)


def setup(bot):
    bot.add_cog(Help(bot))
