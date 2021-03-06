"""
    queries.py

    Contains functions used to perform all queries needed for the api's features
    All functions are stored in a dictionary to be used in __main__.py
"""

# IMPORTS #########################################################################################
import sqlite3
import yaml


###################################################################################################


def select_rules_for(data):
    #

    # Get data
    subject_id = data[2][1]

    # Load database config data
    database_config = yaml.safe_load(open('app/api/database_config.yaml', 'rt'))
    database_path = database_config['database_path']

    # Connection to the database
    connection = sqlite3.connect(database_path)

    # Cursor object
    cursor = connection.cursor()

    # Sql queries
    sql_1 = 'SELECT name FROM subjects WHERE id = ?;'
    sql_2 = 'SELECT S.id, S.name, C.need_to, C.correlative_subject_id, CS.name, C.correlative_status_needed ' \
          'FROM subjects S ' \
          'JOIN correlations C ON S.id = C.subject_id ' \
          'JOIN subjects CS ON CS.id = C.correlative_subject_id ' \
          'WHERE S.id = ?;'

    # Execution of queries
    cursor.execute(sql_1, (subject_id,))
    result_sql_1 = cursor.fetchone()
    # In case the id is invalid
    if not result_sql_1:
        # Close connection
        connection.close()
        return False, False

    subject_name = result_sql_1[0]

    cursor.execute(sql_2, (subject_id,))

    results = cursor.fetchall()

    # Close connection
    connection.close()

    # In case there are no rules
    if not results:
        return results, subject_name

    return results, subject_name


def select_name_and_acronym_from_subjects(data):
    #

    # Load database config data
    print()
    database_config = yaml.safe_load(open('app/api/database_config.yaml', 'rt'))
    database_path = database_config['database_path']

    # Connection to the database
    connection = sqlite3.connect(database_path)

    # Cursor object
    cursor = connection.cursor()

    # Sql query
    sql = 'SELECT name, acronym, id FROM subjects;'

    # Execution of query
    cursor.execute(sql)

    results = cursor.fetchall()

    # Close connection
    connection.close()

    return results


# Dictionary
# -------------------------------------------------------------------------------------------------

dictionary = {
    'names&acronyms': select_name_and_acronym_from_subjects,
    'rules_x': select_rules_for
}
