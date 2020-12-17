"""
	reset_database.py

	This script should be ran with extreme care, it will reset the database to default
"""

# IMPORTS #########################################################################################
import sqlite3
import yaml
import os
from static import handler
###################################################################################################

# SQL QUERIES #####################################################################################
def sql_create_subjects_table():
	return 'CREATE TABLE Subjects \
			(id INTEGER, name VARCHAR(100), acronym VARCHAR(10), level INTEGER);'

def sql_create_correlations_table():
	return 'CREATE TABLE Correlations \
		(subject_id INTEGER, need_to VARCHAR(10), \
		correlative_subject_id INTEGER, plan INTEGER, correlative_status_needed VARCHAR(10));'


###################################################################################################

def load_config_data():
	# Load database config file
	database_config = yaml.safe_load(open('database_config.yaml', 'rt'))

	return database_config


def main():
	#

	# Load configurations
	config_data = load_config_data()

	database_path = config_data['database_path']

	# If database file doesn't exists
	if not os.path.exists(database_path):
		print('There is no database created in the path:', database_path)
		
		answer = ''
		while answer not in ['y', 'n', 'yes', 'no']:
			answer = str(input('Do you want to continue by creating the database? y/n >> '))

		if answer in ['n', 'no']:
			return
	else:
		# Removal of existing database file
		os.remove(database_path)

	# Connection to the database & creation if it doesn't exists
	connection = sqlite3.connect(database_path)

	# Cursor object
	cursor = connection.cursor()


	# Execution of queries
	# -----------------------------------------------------------------------------------
	cursor.execute(sql_create_subjects_table())
	cursor.execute(sql_create_correlations_table())
	# -----------------------------------------------------------------------------------


	# Close connection
	connection.close()

main()