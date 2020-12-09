"""
	reset_database.py

	This script should be ran with extreme care, it will reset the database to default
"""

# IMPORTS #########################################################################################
import sqlite3
###################################################################################################

# Sensitive data needed
database_file = 'FRCdigest.db' # <-- this should be done through an enviroment file called secrets.env


# Connection to the database
connection = sqlite3.connect(database_file)

# Cursor object
cursor = connection.cursor()

# SQL consults by execution order <-- PK and FK need to be set
# Creation of the Subjects table
sql_consult_1 = 'CREATE TABLE Subjects (id INTEGER, name VARCHAR(100), acronym VARCHAR(10), level INTEGER);'
# Creation of the Correlations table
sql_consult_2 = 'CREATE TABLE Correlations (subject_id INTEGER, for VARCHAR(10), \
				correlative_subject_id INTEGER, correlative_status_needed VARCHAR(10));'

# Insertion of default rows (subjects, acronyms and correlations)
"""
	this must be done by executing a fuction in another module that returns
	two vectors of registers, one for subjects and one for correlations
"""



result = cursor.fetchall() # <-- result should be evaluated to handle any error

print(result)

# close connection
connection.close(
