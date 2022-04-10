import json
import yaml
from gendiff.engine.file_extraction import determine_file_format


test_file1 = "tests/fixtures/file1.json"
test_file2 = "tests/fixtures/file1.yaml"
test_file3 = "tests/fixtures/file2.yml"

def test_determine_file_format():
    assert determine_file_format(test_file1) == json.load(open(test_file1))
    assert determine_file_format(test_file2) == yaml.safe_load(open(test_file2))
    assert determine_file_format(test_file3) == yaml.safe_load(open(test_file3))
