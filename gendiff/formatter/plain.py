from gendiff.formatter.stylish import view_change


def plain(diff_list):
    """ Describes file comparison in simple terms. """

    def format(items, path=''):
        result = []
        for node in items:
            if node['status'] == 'parent':
                change_path = path + f"{node['name']}."
                result.append(format(node['children'], change_path))
            else:
                change_path = path + node['name']
                if node['status'] != 'same':
                    result.append(output_generation(node, change_path))
        return '\n'.join(result)

    return format(diff_list)


def to_string(value):
    """ Gives the value a clear, inline look. """
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    else:
        return view_change(value)


def output_generation(items, path):
    result = ''
    if items['status'] == 'changed':
        result = f"Property '{path}' was updated.\
 From {to_string(items['value before'])} to {to_string(items['value after'])}"
    if items['status'] == 'available':
        result = f"Property '{path}' was removed"
    if items['status'] == 'added':
        result = f"Property '{path}' was added with value:\
 {to_string(items['value'])}"
    return result
