from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst:
        return None
    flat_and_sep = []
    for lst in lst_of_lst:
        flat_and_sep += lst
        if lst != lst_of_lst[-1]:
            flat_and_sep.append(sep)
    return flat_and_sep
