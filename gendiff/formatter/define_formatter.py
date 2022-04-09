from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain


def define_formatter(diff_list, view='stylish'):
    if view == 'stylish':
        return stylish(diff_list)
    if view == 'plain':
        return plain(diff_list)
