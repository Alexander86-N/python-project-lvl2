import json
import yaml
from gendiff import generate_diff


test_file1 = "tests/fixtures/file1.json"
test_file2 = "tests/fixtures/file2.json"
test_file3 = "tests/fixtures/file3.json"
test_file4 = "tests/fixtures/file1.yaml"
test_file5 = "tests/fixtures/file2.yml"
test_file6 = "tests/fixtures/file4.json"
test_file7 = "tests/fixtures/file5.json"
test_file8 = "tests/fixtures/file4.yml"
test_file9 = "tests/fixtures/file5.yml"
with open('tests/fixtures/result.txt') as text:
    result1 = text.read()
with open('tests/fixtures/result2.txt') as text:
    result3 = text.read()
def test_generate_diff():
    assert generate_diff.generate_diff(test_file1, test_file2) == result1[:-1]
    assert generate_diff.generate_diff(test_file4, test_file5) == result1[:-1]
    assert generate_diff.generate_diff(test_file6, test_file7) == result3[:-1]
    assert generate_diff.generate_diff(test_file8, test_file9) == result3[:-1]
    assert generate_diff.generate_diff(test_file6, test_file9) == result3[:-1]


def test_determine_file_format():
    assert generate_diff.determine_file_format(test_file1) == json.load(open(test_file1))
    assert generate_diff.determine_file_format(test_file4) == yaml.safe_load(open(test_file4))
    assert generate_diff.determine_file_format(test_file5) == yaml.safe_load(open(test_file5))
