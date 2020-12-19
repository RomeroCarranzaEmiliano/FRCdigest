"""
    database __main__.py

"""

# IMPORTS #########################################################################################
import reset_database
###################################################################################################

def main():
    command = ''
    while command != 'quit':

        # Read command
        command = str(input('>> '))
    
        if command == 'reset_database':
            reset_database.reset()
    

if __name__ == '__main__':
    main()