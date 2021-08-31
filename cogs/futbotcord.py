import random
import asyncio
import os
import mysql.connector

from tabulate import tabulate

import discord
from discord.ext import commands

mydb = mysql.connector.connect(
    host="bh002.bluefoxhost.com",
    user="u333_q34vaVFrPW",
    password="3P.zWdY2Y.VKCFnWVsRJJ=XV",
    database="s333_PlayersDB"
)

league = {
  755367944921415750:874662484,  #azpi
  806189281227046912:350067379,  #brendan
  275711910371000331:64612278,  #cooper
  263480873763078144:95774044,  #pop
  145561425828511745:362698291,  #drax
  761850692453269505:126712691,  #kiddo
  735519422751571978:438789510,  #gintoki
  382228200601944064:981194343,  #goodbye
  713023867764998202:765150342,  #havok
  415130032541925377:842998859,  #imp
  585479151344025622:956829629,  #jalli
  755368781047529642:123407488,  #jerwin
  549210192076603407:494516009,  #joey
  565292861222944769:490519574,  #damnboy
  508023836432662540:132800515,  #kaapo
  604657414649806849:197671480,  #marius
  468208884960722955:985152495,  #mast
  688458544768614469:192906840,  #matt
  748781920241844275:262950827,  #mike
  196656994751348747:808850355,  #kip
  428955457089175552:615861616,  #okkotsu
  533970200391974943:113807326,  #pacy
  318699230229168129:291850130,  #percy
  433462493445095424:20883841,  #rainbow
  243744198136823809:601237630,  #saif
  596593097975005203:889925791,  #froge
  849887001221529610:738549919,  #tess
  633848471316594699:768996681,  #eagle
  333553900567134210:432503448,  #tim
  407959232235700225:394188955,  #war
  703119075198369874:833720351,  #weg
  764965814650011658:833034179,  #damian
  286604631042162688:977816272,  #dziri
  398980616991014913:124009093,  #filkaaa
  776253321560195113:754751886,  #gaem
  546842211296215060:299703658,  #insanitytp
  243101227087429632:45973977,  #kev
  255979673211633666:184670283,  #kool
  588368406865248286:545658181,  #munt
  427432148975484928:741552408,  #noder
  797435614886363176:583463860,  #omar
  467733724394422274:42517100,  #ssom
  265590018779774976:232121659,  #tbf
  202162967045734401:721203021,  #vuto
  753800755466469418:520410434,  #derek
  776191549154656279:904839252,  #mack
  850472365853769728:905473283,  #klichbait
}

class Futbotcord(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="fix", description="See your Futbotcord League fixture for today"
    )
    async def fix(self, ctx):
        if ctx.author.id in league.keys():
            embed = discord.Embed(
                description=f"[Click here](https://futbotleagues.leaguerepublic.com/matches/342846686/-1_-1/{league[ctx.author.id]}/-1/year2021_month08_day31.html) to see your League fixtures for today ```fix\nNote: site won't work or load if all of your fixes are done```",
                color=random.choice(self.bot.color_list)
            )
            embed.set_footer(icon_url=ctx.message.author.avatar_url, text="Good luck for the Leagues")
            await ctx.reply(embed=embed, mention_author=False)
        else:
            return

    @commands.command(
        name="sheet", description="Link to a sheet to guide your SG XI making"
    )
    async def sheet(self, ctx):
        embed = discord.Embed(
            description="[Click here](https://docs.google.com/spreadsheets/d/1QjsLi1wpdLFeJuNhx-hFg_Lw-FDz2dcQnR3gbygXB3A/edit?usp=sharing) to see a sheet comprising the best SGBot combos in the game ```fix\nYes the sheet is a bit unupdated, it will be updated soon```",
            color=random.choice(self.bot.color_list)
        )
        embed.set_footer(icon_url=ctx.message.author.avatar_url, text="Good luck making your XI")
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        name="search", description="A command to find details of any FUT Player from the Player Database", usage="<playername>"
    )
    async def search(self, ctx, *, player):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM FUTData WHERE Name Like %s LIMIT 10"
        val = (f"%{player}%",)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print(val)
        table = []
        headers = ["Name", "RAT", "POS", "VER", "BS"]
        embed = discord.Embed(colour=discord.Colour(0xbde31), description="")
        for player in myresult:
            data = [player[0][:25], player[1], player[2], player[3][:12], player[10]]
            table.append(data)
            output = tabulate(table, headers, tablefmt="pretty", colalign=("left", "center", "center", "left",))
        embed.description = f"```\n{output}```"
        embed.set_footer(text="Player lookup")
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        name="find", description="A command to find stats of any Cricket Guru Player 90+(atm) from the Player Database created by me", usage="<name> <type>"
    )
    async def find(self, ctx, rating, type):
        """Find any Cricket Guru Player from the Database"""
        mycursor = mydb.cursor()
        if type == "wk":
            sql = "SELECT * FROM WicketKeepers WHERE RAT Like %s LIMIT 10"
            val = (f"%{rating}%",)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            print(val)
            for rating in myresult:
                await ctx.send(
                    f"Name: `{rating[1]}` Nation: {rating[2]} RAT: `{rating[3]}` BAT: `{rating[4]}` BOWL: `{rating[5]}` {rating[6]} Price: `{rating[7]}`")
        elif type == "bat":
            sql = "SELECT * FROM Batsmen WHERE RAT Like %s LIMIT 10"
            val = (f"%{rating}%",)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            print(val)
            for rating in myresult:
                await ctx.send(
                    f"Name: `{rating[1]}` Nation: {rating[2]} RAT: `{rating[3]}` BAT: `{rating[4]}` BOWL: `{rating[5]}` {rating[6]} Price: `{rating[7]}`")
        elif type == "alr":
            sql = "SELECT * FROM AllRounders WHERE RAT Like %s LIMIT 10"
            val = (f"%{rating}%",)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            print(val)
            for rating in myresult:
                await ctx.send(
                    f"Name: `{rating[1]}` Nation: {rating[2]} RAT: `{rating[3]}` BAT: `{rating[4]}` BOWL: `{rating[5]}` {rating[6]} {rating[7]} Price: `{rating[8]}`")
        elif type == "bowl":
            sql = "SELECT * FROM Bowlers WHERE RAT Like %s LIMIT 10"
            val = (f"%{rating}%",)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            print(val)
            for rating in myresult:
                await ctx.send(
                    f"Name: `{rating[1]}` Nation: {rating[2]} RAT: `{rating[3]}` BAT: `{rating[4]}` BOWL: `{rating[5]}` {rating[6]} Price: `{rating[7]}`")
        else:
            return

def setup(bot):
    bot.add_cog(Futbotcord(bot))