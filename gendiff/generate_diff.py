import json
import yaml
from gendiff import stylish
from gendiff.engine import diff


def generate_diff(file_path1, file_path2):
    """ Collects and outputs diff. """
    file1 = determine_file_format(file_path1)
    file2 = determine_file_format(file_path2)
    result = diff.diff(file1, file2)
    return stylish.stylish(result)


def determine_file_format(file_path):
    """ Determines the file format and opens it. """
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    if file_path.endswith('.yml') or file_path.endswith('.yaml'):
        return yaml.safe_load(open(file_path))
