import json
import yaml


def determine_file_format(file_path):
    """ Determines the file format and opens it. """
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    if file_path.endswith('.yml') or file_path.endswith('.yaml'):
        return yaml.safe_load(open(file_path))
