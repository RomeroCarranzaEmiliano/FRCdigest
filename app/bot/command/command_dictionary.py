"""
    command_dictionary.py

    Contains functions that represent each command, and a dictionary containing a key(command name)
    and the respective function
"""

# IMPORTS #########################################################################################
import sqlite3
import sys
import discord
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from app.api import __main__ as api
###################################################################################################

def help(data):
    # Shows a list of commands and their use
    return 'This is a help message yet to be written...'

def change_nickname(data):
    # Changes the callable nickname for the server
    # format: ['ch', 'new_nickname', '_']

    # Get vectorized command from data
    command = data[2]

    # Get parameter
    new_nickname = command[2]

    # Get server_id from data
    server_id = data[0].guilds[0].id

    # Update config.db
    # ---------------------------------------------------------------------------------------------
    # Creation & connection to the database
    connection = sqlite3.connect('config.db')

    # Cursor object
    cursor = connection.cursor()

    # sql query
    sql_update_nicknames_table = 'UPDATE nicknames SET nickname=? WHERE server_id = ?'

    # Parameters
    parameters = (new_nickname, server_id)

    # Execution of query
    cursor.execute(sql_update_nicknames_table, parameters)
    connection.commit()

    cursor.execute('SELECT nickname FROM nicknames WHERE server_id=?', (server_id,))
    confirmed_nickname = cursor.fetchone()[0]

    # Close connection
    connection.close()

    return 'El apodo ha sido establecido como: ' + confirmed_nickname

def list_subjects(data):
    # Shows a list of subjects and their acronyms for sistemas plan 2008
    result = api.do('names&acronyms', '')

    length = len(result)
    subjects = ''
    acronyms = ''
    for i in range(length):
        subjects += result[i][0] + '\n'
        acronyms += result[i][1] + '\n'

    colour = discord.Colour.from_rgb(100, 200, 100)
    response = discord.Embed(title='Lista de materias/acronimos',
                             description='ing. en sistemas - plan 2008', color=colour)
    response.add_field(name='Materia', value=subjects, inline=True)
    response.add_field(name='Acronimo', value=acronyms, inline=True)

    return response

dictionary = {
    'help': help,
    'change_nickname': change_nickname,
    'list_subjects': list_subjects
}