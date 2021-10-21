import contextlib
import io
import os
import logging

import disnake
from disnake.mentions import AllowedMentions
import pymongo
from disnake.ext import commands

# Local code
import utils.json_loader
from utils.mongo import Document

intents = disnake.Intents.all()  # Help command requires member intents
DEFAULTPREFIX = ";"
secret_file = utils.json_loader.read_json("secrets")
bot = commands.Bot(
    command_prefix={DEFAULTPREFIX},
    case_insensitive=True,
    owner_id=760426797418151937,
    help_command=None,
    intents=intents,
    AllowedMentions=False,
)  # change command_prefix='-' to command_prefix=get_prefix for custom prefixes
bot.config_token = secret_file["token"]
bot.connection_url = secret_file["mongo"]

logging.basicConfig(level=logging.INFO)

bot.DEFAULTPREFIX = DEFAULTPREFIX
bot.blacklisted_users = []

bot.version = "2.0"

bot.colors = {
    "AQUA": 0x1ABC9C,
    "GREEN": 0x2ECC71,
    "BLUE": 0x3498DB,
    "PURPLE": 0x9B59B6,
    "LUMINOUS_VIVID_PINK": 0xE91E63,
    "GOLD": 0xF1C40F,
    "ORANGE": 0xFFB500,
    "RED": 0xE74C3C,
}
bot.color_list = [c for c in bot.colors.values()]

@bot.event
async def on_ready():
    # On ready, print some details to standard out
    print(
        f"----------\nReady to Deploy\n----------\n"
    )
    await bot.change_presence(
        activity = disnake.Activity(type = disnake.ActivityType.listening, name = ";help or @Gideon"),
        status = disnake.Status.dnd
    )  # This changes the bots 'activity'

@bot.event
async def on_message(message):
    # Ignore messages sent by yourself
    if message.author.bot:
        return

    # A way to blacklist users from the bot by not processing commands
    # if the author is in the blacklisted_users list
    if message.author.id in bot.blacklisted_users:
        return

    # Whenever the bot is tagged, respond with its prefix
    if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(
        f"<@!{bot.user.id}>"
    ):
        await message.reply(f"<:frogeez:879789528511025214> Need any help? My prefix is `;`and you can do `;help` to see a list of all the commands programmed in my System", delete_after=15, mention_author=False)

    await bot.process_commands(message)


bot.mongo = pymongo.MongoClient(str(bot.connection_url))
bot.db = bot.mongo["Gideon"]

for file in os.listdir(f'./cogs'):
    if file.endswith('.py') and not file.startswith('_') and not file.startswith('.'):
        bot.load_extension(f'cogs.{file[:-3]}')
        print(f'Loaded the category: {file}')
    
bot.run(bot.config_token)
