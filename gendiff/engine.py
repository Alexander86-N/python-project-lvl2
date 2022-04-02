def converting(file_one, file_two):
    list_one = [_ for _ in file_one.items()]
    list_two = [_ for _ in file_two.items()]
    result = unite(list_one, list_two)
    return create_new_list(result, list_one, list_two)


def unite(arg_one, arg_two):
    """Combines into a list with unique elements."""
    result = []
    result.extend(arg_one)
    result.extend([_ for _ in arg_two if _ not in arg_one])
    return result


def create_new_list(joint_list, list_one, list_two):
    new_list = ['{']
    for item in sorted(joint_list, key=lambda item: item[0]):
        if item not in list_two:
            new_list.append(convert_to_string(item, '-'))
        elif item not in list_one:
            new_list.append(convert_to_string(item, '+'))
        else:
            new_list.append(convert_to_string(item, ' '))
    new_list.append('}')
    return new_list


def convert_to_string(items, symbol, indent=' '):
    item1, item2 = items
    key = symbol + indent + item1.rstrip('"') if isinstance(item1, str)\
        else f'{symbol}{indent}{item1}'
    value = item2.rstrip('"') if isinstance(item2, str)\
        else str(item2).lower() if isinstance(item2, bool) else item2
    return f'{indent * 2}{key}: {value}'
