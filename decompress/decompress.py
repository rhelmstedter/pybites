from typing import Dict


def decompress(string: str, table: Dict[str, str]) -> str:
    if not any(c in table for c in string):
        return string
    else:
        return decompress("".join(table.get(c, c) for c in string), table)
