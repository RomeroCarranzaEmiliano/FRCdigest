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


def sql_insert_subjects():
	return 'INSERT INTO subjects VALUES (?, ?, ?, ?);'

def sql_insert_correlations():
	return 'INSERT INTO correlations VALUES (?, ?, ?, ?, ?);'

###################################################################################################

def load_config_data():
	# Load database config file
	# database_config = yaml.safe_load(open('database_config.yaml', 'rt'))

	database_config = {'database_path': 'FRCdigest.db'}

	return database_config


def get_data():
	# Format plan's data for sql insertion
	data = handler.get_plan_sistemas_2008()

	l = len(data[0])
	subjects = []
	for i in range(l):
		row = (data[0][i].id, data[0][i].name, data[0][i].acronym, data[0][i].level)
		subjects.append(row)

	l = len(data[1])
	correlations = []
	for i in range(l):
		row = (data[1][i].subject_id, data[1][i].need_to, data[1][i].correlative_subject_id,
			   data[1][i].plan, data[1][i].correlative_status_needed)
		correlations.append(row)

	print(correlations)

	return subjects, correlations


def reset():
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

	data = get_data()
	subjects = data[0]
	correlations = data[1]

	# Execution of queries
	# -----------------------------------------------------------------------------------
	cursor.execute(sql_create_subjects_table())
	connection.commit()
	cursor.execute(sql_create_correlations_table())
	connection.commit()
	cursor.executemany(sql_insert_subjects(), subjects)
	connection.commit()
	cursor.executemany(sql_insert_correlations(), correlations)
	connection.commit()
	# -----------------------------------------------------------------------------------



	# Close connection
	connection.close()

	print('[database reset succesful]')