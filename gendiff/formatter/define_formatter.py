from gendiff.formatter.stylish import stylish


def define_formatter(diff_list, view='stylish'):
    if view == 'stylish':
        return stylish(diff_list)
