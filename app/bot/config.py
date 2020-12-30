"""
    config.py

    serves to config the bot
"""

# IMPORTS #########################################################################################
import sqlite3
import yaml


###################################################################################################


def store_default_nickname_for(server_id):
    # Stores the default nickname for this instance of the bot
    # in the config database

    # Get default nickname from config.yml
    config_file = yaml.safe_load(open('app/bot/config.yml', 'rt'))
    default_nickname = config_file['bot_default_nickname']

    # Connection to the database
    connection = sqlite3.connect('app/bot/config.db')

    # Cursor object
    cursor = connection.cursor()

    # sql query
    sql_delete_existing_row = 'DELETE FROM nicknames WHERE server_id = ?;'
    sql_insert_nickname_and_server_id = 'INSERT INTO nicknames (server_id, nickname) VALUES (?, ?);'
    parameters = (server_id, default_nickname)

    # Execution of query
    # Delete existing rows for the server id
    cursor.execute(sql_delete_existing_row, (server_id,))
    connection.commit()
    # Insert new row for the server id
    cursor.execute(sql_insert_nickname_and_server_id, parameters)
    connection.commit()

    # Close connection
    connection.close()

    print('default_nickname: ', default_nickname)
    print('server_id: ', server_id)


def change_bot_nickname(nickname, server_id):
    # Changes the bot's nickname with the nickname provided

    # Connection to the database
    connection = sqlite3.connect('app/bot/config.db')

    # Cursor object
    cursor = connection.cursor()

    # sql query
    sql_update_nickname = 'UPDATE nicknames SET ? WHERE server_id = ?;'
    parameters = (nickname, server_id)

    # Execution of query
    cursor.execute(sql_update_nickname, parameters)

    # Close connection
    connection.close()


def get_bot_nickname_for_server(server_id):
    # Returns the bot's nickname set for the server

    # Connection to the database
    connection = sqlite3.connect('app/bot/config.db')

    # Cursor object
    cursor = connection.cursor()

    # sql query
    sql_get_nickname = 'SELECT nickname FROM nicknames WHERE server_id = ?'
    parameters = (server_id,)

    # Execution of query
    cursor.execute(sql_get_nickname, parameters)

    # Get result
    nickname = cursor.fetchone()[0]

    # Close connection
    connection.close()

    print('nickname stored: ', nickname)

    return nickname
