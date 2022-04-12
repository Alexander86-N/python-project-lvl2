SYMBOLS = {"added": "+ ", "available": "- ", "parent": "  ", "same": "  "}


def stylish(diff_list):
    """ Forms a text representation of the list. """
    def format(items, depth=0, indent='  '):
        result = ['{']
        for i in range(depth):
            indent += '    '
        for node in items:
            if node['status'] == 'parent':
                result.append(f"{indent}{SYMBOLS.get(node['status'])}\
{node['name']}: {format(node['children'], depth + 1)}")
            elif node['status'] == 'changed':
                result.append(f"{indent}{SYMBOLS['available']}{node['name']}:\
 {format_data(node['value before'], indent)}")
                result.append(f"{indent}{SYMBOLS['added']}{node['name']}:\
 {format_data(node['value after'], indent)}")
            else:
                result.append(f"{indent}{SYMBOLS.get(node['status'])}\
{node['name']}: {format_data(node['value'], indent)}")
        result.append(indent[:-2] + '}')
        return '\n'.join(result)
    return format(diff_list)


def format_data(data, indent):
    """ Modifies each element of the incoming data ."""
    if isinstance(data, dict):
        result = change_dictionary_view(data, indent)
    elif isinstance(data, str):
        result = str(data)
    else:
        result = view_change(data)
    return result


def view_change(value):
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
            value = view_change(data[key])
        result += f'{indent}  {key}: {value}\n'
    result += indent[:-2] + '}'
    return result
