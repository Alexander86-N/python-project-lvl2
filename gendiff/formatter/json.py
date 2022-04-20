import json


def format(data):
    """ Outputs data in json format. """
    print(json.loads(json.dumps(data, indent=4)))
    return json.dumps(data, indent=4)
