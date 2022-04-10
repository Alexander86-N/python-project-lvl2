from gendiff.engine import diff
from gendiff.formatter.define_formatter import define_formatter
from gendiff.engine.file_extraction import determine_file_format


def generate_diff(file_path1, file_path2, formate_name='stylish'):
    """ Collects and outputs diff. """
    file1 = determine_file_format(file_path1)
    file2 = determine_file_format(file_path2)
    result = diff.diff(file1, file2)
    return define_formatter(result, formate_name)
