import json


def format(data):
    """ Outputs data in json format. """
    return json.dumps(data, indent=4)
