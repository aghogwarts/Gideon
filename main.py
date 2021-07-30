  
import discord
from discord import message
from discord.ext import commands
import os, time
import random
import datetime
import mysql.connector

class TZ1(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=1)
    def dst(self, dt):
        return datetime.timedelta(hours=1)

y = datetime.datetime.now(tz=TZ1()).strftime("%d")    

client = commands.Bot(command_prefix=";")
token = os.getenv("ODY2OTg4Mzk5MDMzMzE5NDQ1.YPaj3g.NmIty0Y_Ku4Aavt4dH8PkICu9uc")

mydb = mysql.connector.connect(
  host="bh002.bluefoxhost.com",
  user="u333_q34vaVFrPW",
  password="3P.zWdY2Y.VKCFnWVsRJJ=XV",
  database="s333_PlayersDB"
)

@client.command(name="search")
async def search(ctx, player):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM `TABLE 1` WHERE Name Like %s"
    val = (f"%{player}%",)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for player in myresult:
        await ctx.send(f"Name: `{player[0]}` Rating: `{player[1]}` Position: `{player[2]}` Version: `{player[3]}` Base Stats : `{player[4]}`")

@client.event
async def on_ready() :

    await client.change_presence(status = discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.listening, name=";help or @Gideon"))
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
    if ctx.author.id==760426797418151937 or 755085116593799198: #onlyme
        await ctx.send(f"{message}")
        await ctx.message.delete()
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

league = {760426797418151937:847138145, #ag
  755085116593799198:855960929, #hima
  755367944921415750:874662484, #azpi
  806189281227046912:350067379, #brendan
  275711910371000331:64612278, #cooper
  263480873763078144:95774044, #pop
  145561425828511745:362698291, #drax
  761850692453269505:126712691, #kiddo
  735519422751571978:438789510, #gintoki
  382228200601944064:981194343, #goodbye
  713023867764998202:765150342, #havok
  415130032541925377:842998859, #imp
  585479151344025622:956829629, #jalli
  755368781047529642:123407488, #jerwin
  549210192076603407:494516009, #joey
  565292861222944769:708714348, #damnboy
  508023836432662540:132800515, #kaapo
  604657414649806849:197671480, #marius
  468208884960722955:985152495, #mast
  688458544768614469:192906840, #matt
  748781920241844275:262950827, #mike
  196656994751348747:808850355, #kip
  428955457089175552:615861616, #okkotsu
  533970200391974943:113807326, #pacy
  318699230229168129:291850130, #percy
  433462493445095424:20883841, #rainbow
  243744198136823809:601237630, #saif
  596593097975005203:889925791, #froge
  849887001221529610:738549919, #tess
  633848471316594699:768996681, #eagle
  333553900567134210:432503448, #tim
  407959232235700225:394188955, #war
  703119075198369874:833720351, #weg
  764965814650011658:833034179, #damian
  286604631042162688:977816272, #dziri
  398980616991014913:124009093, #filkaaa
  776253321560195113:754751886, #gaem
  546842211296215060:299703658, #insanitytp
  243101227087429632:45973977, #kev
  255979673211633666:184670283, #kool
  588368406865248286:545658181, #munt
  427432148975484928:741552408, #noder
  797435614886363176:583463860, #omar
  467733724394422274:42517100, #ssom
  265590018779774976:232121659, #tbf
  202162967045734401:721203021 #vuto
  }
@client.command(name="fix", description="A command to show your fixtures for today. Note - The link won't work if your day's fixtures are done")
async def fix(ctx):
    """See your Futbot League's fixtures for today"""
    if ctx.author.id in league.keys():
        await ctx.send(f"All Leagues are done <:pepebusiness:859047053413974026>. Come back when the leagues start again.. That's August 2")
    else:
        return

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error- `{error}` Try ;help')

@client.command(name="sheet", description="Link to a google sheet to guide you through the best combos possible in Soccer Guru")
async def sheet(ctx):
    """Best possible Combos in a SG Team"""
    await ctx.send(f"Google Sheet Link :- https://docs.google.com/spreadsheets/d/1QjsLi1wpdLFeJuNhx-hFg_Lw-FDz2dcQnR3gbygXB3A/edit?usp=sharing")

@client.event    
async def on_message(message):
    for x in message.mentions:
        if(x==client.user):
            await message.channel.send(f"<:frogeez:833600103939571734> Did someone mention me? My prefix is `;`and you can do `;help` to see a list of commands though there aren't many atm")

    await client.process_commands(message)

client.run("ODY2OTg4Mzk5MDMzMzE5NDQ1.YPaj3g.NmIty0Y_Ku4Aavt4dH8PkICu9uc")


