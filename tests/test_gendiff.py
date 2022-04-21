import pytest
import json
from gendiff import generate_diff
from tests.fixtures import result_json


test_file1 = "tests/fixtures/file1.json"
test_file2 = "tests/fixtures/file2.json"
test_file3 = "tests/fixtures/file1.yaml"
test_file4 = "tests/fixtures/file2.yml"
test_file5 = "tests/fixtures/file4.json"
test_file6 = "tests/fixtures/file5.json"
test_file7 = "tests/fixtures/file4.yaml"
test_file8 = "tests/fixtures/file5.yml"
with open('tests/fixtures/result.txt') as text:
    result1 = text.read()
with open('tests/fixtures/result_stylish.txt') as text:
    result2 = text.read()
with open('tests/fixtures/result_plain.txt') as text:
    result3 = text.read()


@pytest.mark.parametrize('filepath1, filepath2, format, result', [
    (test_file1, test_file2, 'stylish', result1),
    (test_file3, test_file4, 'stylish', result1),
    (test_file5, test_file6, 'stylish', result2),
    (test_file7, test_file8, 'stylish', result2),
    (test_file5, test_file8, 'stylish', result2),
    (test_file5, test_file6, 'plain', result3),
    (test_file7, test_file8, 'plain', result3),
    (test_file5, test_file8, 'plain', result3)
])
def test_generate_diff(filepath1, filepath2, format, result):
    assert generate_diff(filepath1, filepath2, format) == result[:-1]


@pytest.mark.parametrize('file_path1, file_path2, format, result', [
    (test_file5, test_file6, 'json', result_json.result),
    (test_file7, test_file8, 'json', result_json.result),
    (test_file5, test_file8, 'json', result_json.result)
])
def test_generate_diff_json(file_path1, file_path2, format, result):
    assert json.loads(generate_diff(file_path1, file_path2, format)) == result
