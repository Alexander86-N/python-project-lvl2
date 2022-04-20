SYMBOLS = {"added": "+ ", "available": "- ", "parent": "  ", "same": "  "}


def format(data):
    """ Forms a text representation of the list. """

    def creating_form(items, depth=0, indent='  '):
        result = ['{']
        for i in range(depth):
            indent += '    '
        for node in items:
            if node['status'] == 'parent':
                symbol = SYMBOLS.get(node['status'])
                children = creating_form(node['children'], depth + 1)
                result.append(f"{indent}{symbol}{node['name']}: {children}")
            elif node['status'] == 'changed':
                symbol = SYMBOLS['available']
                value = format_data(node['value before'], indent)
                result.append(f"{indent}{symbol}{node['name']}: {value}")
                symbol = SYMBOLS['added']
                value = format_data(node['value after'], indent)
                result.append(f"{indent}{symbol}{node['name']}: {value}")
            else:
                symbol = SYMBOLS.get(node['status'])
                value = format_data(node['value'], indent)
                result.append(f"{indent}{symbol}{node['name']}: {value}")
        result.append(indent[:-2] + '}')
        return '\n'.join(result)

    return creating_form(data)


def format_data(data, indent):
    """ Modifies each element of the incoming data ."""
    if isinstance(data, dict):
        result = change_dictionary_view(data, indent)
    elif isinstance(data, str):
        result = str(data)
    else:
        result = to_string(data)
    return result


def to_string(value):
    """ Outputs values in the specified form. """
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, type(None)):
        return 'null'
    else:
        return value


def change_dictionary_view(data, indent):
    """ Outputs dictionary in the specified form. """
    indent += '    '
    result = '{\n'
    for key in data.keys():
        if isinstance(data[key], dict):
            value = change_dictionary_view(data[key], indent)
        else:
            value = to_string(data[key])
        result += f'{indent}  {key}: {value}\n'
    result += indent[:-2] + '}'
    return result
