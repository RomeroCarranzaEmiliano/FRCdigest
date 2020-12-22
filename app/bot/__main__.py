"""
    __main__.py
    The bot runs up by executing this file


"""

# IMPORTS
###################################################################################################
import os
import discord
from dotenv import load_dotenv
import config
from command import __main__ as cmd
#
###################################################################################################


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


# When the bot is logged in the server
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    # Adds the server_id and default nickname to the config database
    server_id = client.guilds[0].id

    config.store_default_nickname_for(server_id)


# When a message is send in the server
@client.event
async def on_message(message):
    # Discriminates messages send by the actual bot, only continue with messages send by users
    if message.author == client.user:
        return

    # Process message content into a vectorized command
    command = cmd.process_message_into_vectorized_command(message.content)

    # Discriminates messages that arent meant for the bot
    server_id = client.guilds[0].id
    if config.get_bot_nickname_for_server(server_id) != command[0]:
        return

    # Execute command and fetch response
    response = cmd.do(command)

    # Send response
    await message.channel.send(response)

client.run(TOKEN)
