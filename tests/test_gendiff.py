from gendiff import generate_diff


file1.json = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": false
        }
file2.json = {
        "timeout": 20,
        "verbose": true,
        "host": "hexlet.io"
        }
result = {
        - follow: false
          host: hexlet.io
        - proxy: 123.234.53.22
        - timeout: 50
        + timeout: 20
        + verbose: true
        }
def test_generate_diff():
    assert generate_diff(file1.json, file2.json) == result
