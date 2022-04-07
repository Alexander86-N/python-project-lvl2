def diff(dirictory1, dirictory2):
    """
    Combines dictionaries and determines the statuses of all keys.
        :param dirictory1: dict
        :param dirictory2: dict
        :return: list
    """
    result = []
    keys = sorted(dirictory1.keys() | dirictory2.keys())
    for key in keys:
        node = {'name': key}
        if key not in dirictory2:
            node['status'] = 'available'
            node['value'] = dirictory1[key]
        elif key not in dirictory1:
            node['status'] = 'added'
            node['value'] = dirictory2[key]
        elif isinstance(dirictory1[key], dict) and\
                isinstance(dirictory2[key], dict):
            node['status'] = 'parent'
            node['children'] = diff(dirictory1[key], dirictory2[key])
        elif dirictory1[key] == dirictory2[key]:
            node['status'] = 'same'
            node['value'] = dirictory1[key]
        else:
            node['status'] = 'changed'
            node['value before'] = dirictory1[key]
            node['value after'] = dirictory2[key]
        result.append(node)
    return result

