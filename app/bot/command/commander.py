"""
    commander.py

    An object responsible of detecting the command called, the parameters given, verification of parameters,
    formatting of parameters as a vector and execution of the command
"""

# IMPORTS #########################################################################################
from command import command_dictionary


###################################################################################################

class Commander():
    def __init__(self, command):
        self.command = command
        self.parameters = []
        self.to_do = ''
        self.command_dictionary = command_dictionary.dictionary
        self.response = ''

    def detect(self):
        # Detects which command has been called
        """
            for developing purposes, return help as if the command given
            had some syntax error
        """

        self.to_do = 'help'

    def execute(self):
        # Executes the command listed

        # Verifies that to_do isn't empty
        if self.to_do == '':
            return False

        # Executes command
        self.response = self.command_dictionary[self.to_do]()
