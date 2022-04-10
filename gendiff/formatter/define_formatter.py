from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import format_json


def define_formatter(diff_list, view='stylish'):
    if view == 'stylish':
        return stylish(diff_list)
    if view == 'plain':
        return plain(diff_list)
    if view == 'json':
        return format_json(diff_list)
