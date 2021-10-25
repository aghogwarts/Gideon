import disnake
from disnake.ext import commands
from disnake.ext.commands import param

from tabulate import tabulate
import asyncio
import random

from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'cogs/sheetsapi.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1gFjDHVB27FZPsIK1PHF_S4Dex4HklKJrSxkp6-ZmLhc'

service = build('sheets', 'v4', credentials=credentials)

# Call the Sheets API
sheet = service.spreadsheets()

# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="Sheet1!B2:C4").execute()
# values = result.get('values', [])

Predictors=["ansh", "hima", "gorkhali", "ssom", "amit", "spahash", "jerwin", "froge"]

async def autocomp_users(inter, user_input: str):
    return [pred for pred in Predictors if user_input.lower() in pred]

Positions=["forward", "midfield", "defence", "goalie"]

async def autocomp_postn(inter, user_input: str):
    return [postn for postn in Positions if user_input.lower() in postn]

current_gw = "GW 10"

user_cells={
    "ansh":"C5",
    "hima":"C6",
    "gorkhali":"C7",
    "ssom":"C8",
    "amit":"C9",
    "spahash":"C10",
    "jerwin":"C11",
    "froge":"C12",
}

pos_cells={
    "forward":"C5",
    "midfield":"D5",
    "defence":"E5",
    "goalie":"F5",
}

ind_user={
    "ansh":"5",
    "hima":"6",
    "gorkhali":"7",
    "ssom":"8",
    "amit":"9",
    "spahash":"10",
    "jerwin":"11",
    "froge":"12",
}

ind_pos={
    "forward":"C",
    "midfield":"D",
    "defence":"E",
    "goalie":"F",
}

class Gsheets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        guild_ids=[772179896097177631]
    )
    async def picks(self, inter):
        pass

    @picks.sub_command(
        name="user",
        description="Update prediction picks of a user"
    )
    async def picks_user(
        self,
        inter,
        user: str = param(desc="Choose the user who's picks are to be updated", autocomp=autocomp_users),
        forward: str = param(desc="Enter the name of the Forward"),
        midfielder: str = param(desc="Enter the name of the Midfielder"),
        defender: str = param(desc="Enter the name of the Defender"),
        goalie: str = param(desc="Enter the name of the Goalkeeper")
    ):
        if inter.author.id in (760426797418151937, 755085116593799198):
            picks = [[forward, midfielder, defender, goalie]]
            request = sheet.values().update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=f"{current_gw}!{user_cells[user]}",
                valueInputOption="USER_ENTERED",
                body={"values":picks}
            ).execute()
            await inter.response.send_message(f"Updated picks for `{user}`: `{forward}`,`{midfielder}`,`{defender}`,`{goalie}`\n```{request}```")
            await asyncio.sleep(20)
            await inter.delete_original_message()
        else:
            await inter.response.send_message("Sorry, you don't have access to this command :jayshreeram:", ephemeral=True)

    @picks.sub_command(
        name="postn",
        description="Update prediction picks of a position for all the users"
    )
    async def picks_postn(
        self,
        inter,
        position: str = param(desc="Choose the position whose picks are to be updated for multiple users", autocomp=autocomp_postn),
        ansh: str = param(None, desc="Enter ansh's pick"),
        hima: str = param(None, desc="Enter hima's pick"),
        gork: str = param(None, desc="Enter gork's pick"),
        ssom: str = param(None, desc="Enter gork's pick"),
        amit: str = param(None, desc="Enter amit's pick"),
        spahash: str = param(None, desc="Enter spahash's pick"),
        jerwin: str = param(None, desc="Enter jerwin's pick"),
        froge: str = param(None, desc="Enter froge's pick")
    ):
        if inter.author.id in (760426797418151937, 755085116593799198):
            picks = [[ansh],[hima],[gork],[ssom],[amit],[spahash],[jerwin],[froge]]
            request = sheet.values().update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=f"{current_gw}!{pos_cells[position]}",
                valueInputOption="USER_ENTERED",
                body={"values":picks}
            ).execute()
            await inter.response.send_message(f"```Updated picks for {position}:\nAnsh - {ansh}, Hima - {hima}, Gork - {gork}, Ssom - {ssom}\nAmit - {amit}, Spahash - {spahash}, Jerwin - {jerwin}, Froge - {froge}\n{request}```")
            await asyncio.sleep(20)
            await inter.delete_original_message()
        else:
            await inter.response.send_message("Sorry, you don't have access to this command :jayshreeram:", ephemeral=True)
    
    @picks.sub_command(
        name="individual",
        description="Update a single position pick for a user"
    )
    async def picks_individual(
        self,
        inter,
        user: str = param(desc="Choose the user who's pick is to be updated", autocomp=autocomp_users),
        position: str = param(desc="Choose the position where the pick is to be updated", autocomp=autocomp_postn),
        pick: str = param(desc="Enter the pick to be updated")
    ):
        if inter.author.id in (760426797418151937, 755085116593799198):
            picks = [[pick]]
            request = sheet.values().update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=f"{current_gw}!{ind_pos[position]}{ind_user[user]}",
                valueInputOption="USER_ENTERED",
                body={"values":picks}
            ).execute()
            await inter.response.send_message(f"Updated {pick} for {user}\n```{request}```")
            await asyncio.sleep(20)
            await inter.delete_original_message()
        else:
            await inter.response.send_message("Sorry, you don't have access to this command :jayshreeram:", ephemeral=True)

    @commands.slash_command(
        guild_ids=[772179896097177631]
    )
    async def preds(self, inter):
        pass

    @preds.sub_command(
        name="summary",
        description="Sends a summary of the picks done till now in the form of a table"
    )
    async def preds_summary(
        self,
        inter
    ):
        result = sheet.values().get(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=f"{current_gw}!B5:G12"
        ).execute()
        values = result.get('values', [])
        headers = ["Manager","FWD","MID","DEF","GK","Autosub"]
        summary = tabulate(values, headers, tablefmt="pretty")
        await inter.response.send_message(f"```\n{summary}```", ephemeral=True)

    @preds.sub_command(
        name="sheet",
        description="Sends the link to the Predictions google sheet"
    )
    async def preds_sheet(
        self,
        inter
    ):
        embed = disnake.Embed(
            colour=random.choice(self.bot.color_list),
            description="[Click here to go to the google sheet](https://docs.google.com/spreadsheets/d/1gFjDHVB27FZPsIK1PHF_S4Dex4HklKJrSxkp6-ZmLhc/edit?usp=sharing)\n<:messithumbsup:855310126503559198>"
        )
        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Gsheets(bot))
