from gendiff import stylish


test_case1 = [{'name': 'one', 'status': 'added', 'value': False}]
test_case2 = [{'name': 'one', 'status': 'available', 'value': False},
            {'name': 'two', 'status': 'same', 'value': 5}]
test_case3 = [{'name': 'one', 'status': 'parent', 'children': [
    {'name': 'two', 'status': 'added', 'value': None}]}]
test_case4 = [{'name': 'one', 'status': 'changed', 'value before': False,
    'value after': True}]
def test_stylish():
        assert stylish.stylish(test_case1) == '{\n  + one: false\n}'
        assert stylish.stylish(test_case2) == '{\n  - one: false\n    two: 5\n}'
        assert stylish.stylish(test_case3) == \
        '{\n    one: {\n      + two: null\n    }\n}'
        assert stylish.stylish(test_case4) == \
        '{\n  - one: false\n  + one: true\n}'


test_case6 = False
test_case7 = None
test_case8 = {'wolf': 5}
test_case9 = {'wolf': {'fox': True}}
test_case10 = ''
def test_format_data():
        assert stylish.format_data(test_case6, '  ') == 'false'
        assert stylish.format_data(test_case7, '  ') == 'null'
        assert stylish.format_data(test_case8, '  ') == '{\n        wolf: 5\n    }'
        assert stylish.format_data(test_case9, '  ') ==\
        '{\n        wolf: {\n            fox: true\n        }\n    }'
        assert stylish.format_data(test_case10, '  ') == ''

