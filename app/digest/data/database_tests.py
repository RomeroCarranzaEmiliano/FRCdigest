# database tests

# IMPORTS
import sqlite3


# connection to the database
connection = sqlite3.connect('FRCdigest.db')

# cursor object
cursor = connection.cursor()

sql_consult = 'SELECT * FROM Subjects;'
cursor.execute(sql_consult)
result = cursor.fetchall()

print(result)

# close connection
connection.close()
