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

        command = self.command
        command_length = len(command)

        # Verify that the command isn't empty
        if command_length == 0:
            # If it is the case, show help command
            self.to_do = 'help'
            return

        # Vectorized commands supported
        # '_' means a parameter
        supported = [
            ['help'],
            ['ch', 'nickname', '_']
        ]
        tag = [
            'help',
            'change_nickname'
        ]

        detected_command = ''
        for i in range(len(supported)):
            if detected_command != '':
                break
            if len(supported[i]) == command_length:
                for j in range(command_length):
                    if supported[i][j] != '_':
                        if command[j] != supported[i][j]:
                            break
                    if j == command_length-1:
                        detected_command = tag[i]
                        break

        self.to_do = detected_command

        # In case that any command matched
        if detected_command == '':
            # Show help command
            self.to_do = 'help'

    def execute(self, data):
        # Executes the command listed

        # Verifies that to_do isn't empty
        if self.to_do == '':
            return False

        # Executes command
        self.response = self.command_dictionary[self.to_do](data)
