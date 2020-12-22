"""
    command.__main__.py

    Serves to process messages and execute commands
"""


# IMPORTS #########################################################################################
from command import commander as cmdr
###################################################################################################

def process_message_into_vectorized_command(message):
    # Grabs a message, returns a vectorized command

    # Split message
    vectorized_command = message.split(' ')

    return vectorized_command


def do(command):
    # Grabs a vectorized command, detects command and parameters, executes command

    """
        For testing purposes
        without further due, returns as if it was a syntax error,
        informs error and returns help command instead
    """

    # Delete first element of command which is the bot's nickname, already verified
    del command[0]

    # Obtain an object with the method execute which will perform the command
    commander = cmdr.Commander(command)

    # Detects which command has been called
    commander.detect()

    # Executes command
    commander.execute()

    # Fetch response
    response = commander.response

    return response


