from gendiff.diff import diff
from gendiff.formatter.define_formatter import define_formatter
from gendiff.file_extraction import parser_file


def generate_diff(file_path1, file_path2, formate_name='stylish'):
    """ Collects and outputs diff. """
    file1 = parser_file(file_path1)
    file2 = parser_file(file_path2)
    result = diff(file1, file2)
    return define_formatter(result, formate_name)
