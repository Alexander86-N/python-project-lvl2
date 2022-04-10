from gendiff.engine.view_change import view_change


SYMBOLS = {"added": "+ ", "available": "- ", "parent": "  ", "same": "  "}


def stylish(diff_list, depth=0, indent='  '):
    """ Forms a text representation of the list. """
    result = ['{']
    for i in range(depth):
        indent += '    '
    for node in diff_list:
        if node['status'] == 'parent':
            result.append(f"{indent}{SYMBOLS.get(node['status'])}{node['name']}:\
 {stylish(node['children'], depth + 1)}")
        elif node['status'] == 'changed':
            result.append(f"{indent}{SYMBOLS['available']}{node['name']}:\
 {format_data(node['value before'], indent)}")
            result.append(f"{indent}{SYMBOLS['added']}{node['name']}:\
 {format_data(node['value after'], indent)}")
        else:
            result.append(f"{indent}{SYMBOLS.get(node['status'])}{node['name']}:\
 {format_data(node['value'], indent)}")
    result.append(indent[:-2] + '}')
    return '\n'.join(result)


def format_data(data, indent):
    """ Modifies each element of the incoming data ."""
    if isinstance(data, dict):
        indent += '    '
        result = '{\n'
        for key in data.keys():
            value = format_data(data[key], indent)
            result += f'{indent}  {key}: {value}\n'
        result += indent[:-2] + '}'
    elif isinstance(data, str):
        result = str(data)
    else:
        result = view_change(data)
    return result
