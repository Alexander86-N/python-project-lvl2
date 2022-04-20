from gendiff.formatter import stylish
from gendiff.formatter import plain
from gendiff.formatter import json


def format(data, format_type):
    if format_type == 'stylish':
        return stylish.format(data)
    if format_type == 'plain':
        return plain.format(data)
    if format_type == 'json':
        return json.format(data)
