import os
import random
import traceback

import asyncio
import disnake
from disnake.ext import commands

import utils.json_loader


class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="blacklist", description="Blacklist a user from the bot", usage="<user>"
    )
    @commands.is_owner()
    async def blacklist(self, ctx, user: disnake.Member):
        if ctx.message.author.id == user.id:
            await ctx.send("I do not support Drink and Type")
            return

        self.bot.blacklisted_users.append(user.id)
        data = utils.json_loader.read_json("blacklist")
        data["blacklistedUsers"].append(user.id)
        utils.json_loader.write_json(data, "blacklist")
        await ctx.reply(f"Alright, {user.name} was blacklisted from using this bot.", mention_author=False)

    @commands.command(
        name="unblacklist",
        description="Unblacklist a user from the bot",
        usage="<user>",
    )
    @commands.is_owner()
    async def unblacklist(self, ctx, user: disnake.Member):
        """
        Unblacklist someone from the bot
        """
        self.bot.blacklisted_users.remove(user.id)
        data = utils.json_loader.read_json("blacklist")
        data["blacklistedUsers"].remove(user.id)
        utils.json_loader.write_json(data, "blacklist")
        await ctx.reply(f"{user.name} was unblacklisted and can use the bot kudos.", mention_author=False)

    @commands.command(
        name="logout",
        aliases=["disconnect", "close", "stopbot"],
        description="Log the bot out of discord",
    )
    @commands.is_owner()
    async def logout(self, ctx):
        """
        If the user running the command owns the bot then this will disconnect the bot from Discord.
        """
        await ctx.send(f"Okay {ctx.author.mention}, Gideon signing off :wave:")
        await self.bot.logout()

    @commands.command(
        name='reload', description="Reload all/one of the bots cogs!"
    )
    @commands.is_owner()
    async def reload(self, ctx, cog=None):
        if not cog:
            # No cog, means we reload all cogs
            async with ctx.typing():
                embed = disnake.Embed(
                    title=":gear: Reloading all cogs",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cogs/"):
                    if ext.endswith(".py") and not ext.startswith("_"):
                        try:
                            self.bot.unload_extension(f"cogs.{ext[:-3]}")
                            self.bot.load_extension(f"cogs.{ext[:-3]}")
                            embed.add_field(
                                name=f"Reloaded cog - `{ext}`",
                                value='\uFEFF',
                                inline=False
                            )
                        except Exception as e:
                            embed.add_field(
                                name=f"Failed to reload cog - `{ext}`",
                                value=e,
                                inline=False
                            )
                        await asyncio.sleep(0.5)
                await ctx.reply(embed=embed, mention_author=False)
        else:
            # reload the specific cog
            async with ctx.typing():
                embed = disnake.Embed(
                    title=":gear: Carrying out the request",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog.lower()}.py"
                if not os.path.exists(f"./cogs/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"Failed to reload cog - `{ext}`",
                        value="This cog does not exist.",
                        inline=False
                    )

                elif ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.bot.unload_extension(f"cogs.{ext[:-3]}")
                        self.bot.load_extension(f"cogs.{ext[:-3]}")
                        embed.add_field(
                            name=f"Reloaded cog - `{ext}`",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f"Failed to reload cog - `{ext}`",
                            value=desired_trace,
                            inline=False
                        )
                await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(Config(bot))
