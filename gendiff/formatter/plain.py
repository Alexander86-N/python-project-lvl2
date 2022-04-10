from gendiff.engine.change_view import view_change


def plain(diff_list, path=''):
    """ Describes file comparison in simple terms. """
    result = []
    for node in diff_list:
        if node['status'] == 'parent':
            change_path = path + f"{node['name']}."
            result.append(plain(node['children'], change_path))
        elif node['status'] == 'changed':
            change_path = path + node['name']
            result.append(f"Property '{change_path}' was updated.\
 From {get_view(node['value before'])} to {get_view(node['value after'])}")
        elif node['status'] == 'available':
            change_path = path + node['name']
            result.append(f"Property '{change_path}' was removed")
        elif node['status'] == 'added':
            change_path = path + node['name']
            result.append(f"Property '{change_path}' was added with value:\
 {get_view(node['value'])}")
    return '\n'.join(result)


def get_view(value):
    """ Gives the value a clear, inline look. """
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    else:
        return view_change(value)
