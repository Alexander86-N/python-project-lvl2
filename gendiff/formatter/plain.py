def format(data):
    """ Describes file comparison in simple terms. """

    def creating_form(items, path=''):
        result = []
        for node in items:
            if node['status'] == 'parent':
                change_path = path + f"{node['name']}."
                result.append(creating_form(node['children'], change_path))
            else:
                change_path = path + node['name']
                if node['status'] != 'same':
                    result.append(output_generation(node, change_path))
        return '\n'.join(result)

    return creating_form(data)


def to_string(value):
    """ Gives the value a clear, inline look. """
    result = ''
    if isinstance(value, dict):
        result = '[complex value]'
    elif isinstance(value, str):
        result = f"'{value}'"
    elif isinstance(value, bool):
        result = str(value).lower()
    elif isinstance(value, type(None)):
        result = 'null'
    else:
        result = value
    return result


def output_generation(items, path):
    """ Generates lines of data for output. """
    result = ''
    if items['status'] == 'changed':
        value1 = to_string(items['value before'])
        value2 = to_string(items['value after'])
        result = f"Property '{path}' was updated. From {value1} to {value2}"
    if items['status'] == 'available':
        result = f"Property '{path}' was removed"
    if items['status'] == 'added':
        value = to_string(items['value'])
        result = f"Property '{path}' was added with value: {value}"
    return result
