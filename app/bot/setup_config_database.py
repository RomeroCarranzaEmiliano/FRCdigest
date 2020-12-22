"""
    setup_cofig_database.py

    Serves to create the config database and tables
"""

# IMPORTS #########################################################################################
import sqlite3
import os


###################################################################################################

def setup():
    # Setup config database

    # Continue only if database doesn't exists
    if os.path.exists('config.db'):
        print('The database already exists')
        return False

    print('The database doesnt exists')

    # Creation & connection to the database
    connection = sqlite3.connect('config.db')

    # Cursor object
    cursor = connection.cursor()

    # sql query
    sql_create_nicknames_table = 'CREATE TABLE nicknames (server_id VARCHAR(50), nickname VARCHAR(5));'

    # Execution of query
    cursor.execute(sql_create_nicknames_table)
    connection.commit()

    print(cursor.fetchall())

    # Close connection
    connection.close()

    return True

if __name__ == '__main__':
    setup()