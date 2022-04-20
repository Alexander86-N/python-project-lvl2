from pathlib import Path
from gendiff.diff import diff
from gendiff.parsing import parser
from gendiff.formatter.format import format


def generate_diff(file_path1, file_path2, formate_name='stylish'):
    """ Collects and outputs diff. """
    data1 = parser(read_file(file_path1), get_format(file_path1))
    data2 = parser(read_file(file_path2), get_format(file_path2))
    result = diff(data1, data2)
    return format(result, formate_name)


def read_file(filename):
    result = ''
    with open(filename) as file_data:
        result = file_data.read()
    return result


def get_format(filename):
    """ Specifies the format of this file. """
    path = Path(filename)
    extension = path.suffix
    return extension[1:]
