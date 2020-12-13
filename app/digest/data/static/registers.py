"""
	registers.py

"""

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