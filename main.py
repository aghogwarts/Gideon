  
import discord
from discord.ext import commands
import os
import random

from discord.ext import commands

client = commands.Bot(command_prefix=";")
token = os.getenv("ODY2OTg4Mzk5MDMzMzE5NDQ1.YPaj3g.NmIty0Y_Ku4Aavt4dH8PkICu9uc")

@client.event
async def on_ready() :

    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Working on myself"))
    print("Ready to Deploy")

from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

@client.command(name="kick", pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def _kick(ctx, member: Member):
    await client.kick(member)

@_kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await client.send_message(ctx.message.channel, text)

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

@client.command(name="fixpl")
async def fix(ctx, user) :
    league= {pl, champ, league1, league2}
    if league= a
    await ctx.send()
    await ctx.send(f"Go here to see all the fixtures https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/-1/-1/-1.html")

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


