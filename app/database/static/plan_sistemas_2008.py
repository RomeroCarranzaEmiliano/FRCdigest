"""
	plan_sistemas_2008.py

"""

# IMPORTS #########################################################################################
import os


###################################################################################################

# REGISTERS & OBJECTS #############################################################################

# Subject register
class Subject():
    def __init__(self, id, name, acronym, level):
        self.id = id
        self.name = name
        self.acronym = acronym
        self.level = level


# Correlation register
class Correlation():
    def __init__(self, subject_id, need_to, correlative_subject_id, plan, correlative_status_needed):
        self.subject_id = subject_id
        self.need_to = need_to
        self.correlative_subject_id = correlative_subject_id
        self.plan = plan
        self.correlative_status_needed = correlative_status_needed


class Parsed_line():
    def __init__(self, level, id, name, acronym, regulars_to_enroll, passed_to_enroll, passed_to_take_final):
        self.level = level
        self.id = id
        self.name = name
        self.acronym = acronym
        self.regulars_to_enroll = regulars_to_enroll
        self.passed_to_enroll = passed_to_enroll
        self.passed_to_take_final = passed_to_take_final


###################################################################################################


# FUNCTIONS
###################################################################################################

def csv_sublist_to_vector(string):
    # Recives a string with format like (0;1;2) and returns a list like [0, 1, 2]
    vector = []
    if string != '':
        length = len(string)
        if string[0] == '(' and string[length - 1] == ')':
            trimed_string = string[1:length - 1]
            trimed_string = trimed_string.split(';')
            for number in trimed_string:
                vector.append(int(number))
            return vector
        elif string == 'all':
            # Support 'all' referring to all subject needed
            vector.append('all')
        else:
            # It is getting only one subject, not a list
            vector.append(int(string))
            return vector
    else:
        return False


def read_csv_line(line):
    # Reads the csv line and retuns a ready-to-use object containing the data
    if line[0] != '#':
        line = line.rstrip()
        splited_line = line.split(',')

        level = splited_line[0]
        id = splited_line[1]
        name = splited_line[2]
        acronym = splited_line[3]
        regulars_to_enroll = csv_sublist_to_vector(splited_line[4])
        passed_to_enroll = csv_sublist_to_vector(splited_line[5])
        passed_to_take_final = csv_sublist_to_vector(splited_line[6])

        parsed_line = \
            Parsed_line(level, id, name, acronym, regulars_to_enroll, passed_to_enroll, passed_to_take_final)

        return parsed_line

    else:
        return False


def get_correlations_from_list(subject_id, need_to, subject_list, plan, correlative_status_needed):
    # Returns false if the list provided is false
    # Otherwise, returns a vector with of registers containing
    # the data for every correlation rule
    if not subject_list:
        return False

    correlations_vector = []
    for subject in subject_list:
        correlation = Correlation(subject_id, need_to, subject, plan, correlative_status_needed)
        correlations_vector.append(correlation)

    return correlations_vector


def get_data(filename='static/plan_sistemas_2008.csv'):
    # Returns two vectors with registers for subjects and correlatives
    # containing all data for easy insertion into the database

    # Open file
    file = open(filename, 'rt')

    length = os.path.getsize(filename)
    pointer = file.tell()

    subjects_vector = []
    correlations_vector = []

    while pointer < length:
        raw_line = file.readline()
        pointer = file.tell()

        line = read_csv_line(raw_line)

        if line:
            subject = Subject(line.id, line.name, line.acronym, line.level)

            subjects_vector.append(subject)

            regulars_to_enroll = get_correlations_from_list(line.id, 'enroll', line.regulars_to_enroll,
                                                            2008, 'REGULAR')
            passed_to_enroll = get_correlations_from_list(line.id, 'enroll', line.passed_to_enroll,
                                                          2008, 'PASSED')
            passed_to_take_final = get_correlations_from_list(line.id, 'final', line.passed_to_take_final,
                                                              2008, 'PASSED')

            if regulars_to_enroll:
                for i in range(len(regulars_to_enroll)):
                    correlations_vector.append(regulars_to_enroll[i])

            if passed_to_enroll:
                for i in range(len(passed_to_enroll)):
                    correlations_vector.append(passed_to_enroll[i])

            if passed_to_take_final:
                for i in range(len(passed_to_take_final)):
                    correlations_vector.append(passed_to_take_final[i])

    # Close file
    file.close()

    return subjects_vector, correlations_vector

###################################################################################################
