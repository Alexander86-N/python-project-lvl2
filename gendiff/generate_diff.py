from gendiff.diff import diff
from gendiff.data_extraction import fetches_data
from gendiff.formatter import stylish
from gendiff.formatter import plain
from gendiff.formatter import json


def generate_diff(file_path1, file_path2, formate_name='stylish'):
    """ Collects and outputs diff. """
    data1 = fetches_data(file_path1)
    data2 = fetches_data(file_path2)
    result = diff(data1, data2)
    return {'stylish': stylish.format(result),
            'plain': plain.format(result),
            'json': json.format(result)}.get(formate_name)
