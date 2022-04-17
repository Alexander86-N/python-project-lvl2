import json


def format_json(diff_list):
    """ Outputs data in json format. """
    return json.dumps(diff_list, indent=4)


def format(data):
    return format_json(data)
