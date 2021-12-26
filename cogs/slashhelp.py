import random
import disnake
from disnake.ext import commands
 

class SlashHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    @commands.slash_command(
        name="help",
        description="Get a list of commands in the bot.",
    )
    async def _help(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title="Gideon Help", color=random.choice(self.bot.color_list))
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        description = ""
        for cog in self.bot.cogs.values():
            for command in cog.__cog_app_commands__:
                description += "`/" + command.name
                for option in command.options:
                    if option.required:
                        description += f" <{option.name}>"
                    else:
                        description += f" [{option.name}]"
 
                description += f"` - {command.description}\n"
        embed.description = description
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(SlashHelp(bot))