import json
import yaml


def parser(data, extension):
    if extension == 'json':
        return json.loads(data)
    if extension == 'yaml' or extension == 'yml':
        return yaml.safe_load(data)
