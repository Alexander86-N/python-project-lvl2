from gendiff import generate_diff

test_file1 = "tests/fixtures/file1.json"
test_file2 = "tests/fixtures/file2.json"
test_file3 = "tests/fixtures/file3.json"
result1 = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
result2 = '{\n    host: hexlet.io\n    timeout: 20\n    verbose: true\n}'
def test_generate_diff():
    assert generate_diff.generate_diff(test_file1, test_file2) == result1
    assert generate_diff.generate_diff(test_file3, test_file2) == result2
