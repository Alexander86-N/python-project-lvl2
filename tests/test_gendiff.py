from gendiff import generate_diff

test_file1 = "/home/golem86/example/one/two/file1.json"
test_file2 = "/home/golem86/example/file2.json"
result = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
def test_generate_diff():
    assert generate_diff.generate_diff(test_file1, test_file2) == result
