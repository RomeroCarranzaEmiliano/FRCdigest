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
from app.bot import config


###################################################################################################

def help(data):
    # Shows a list of commands and their use

    content = ''
    content += '**[ help ]** *lista de comandos aceptados*\n'
    content += '**[ ch nickname <nickname> ]** *modifica el apodo del bot*\n'
    content += '**[ list subjects ]** *lista de materias y sus acronimos*\n'
    content += '**[ rules <ord> ]** *muestra las correlatividades para una materia*\n'

    colour = discord.Colour.from_rgb(100, 200, 100)
    response = discord.Embed(title='Comandos aceptados',
                             description=content, color=colour)

    return response


def change_nickname(data):
    # Changes the callable nickname for the server
    # format: ['ch', 'new_nickname', '_']

    # Verify that it has administrator privileges
    is_admin = data[1].author.guild_permissions.administrator
    if not is_admin:
        colour = discord.Colour.from_rgb(100, 0, 0)
        response = discord.Embed(title='ERROR: Permiso denegado',
                                 description='Debe tener privilegios de administrador para poder ejecutar el commando',
                                 color=colour)
        return response

    # Get vectorized command from data
    command = data[2]

    # Get parameter
    new_nickname = command[2]

    # Get server_id from data
    server_id = data[1].guild.id

    # Update config.db
    # ---------------------------------------------------------------------------------------------
    # Creation & connection to the database
    connection = sqlite3.connect('app/bot/config.db')

    """
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
    
    """

    config.change_bot_nickname(new_nickname, server_id)

    confirmed_nickname = new_nickname

    content = 'Mi nuevo apodo es: ' + confirmed_nickname + '\n'
    content += '**[ ' + confirmed_nickname + ' help ]** *para más ayuda*'

    colour = discord.Colour.from_rgb(100, 200, 100)
    response = discord.Embed(title='ATENCIÓN !!!',
                             description=content, color=colour)

    return response


def list_subjects(data):
    # Shows a list of subjects and their acronyms for sistemas plan 2008
    result = api.do('names&acronyms', '')

    length = len(result)
    ids = ''
    subjects = ''
    acronyms = ''

    for i in range(length):
        ids += str(result[i][2]) + '\n'
        subjects += result[i][0] + '\n'
        if result[i][1] == '':
            acronyms += 'none\n'
        else:
            acronyms += result[i][1] + '\n'

    colour = discord.Colour.from_rgb(100, 200, 100)
    response = discord.Embed(title='Lista de materias/acronimos',
                             description='ing. en sistemas - plan 2008', color=colour)
    response.add_field(name='Ord.', value=ids, inline=True)
    response.add_field(name='Materia', value=subjects, inline=True)
    response.add_field(name='Acronimo', value=acronyms, inline=True)

    return response


def rules_x(data):
    results, subject_name = api.do('rules_x', data)

    # In case subject id isn't valid
    if not results and type(results) == bool:
        colour = discord.Colour.from_rgb(100, 0, 0)
        response = discord.Embed(title='ERROR: materia no encontrada',
                                 description='Verifique que el parametro dado corresponda al ord. de la materia\n'
                                             '> [ list subjects ] *para ver el ord. de cada materia*', color=colour)
        return response

    title = 'Correlatividades para __' + subject_name + '__'

    to_enroll = ''
    to_take_final = ''

    length = len(results)
    if length > 0:
        for i in range(len(results)):
            if results[i][2] == 'enroll':
                if results[i][5] == 'REGULAR':
                    to_enroll += '[reg] '
                elif results[i][5] == 'PASSED':
                    to_enroll += '[apr] '
                to_enroll += results[i][4] + '\n'
            elif results[i][2] == 'final':
                if results[i][5] == 'REGULAR':
                    to_take_final += '[reg] '
                elif results[i][5] == 'PASSED':
                    to_take_final += '[apr] '
                to_take_final += results[i][4] + '\n'

    # In case there is no correlatives
    if to_enroll == '':
        to_enroll = 'no posee correlativas para cursar'
    if to_take_final == '':
        to_take_final = 'no posee correlativas para rendir'

    colour = discord.Colour.from_rgb(100, 200, 100)
    response = discord.Embed(title=title,
                             description='[reg] *se debe tener regular* \n [apr] *se debe tener aprobada*',
                             color=colour)

    response.add_field(name='Para cursar', value=to_enroll, inline=False)
    response.add_field(name='Para rendir', value=to_take_final, inline=False)

    return response


dictionary = {
    'help': help,
    'change_nickname': change_nickname,
    'list_subjects': list_subjects,
    'rules_x': rules_x,
}
