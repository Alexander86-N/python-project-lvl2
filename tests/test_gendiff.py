import json
import yaml
from gendiff import generate_diff


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
with open('tests/fixtures/result_json.txt') as text:
    result4 = text.read()

def test_generate_diff():
    assert generate_diff.generate_diff(test_file1, test_file2) == result1[:-1]
    assert generate_diff.generate_diff(test_file3, test_file4) == result1[:-1]
    assert generate_diff.generate_diff(test_file5, test_file6) == result2[:-1]
    assert generate_diff.generate_diff(test_file7, test_file8) == result2[:-1]
    assert generate_diff.generate_diff(test_file5, test_file8) == result2[:-1]
    assert generate_diff.generate_diff(test_file5, test_file6, 'plain') == result3[:-1]
    assert generate_diff.generate_diff(test_file7, test_file8, 'plain') == result3[:-1]
    assert generate_diff.generate_diff(test_file5, test_file8, 'plain') == result3[:-1]
    assert generate_diff.generate_diff(test_file5, test_file6, 'json') == result4[:-1]
    assert generate_diff.generate_diff(test_file7, test_file8, 'json') == result4[:-1]
    assert generate_diff.generate_diff(test_file5, test_file8, 'json') == result4[:-1]


def test_determine_file_format():
    assert generate_diff.determine_file_format(test_file1) == json.load(open(test_file1))
    assert generate_diff.determine_file_format(test_file3) == yaml.safe_load(open(test_file3))
    assert generate_diff.determine_file_format(test_file4) == yaml.safe_load(open(test_file4))
