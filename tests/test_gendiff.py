from gendiff import generate_diff

test_file1 = "/home/golem86/example/one/two/file1.json"
test_file2 = "/home/golem86/example/file2.json"
result =
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
def test_generate_diff():
    assert generate_diff(test_file1, test_file2) == result
