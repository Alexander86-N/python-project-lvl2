def stylish(diff_list, level=0):
    result = '{\n'
    indent = '  '
    for i in range(level):
        indent += '    '
    for node in diff_list:
        if node['status'] == 'parent':
            data = stylish(node['children'], level + 1)
            result += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'same':
            data = format_data(node['value'], indent)
            result += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'available':
            data = format_data(node['value'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
        if node['status'] == 'added':
            data = format_data(node['value'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
        if node['status'] == 'changed':
            data = format_data(node['value before'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
            data = format_data(node['value after'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
    result += indent[:-2] + '}'
    return result


def format_data(data, indent):
    if isinstance(data, dict):
        indent += '    '
        result = '{\n'
        for key in data.keys():
            value = format_data(data[key], indent)
            result += f'{indent}  {key}: {value}\n'
        result += indent[:-2] + '}'
    else:
        result = str(data).lower() if isinstance(data, bool) else 'null' if isinstance(data, type(None)) else str(data)
    return result
