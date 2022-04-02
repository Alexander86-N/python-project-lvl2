import json
from gendiff import engine


test_case1 = json.load(open("tests/fixtures/file1.json"))
test_case2 = json.load(open("tests/fixtures/file2.json"))
result1 = ['{', '  - follow: false', '    host: hexlet.io',
        '  - proxy: 123.234.53.22', '  - timeout: 50',
        '  + timeout: 20', '  + verbose: true', '}']
def test_converting():
        assert engine.converting(test_case1, test_case2) == result1


test_case3 = [('two', False), ('four', 'Yes'), ('one', 1)]
test_case4 = [('one', 1), ('two', True), ('tree', 'no')]
test_case5 = [('one', 1), ('two', True), ('tree', 'no'),
        ('two', False), ('four', 'Yes')]
result = ['{', '  + four: Yes', '    one: 1', '  - tree: no',
                '  - two: true', '  + two: false', '}']
def test_create_new_list():
        assert engine.create_new_list(test_case5, test_case4, test_case3) == result


test_case6 = ('fllow', 5)
test_case7 = (124, False)
def test_covert_to_string():
        assert engine.convert_to_string(test_case6, '-') == '  - fllow: 5'
        assert engine.convert_to_string(test_case7, ' ') == '    124: false'


test_case8 = ['one', 'two', 'tree']
test_case9 = ['two', 'four']
test_case10 = []
result2 = ['one', 'two', 'tree', 'four']
def test_unite():
    assert engine.unite(test_case8, test_case9) == result2
    assert engine.unite(test_case10, test_case9) == ['two', 'four']
    assert engine.unite(test_case10, test_case10) == []


