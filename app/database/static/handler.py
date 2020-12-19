"""
	handler.py
	Serves as an interface module for transforming .csv files in this directory into 
	easy-to-use vectors of registers

	Every .csv static file in this directory should have a function in this file in order
	to be easy handled by other modules
"""

# IMPORTS #########################################################################################
from static import plan_sistemas_2008
###################################################################################################

# plan_sistemas_2008
def get_plan_sistemas_2008():
	data = plan_sistemas_2008.get_data()
	return data

