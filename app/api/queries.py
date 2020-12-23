"""
    queries.py

    Contains functions used to perform all queries needed for the api's features
    All functions are stored in a dictionary to be used in __main__.py
"""

# IMPORTS #########################################################################################
import sqlite3
import yaml


###################################################################################################

def select_name_and_acronym_from_subjects(data):
    #

    # Load database config data
    print()
    database_config = yaml.safe_load(open('../api/database_config.yaml', 'rt'))
    database_path = database_config['database_path']

    # Connection to the database
    connection = sqlite3.connect(database_path)

    # Cursor object
    cursor = connection.cursor()

    # Sql query
    sql = 'SELECT name, acronym FROM subjects;'

    # Execution of query
    cursor.execute(sql)

    results = cursor.fetchall()

    # Close connection
    connection.close()

    return results


# Dictionary
# -------------------------------------------------------------------------------------------------

dictionary = {
    'names&acronyms': select_name_and_acronym_from_subjects
}