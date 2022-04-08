from gendiff.engine import diff


test_case1 = {'file': 1}
test_case2 = {}
test_case3 = {'file': 1, 'doc': False}
test_case4 = {'file': 5, 'doc': False}
test_case5 = {'file': None, 'doc': {'hello': 'world'}}
test_case6 = {'file': None, 'doc': {'hello': 'world!', 'good': 'bad'}} 
def test_diff():
    assert diff.diff(test_case1, test_case2) == \
            [{'name': 'file', 'status': 'available', 'value': 1}]
    assert diff.diff(test_case1, test_case3) == \
            [{'name': 'doc', 'status': 'added', 'value': False},
             {'name': 'file', 'status': 'same', 'value': 1}]
    assert diff.diff(test_case3, test_case4) == \
            [{'name': 'doc', 'status': 'same', 'value': False},
             {'name': 'file', 'status': 'changed', 'value before': 1, 'value after': 5}]
    assert diff.diff(test_case5, test_case6) == \
            [{'name': 'doc', 'status': 'parent', 'children': [
             {'name': 'good', 'status': 'added', 'value': 'bad'}, {'name': 'hello',
              'status': 'changed', 'value before': 'world', 'value after': 'world!'}]},
             {'name': 'file', 'status': 'same', 'value': None}]
