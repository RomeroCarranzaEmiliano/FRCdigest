"""
    api.__main__.py

    api's access point
"""

# IMPORTS #########################################################################################
from app.api import queries


###################################################################################################

def do(feature_tag, data):
    return queries.dictionary[feature_tag](data)

