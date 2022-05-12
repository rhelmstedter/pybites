def flatten(list_of_lists):
    if not list_of_lists:
        return list_of_lists
    if isinstance(list_of_lists[0], list) or isinstance(list_of_lists[0], tuple):
        return flatten(list(list_of_lists[0])) + flatten(list(list_of_lists[1:]))
    return list_of_lists[:1] + flatten(list_of_lists[1:])
