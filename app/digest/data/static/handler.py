"""
	handler.py
	Serves as an interface module for transforming .csv files in this directory into 
	easy-to-use vectors of registers

	Every .csv static file in this directory should have a function in this file in order
	to be easy handled by other modules
"""

# IMPORTS #########################################################################################
import registers

###################################################################################################

class Parsed_line():
	def __init__(self, level, id, name, acronym, regulars_to_enroll, passed_to_enroll, passed_to_take_final):
		self.level = level
		self.id = id
		self.name = name
		self.acronym = acronym
		self.regulars_to_enroll = regulars_to_enroll
		self.passed_to_enroll = passed_to_enroll
		self.passed_to_take_final = passed_to_take_final


def csv_sublist_to_vector(string):
	# Recives a string with format like (0;1;2) and returns a list like [0, 1, 2] 
	vector = []
	if string != '':
		length = len(string)
		if string[0] == '(' and string[length - 1] == ')':
			trimed_string = string[1:length-1]
			trimed_string = trimed_string.split(';')
			for number in trimed_string:
				vector.append(int(number))
			return vector
		else:
			return False
	else:
		return False



def read_csv_line(line):
	# Reads the csv line and retuns a ready-to-use object
	if line[0] != '#':
		splited_line = line.split(',')
		
		level = splited_line[0]
		id = splited_line[1]
		name = splited_line[2]
		acronym = splited_line[3]
		regulars_to_enroll = csv_sublist_to_vector(splited_line[4])
		passed_to_enroll = csv_sublist_to_vector(splited_line[5])
		passed_to_take_final = csv_sublist_to_vector(splited_line[6])

		parsed_line = Parsed_line(level, id, name, acronym, regulars_to_enroll, passed_to_enroll, passed_to_take_final)

		return parsed_line


#reg = read_csv_line('2,10,analisis matematico II,,(1;2),,(1;2)')
