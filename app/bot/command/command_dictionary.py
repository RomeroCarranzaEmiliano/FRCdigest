"""
    command_dictionary.py

    Contains functions that represent each command, and a dictionary containing a key(command name)
    and the respective function
"""

# IMPORTS #########################################################################################
import sqlite3
###################################################################################################

def help(data):
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

dictionary = {
    'help': help,
    'change_nickname': change_nickname
}