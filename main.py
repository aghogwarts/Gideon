  
import discord
from discord.ext import commands
import os, time
import random
import datetime

from discord.ext import commands

class TZ1(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=1)
    def dst(self, dt):
        return datetime.timedelta(hours=1)

y = datetime.datetime.now(tz=TZ1()).strftime("%d")    

client = commands.Bot(command_prefix=";")
token = os.getenv("ODY2OTg4Mzk5MDMzMzE5NDQ1.YPaj3g.NmIty0Y_Ku4Aavt4dH8PkICu9uc")

@client.event
async def on_ready() :

    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Working on myself"))
    print("Ready to Deploy")

@client.command(name="test")
async def test(ctx):
    """Testing command dev only"""
    if ctx.author.id==760426797418151937: #only me
        await ctx.send(f"Date is {y}")
    else:
        return    

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

@client.command()
async def say(ctx,*,message):
    """Dev only atm due to spam"""
    if ctx.author.id==760426797418151937: #onlyme
        await ctx.send(f"{message}")
        await ctx.message.delete()
    else:
        return    

@client.command(name="fix", description="A command to show your fixtures for today. Note - The link won't work if your day's fixtures are done")
async def fix(ctx):
    """See your Futbot League's fixtures for today"""
    if ctx.author.id==760426797418151937: #ag
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/847138145/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==755085116593799198: #hima
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/855960929/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==755367944921415750: #azpi
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/874662484/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==478610182625034243: #amit
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/207226768/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==806189281227046912: #brendan
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/350067379/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==275711910371000331: #cooper
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/64612278/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==263480873763078144: #pop
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/95774044/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==145561425828511745: #drax
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/362698291/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==761850692453269505: #kiddo
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/126712691/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==735519422751571978: #gintoki
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/438789510/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==382228200601944064: #goodbye
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/981194343/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==713023867764998202: #havok
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/765150342/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==415130032541925377: #imp
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/842998859/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==585479151344025622: #jalli
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/956829629/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==755368781047529642: #jerwin
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/123407488/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==549210192076603407: #joey
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/494516009/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==842723531073519619: #josiah
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/708714348/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==508023836432662540: #kaapo
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/132800515/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==173014215680983040: #kaki
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/900151105/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==604657414649806849: #marius
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/197671480/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==468208884960722955: #mast
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/985152495/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==688458544768614469: #matt
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/192906840/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==748781920241844275: #mike
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/262950827/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==196656994751348747: #kip
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/808850355/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==428955457089175552: #okkotsu
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/615861616/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==533970200391974943: #pacy
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/113807326/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==318699230229168129: #percy
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/291850130/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==433462493445095424: #rainbow
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/20883841/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==243744198136823809: #saif
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/601237630/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==596593097975005203: #froge
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/889925791/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==849887001221529610: #tess
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/738549919/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==633848471316594699: #eagle
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/768996681/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==333553900567134210: #tim
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/432503448/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==407959232235700225: #war
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/394188955/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==703119075198369874: #weg
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/833720351/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==764965814650011658: #damian
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/833034179/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==286604631042162688: #dziri
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/977816272/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==398980616991014913: #filkaaa
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/124009093/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==776253321560195113: #gaem
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/754751886/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==546842211296215060: #insantitytp
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/299703658/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==243101227087429632: #kev
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/45973977/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==255979673211633666: #kool
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/184670283/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==588368406865248286: #munt
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/545658181/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==427432148975484928: #noder
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/741552408/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==797435614886363176: #omar
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/583463860/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==467733724394422274: #ssom
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/42517100/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==265590018779774976: #tbf
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/232121659/-1/year2021_month07_day{y}.html")
    elif ctx.author.id==202162967045734401: #vuto
        await ctx.send(f"Your fixtures for the day are https://futbotleagues.leaguerepublic.com/matches/229039714/-1_-1/721203021/-1/year2021_month07_day{y}.html")
    else:
        return

@client.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@client.command(name="invite")
async def invite(ctx) :
    """Bot invite, pretty useless cause this bot is private atm"""
    await ctx.send(f"https://discord.com/api/oauth2/authorize?client_id=866988399033319445&permissions=8&scope=bot")

@client.event    
async def on_message(message):
    for x in message.mentions:
        if(x==client.user):
            await message.channel.send(f"<:frogeez:833600103939571734> Did someone mention me? My prefix is `;`and you can do `;help` to see a list of commands though there aren't many atm")

    await client.process_commands(message)

client.run("ODY2OTg4Mzk5MDMzMzE5NDQ1.YPaj3g.NmIty0Y_Ku4Aavt4dH8PkICu9uc")


