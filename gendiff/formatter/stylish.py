from gendiff.engine.change_view import view_change, change_dictionary_view


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
        result = change_dictionary_view(data, indent)
    elif isinstance(data, str):
        result = str(data)
    else:
        result = view_change(data)
    return result
