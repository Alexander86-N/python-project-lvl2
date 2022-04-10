from gendiff.formatter.plain import plain


test_case1 = [{'name': 'hello', 'status': 'available', 'value': 5}]
test_case2 = [{'name': 'good', 'status': 'added', 'value': True}]
test_case3 = [{'name': 'city', 'status': 'changed', 'value before': 'Moscow',
        'value after': 'Kazan'}]
test_case4 = [{'name': 'hello', 'status': 'parent', 'children': [\
        {'name': 'good', 'status': 'changed', 'value before': None,
            'value after': {'city': 'Kazan'}}]}]
test_case5 = [{'name': 'hello', 'status': 'same', 'value': 5}]
test_case6 = [{'name': 'hello', 'status': 'added', 'value': 0}]

def test_plain():
    assert plain(test_case1) == "Property 'hello' was removed"
    assert plain(test_case2) == "Property 'good' was added with value: true"
    assert plain(test_case3) == "Property 'city' was updated.\
 From 'Moscow' to 'Kazan'"
    assert plain(test_case4) == "Property 'hello.good' was updated.\
 From null to [complex value]"
    assert plain(test_case5) == ""
    assert plain(test_case6) == "Property 'hello' was added with value: 0"
