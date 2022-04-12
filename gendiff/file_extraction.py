import json
import yaml
from pathlib import Path


def parser_file(data):
    """ Generates the absolute path of the file. """
    path = Path(data)
    extension = path.suffix
    if path.is_absolute():
        return opening_file(path, extension)
    else:
        file_path = path.expanduser()
        return opening_file(file_path, extension)


def opening_file(path, file_extension):
    """ Determines the file format and opens it. """
    if file_extension == '.json':
        with open(path) as f:
            return json.load(f)
    elif file_extension == '.yml' or file_extension == '.yaml':
        with open(path) as f:
            return yaml.safe_load(f)
