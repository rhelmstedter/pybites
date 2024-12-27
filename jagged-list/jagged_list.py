def jagged_list(lst_of_lst: list[list[int]], fillvalue: int = 0) -> list[list[int]]:
    return [lst + [fillvalue] * (len(max(lst_of_lst)) - len(lst)) for lst in lst_of_lst]
