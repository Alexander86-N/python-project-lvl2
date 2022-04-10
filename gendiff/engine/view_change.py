def view_change(value):
    """ Outputs values in the specified form. """
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, type(None)):
        return 'null'
    else:
        return value
