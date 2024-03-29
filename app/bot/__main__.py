"""
    __main__.py
    The bot runs up by executing this file


"""

# IMPORTS
###################################################################################################
import sys
import os
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import discord
from dotenv import load_dotenv
import app.bot.config as config
from app.bot.command import __main__ as cmd
import yaml

from discord.ext import commands, tasks

from command import scrapers
###################################################################################################

class DailyCog(commands.Cog):
    def __init__(self):
        self.scrap.start()

    def cog_unload(self):
        self.scrap.cancel()

    @tasks.loop(minutes=1)
    async def scrap(self):
        print("[SERVER] scheduled task performed")
        response_list = scrapers.dictionary["departamento_sistemas_novedades"]("")

        if response_list:
            channel = discord.utils.get(client.get_all_channels(), name="general")
            for response in response_list:
                await channel.send(embed=response)


# Check environment
config_file = yaml.safe_load(open('app/bot/config.yml', 'rt'))
environment = config_file['environment']
load_dotenv()
if environment == 'dev':
    # Development environment
    TOKEN = os.getenv('DEV_TOKEN')
else:
    # Production environment
    TOKEN = os.getenv('PROD_TOKEN')


client = discord.Client()


# When the bot is logged in the server
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    # Adds the server_id and default nickname to the config database
    #server_id = client.guilds[0].id

    #config.store_default_nickname_for(server_id)

    # Creates and starts the webscrappers schedules
    cog = DailyCog()


# When a message is send in the server
@client.event
async def on_message(message):
    # Discriminates messages send by the actual bot, only continue with messages send by users
    if message.author == client.user:
        return

    # Process message content into a vectorized command
    command = cmd.process_message_into_vectorized_command(message.content)

    # Discriminates messages that arent meant for the bot
    server_id = message.guild.id
    if config.get_bot_nickname_for_server(server_id) != command[0]:
        return

    # Execute command and fetch response
    data = [client, message, command]
    response = cmd.do(data)

    # Send response
    if type(response) == discord.embeds.Embed:
        await message.channel.send(embed=response)
    else:
        await message.channel.send(response)



client.run(TOKEN)
