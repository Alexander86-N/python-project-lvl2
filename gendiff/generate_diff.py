import json
import yaml
from gendiff.engine import diff
from gendiff.formatter.define_formatter import define_formatter


def generate_diff(file_path1, file_path2, formate_name='stylish'):
    """ Collects and outputs diff. """
    file1 = determine_file_format(file_path1)
    file2 = determine_file_format(file_path2)
    result = diff.diff(file1, file2)
    return define_formatter(result, formate_name)


def determine_file_format(file_path):
    """ Determines the file format and opens it. """
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    if file_path.endswith('.yml') or file_path.endswith('.yaml'):
        return yaml.safe_load(open(file_path))
