import discord
from discord.ext import commands
import os

from discord.ext.commands import bot

client = commands.Bot(command_prefix=when_mentioned_or("."))
token = os.getenv("Token")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("Ready to Deploy")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=10) :
    await ctx.channel.purge(limit=amount)

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send("Hey do !fix Premier League to see your fixes for the day")
        
    await bot.process_commands(message)    
    
client.run("Token")
