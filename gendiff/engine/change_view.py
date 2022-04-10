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
