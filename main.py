  
import discord
from discord.ext import commands
import os
import random
import datetime

from discord.ext import commands

x = datetime.datetime.now()
y = x.strftime("%d")
client = commands.Bot(command_prefix=";")
token = os.getenv("ODY2OTg4Mzk5MDMzMzE5NDQ1.YPaj3g.NmIty0Y_Ku4Aavt4dH8PkICu9uc")

@client.event
async def on_ready() :

    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Working on myself"))
    print("Ready to Deploy")

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.channel.send(f'{member.mention} has been kicked.')

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.channel.send(f'{member.mention} has been banned.')

@client.command(name="pl")
async def pl(ctx):
    if ctx.author.id==760426797418151937:
        await ctx.send(f"Your fixes for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/847138145/-1/year2021_month07_day{y}.html")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount:int =10): 
    await ctx.channel.purge(limit=amount)

@client.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@client.command(name="invite")
async def invite(ctx) :
    await ctx.send(f"https://discord.com/api/oauth2/authorize?client_id=866988399033319445&permissions=8&scope=bot")

@client.event    
async def on_message(message):
    for x in message.mentions:
        if(x==client.user):
            await message.channel.send(f":sauropod: did someone mention me? My prefix is `;`")

    await client.process_commands(message)

client.run("ODY2OTg4Mzk5MDMzMzE5NDQ1.YPaj3g.NmIty0Y_Ku4Aavt4dH8PkICu9uc")


