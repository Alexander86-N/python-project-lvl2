result = [
    {'name': 'common', 'status': 'parent', 'children': [
        {'name': 'follow', 'status': 'added', 'value': False},
        {'name': 'setting1', 'status': 'same', 'value': 'Value 1'},
        {'name': 'setting2', 'status': 'available', 'value': 200},
        {'name': 'setting3', 'status': 'changed', 'value before': True,
         'value after': None},
        {'name': 'setting4', 'status': 'added', 'value': 'blah blah'},
        {'name': 'setting5', 'status': 'added', 'value': {'key5': 'value5'}},
        {'name': 'setting6', 'status': 'parent', 'children': [
            {'name': 'doge', 'status': 'parent', 'children': [
                {'name': 'wow', 'status': 'changed', 'value before': '',
                 'value after': 'so much'}]},
            {'name': 'key', 'status': 'same', 'value': 'value'},
            {'name': 'ops', 'status': 'added', 'value': 'vops'}]}]},
    {'name': 'group1', 'status': 'parent', 'children': [
        {'name': 'baz', 'status': 'changed', 'value before': 'bas',
         'value after': 'bars'},
        {'name': 'foo', 'status': 'same', 'value': 'bar'},
        {'name': 'nest', 'status': 'changed', 'value before': {'key': 'value'},
         'value after': 'str'}]},
    {'name': 'group2', 'status': 'available',
     'value': {'abc': 12345, 'deep': {'id': 45}}},
    {'name': 'group3', 'status': 'added',
     'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
]
