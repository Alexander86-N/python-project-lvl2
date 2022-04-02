import json
import yaml
from gendiff import engine


def generate_diff(file_path1, file_path2):
    file1 = determine_file_format(file_path1)
    file2 = determine_file_format(file_path2)
    result = engine.converting(file1, file2)
    return '\n'.join(result)


def determine_file_format(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    if file_path.endswith('.yml') or file_path.endswith('.yaml'):
        return yaml.safe_load(open(file_path))
