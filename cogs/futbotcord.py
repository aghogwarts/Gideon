import random
import asyncio
import os

from tabulate import tabulate

import disnake
from disnake.ext import commands

from pymongo import MongoClient

myclient = MongoClient("mongodb+srv://ag_discordbot:xxAGxx22@cluster0.gbn7p.mongodb.net/Gideon?retryWrites=true&w=majority")
mydb = myclient["Gideon"]
futdb = mydb["FUTData"]
batdb = mydb["Batsmen"]
bowldb = mydb["Bowlers"]
wkdb = mydb["Keepers"]
alrdb = mydb["AllRounders"]

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
            embed = disnake.Embed(
                description=f"[Click here](https://futbotleagues.leaguerepublic.com/matches/342846686/-1_-1/{league[ctx.author.id]}/-1/year2021_month09_day21.html) to see your League fixtures for today ```fix\nNote: site won't work or load if all of your fixes are done\nHeard Leagues have been stopped for the moment tho```",
                color=random.choice(self.bot.color_list)
            )
            embed.set_footer(icon_url=self.bot.user.avatar.url, text="Good luck for the Leagues")
            await ctx.reply(embed=embed, mention_author=False)
        else:
            return

    @commands.command(
        name="sheet", description="Link to a sheet to guide your SG XI making"
    )
    async def sheet(self, ctx):
        embed = disnake.Embed(
            description="[Click here](https://docs.google.com/spreadsheets/d/1QjsLi1wpdLFeJuNhx-hFg_Lw-FDz2dcQnR3gbygXB3A/edit?usp=sharing) to see a sheet comprising the best SGBot combos in the game ```fix\nYes, the sheet is unupdated and I do not plan to update it as FIFA 21 Season is almost at an end```",
            color=random.choice(self.bot.color_list)
        )
        embed.set_footer(icon_url=ctx.message.author.avatar.url, text="Good luck making your XI")
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        name="search", description="A command to find details of any FUT Player from the Player Database", usage="<playername>"
    )
    async def search(self, ctx, *, player):
        print({player})
        player_info = list()
        headers = ["Name", "RAT", "POS", "VER", "BS"]
        embed = disnake.Embed(colour=random.choice(self.bot.color_list), description="")
        myquery = { "Name": {"$regex": f"{player}", "$options": "i"}}
        filters = { "_id": 0, "Name": 1, "RAT": 1, "POS": 1, "VER": 1, "BS": 1}
        for player in futdb.find(myquery, filters).sort("BS", -1).limit(10):
            player_result = list()
            player_result.append(player['Name'][:25])
            player_result.append(player['RAT'])
            player_result.append(player['POS'])
            player_result.append(player['VER'][:12])
            player_result.append(player['BS'])
            player_info.append(player_result)
            output = tabulate(player_info, headers, tablefmt="pretty", colalign=("left", "center", "center", "left",))
        embed.description = f"```\n{output}```"
        embed.set_footer(icon_url=ctx.message.author.avatar.url, text="Player lookup")
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        name="find", description="Find players and their stats from the CG Player Database (90+ only atm)", usage="<rating> <type>"
    )
    async def find(self, ctx, rating: int, style: str):
        style = style.lower()
        if style == "wk":
            myquery = {"RAT": rating}
            filters = {"_id": 0, "Name": 1, "Nation": 1, "RAT": 1, "BAT": 1, "BOWL": 1, "Type": 1, "Price": 1}
            result = ""
            embed = disnake.Embed(colour=random.choice(self.bot.color_list), title="Wicket-Keepers :gloves:", description="")
            for rating in wkdb.find(myquery, filters).sort("BAT", -1):
                player = list()
                player.append(rating['Name'])
                player.append(rating['Nation'])
                player.append(rating['RAT'])
                player.append(rating['BAT'])
                player.append(rating['BOWL'])
                player.append(rating['Type'])
                player.append(rating['Price'])
                result += f"`{player[0]}` {player[1]} OVR: `{player[2]}` BAT: `{player[3]}` BOWL: `{player[4]}` Price: `{player[6]}`\n"  # {player[5]} for type
            embed.description = result
            await ctx.reply(embed=embed, mention_author=False)
        elif style == "bat":
            myquery = {"RAT": rating}
            filters = {"_id": 0, "Name": 1, "Nation": 1, "RAT": 1, "BAT": 1, "BOWL": 1, "Type": 1, "Price": 1}
            result = ""
            embed = disnake.Embed(colour=random.choice(self.bot.color_list), title="Batsmen <:cbat:874867863264055356>", description="")
            for rating in batdb.find(myquery, filters).sort("BAT", -1):
                player = list()
                player.append(rating['Name'])
                player.append(rating['Nation'])
                player.append(rating['RAT'])
                player.append(rating['BAT'])
                player.append(rating['BOWL'])
                player.append(rating['Type'])
                player.append(rating['Price'])
                result += f"`{player[0]}` {player[1]} OVR: `{player[2]}` BAT: `{player[3]}` BOWL: `{player[4]}` Price: `{player[6]}`\n"  # {player[5]}
            embed.description = result
            await ctx.reply(embed=embed, mention_author=False)
        elif style == "bowl":
            myquery = {"RAT": rating}
            filters = {"_id": 0, "Name": 1, "Nation": 1, "RAT": 1, "BAT": 1, "BOWL": 1, "Style": 1, "Price": 1}
            result = ""
            embed = disnake.Embed(colour=random.choice(self.bot.color_list), title="Bowlers <:cball:874869772058238986>", description="")
            for rating in bowldb.find(myquery, filters).sort("BOWL", -1):
                player = list()
                player.append(rating['Name'])
                player.append(rating['Nation'])
                player.append(rating['RAT'])
                player.append(rating['BAT'])
                player.append(rating['BOWL'])
                player.append(rating['Style'])
                player.append(rating['Price'])
                result += f"`{player[0]}` {player[1]} OVR: `{player[2]}` BAT: `{player[3]}` BOWL: `{player[4]}` {player[5]} Price: `{player[6]}`\n"
            embed.description = result
            await ctx.reply(embed=embed, mention_author=False)
        elif style == "alr":
            myquery = {"RAT": rating}
            filters = {"_id": 0, "Name": 1, "Nation": 1, "RAT": 1, "BAT": 1, "BOWL": 1, "Type": 1, "Style": 1, "Price": 1}
            result = ""
            embed = disnake.Embed(colour=random.choice(self.bot.color_list), title="All-Rounders :cricket-game:", description="")
            for rating in alrdb.find(myquery, filters):
                player = list()
                player.append(rating['Name'])
                player.append(rating['Nation'])
                player.append(rating['RAT'])
                player.append(rating['BAT'])
                player.append(rating['BOWL'])
                player.append(rating['Type'])
                player.append(rating['Style'])
                player.append(rating['Price'])
                result += f"`{player[0]}` {player[1]} OVR: `{player[2]}` BAT: `{player[3]}` BOWL: `{player[4]}` {player[6]} Price: `{player[7]}`\n"  # {player[5]}
            embed.description = result
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply("Please enter a valid type ALR/WK/BAT/BOWL", mention_author=True, delete_after=15)

def setup(bot):
    bot.add_cog(Futbotcord(bot))