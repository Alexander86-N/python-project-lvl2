import json
import yaml
from gendiff import generate_diff
from gendiff.diff import diff
from gendiff.formatter.plain import plain
from gendiff.formatter import stylish
from gendiff.file_extraction import parser_file


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
    assert generate_diff(test_file1, test_file2) == result1[:-1]
    assert generate_diff(test_file3, test_file4) == result1[:-1]
    assert generate_diff(test_file5, test_file6) == result2[:-1]
    assert generate_diff(test_file7, test_file8) == result2[:-1]
    assert generate_diff(test_file5, test_file8) == result2[:-1]
    assert generate_diff(test_file5, test_file6, 'plain') == result3[:-1]
    assert generate_diff(test_file7, test_file8, 'plain') == result3[:-1]
    assert generate_diff(test_file5, test_file8, 'plain') == result3[:-1]
    assert generate_diff(test_file5, test_file6, 'json') == result4[:-1]
    assert generate_diff(test_file7, test_file8, 'json') == result4[:-1]
    assert generate_diff(test_file5, test_file8, 'json') == result4[:-1]


test_case9 = {'file': 1}
test_case10 = {}
test_case11 = {'file': 1, 'doc': False}
test_case12 = {'file': 5, 'doc': False}
test_case13 = {'file': None, 'doc': {'hello': 'world'}}
test_case14 = {'file': None, 'doc': {'hello': 'world!', 'good': 'bad'}}


def test_diff():
    assert diff(test_case9, test_case10) == \
        [{'name': 'file', 'status': 'available', 'value': 1}]
    assert diff(test_case9, test_case11) == \
        [{'name': 'doc', 'status': 'added', 'value': False},
         {'name': 'file', 'status': 'same', 'value': 1}]
    assert diff(test_case11, test_case12) == \
        [{'name': 'doc', 'status': 'same', 'value': False},
         {'name': 'file', 'status': 'changed', 'value before': 1,
          'value after': 5}]
    assert diff(test_case13, test_case14) == \
        [{'name': 'doc', 'status': 'parent', 'children': [
         {'name': 'good', 'status': 'added', 'value': 'bad'},
         {'name': 'hello', 'status': 'changed', 'value before': 'world',
          'value after': 'world!'}]},
         {'name': 'file', 'status': 'same', 'value': None}]


test_case15 = [{'name': 'hello', 'status': 'available', 'value': 5}]
test_case16 = [{'name': 'good', 'status': 'added', 'value': True}]
test_case17 = [{'name': 'city', 'status': 'changed', 'value before': 'Moscow',
               'value after': 'Kazan'}]
test_case18 = [{'name': 'hello', 'status': 'parent', 'children': [
    {'name': 'good', 'status': 'changed', 'value before': None,
     'value after': {'city': 'Kazan'}}]}]
test_case19 = [{'name': 'hello', 'status': 'same', 'value': 5}]
test_case20 = [{'name': 'hello', 'status': 'added', 'value': 0}]


def test_plain():
    assert plain(test_case15) == "Property 'hello' was removed"
    assert plain(test_case16) == "Property 'good' was added with value:\
 true"
    assert plain(test_case17) == "Property 'city' was updated.\
 From 'Moscow' to 'Kazan'"
    assert plain(test_case18) == "Property 'hello.good' was updated.\
 From null to [complex value]"
    assert plain(test_case19) == ""
    assert plain(test_case20) == "Property 'hello' was added with value: 0"


test_case21 = [{'name': 'one', 'status': 'added', 'value': False}]
test_case22 = [{'name': 'one', 'status': 'available', 'value': False},
               {'name': 'two', 'status': 'same', 'value': 5}]
test_case23 = [{'name': 'one', 'status': 'parent', 'children': [
    {'name': 'two', 'status': 'added', 'value': None}]}]
test_case24 = [{'name': 'one', 'status': 'changed', 'value before': False,
                'value after': True}]


def test_stylish():
    assert stylish.stylish(test_case21) == '{\n  + one: false\n}'
    assert stylish.stylish(test_case22) == '{\n  - one: false\n    two: 5\n}'
    assert stylish.stylish(test_case23) == \
           '{\n    one: {\n      + two: null\n    }\n}'
    assert stylish.stylish(test_case24) == \
           '{\n  - one: false\n  + one: true\n}'


test_case25 = False
test_case26 = None
test_case27 = {'wolf': 5}
test_case28 = {'wolf': {'fox': True}}
test_case29 = ''


def test_format_data():
    assert stylish.format_data(test_case25, '  ') == 'false'
    assert stylish.format_data(test_case26, '  ') == 'null'
    assert stylish.format_data(test_case27, '  ') == '{\n        wolf: 5\n    }'
    assert stylish.format_data(test_case28, '  ') ==\
           '{\n        wolf: {\n            fox: true\n        }\n    }'
    assert stylish.format_data(test_case29, '  ') == ''


test_file30 = "/home/golem86/python-project-lvl2/tests/fixtures/file1.json"
test_file31 = "tests/fixtures/file1.yaml"
test_file32 = "tests/fixtures/file2.yml"


def test_parser_file():
    assert parser_file(test_file30) == json.load(open(test_file1))
    assert parser_file(test_file31) ==\
           yaml.safe_load(open(test_file3))
    assert parser_file(test_file32) ==\
           yaml.safe_load(open(test_file4))
