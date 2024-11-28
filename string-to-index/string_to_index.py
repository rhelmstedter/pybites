def convert_string_to_index(input_value: str | list[str]) -> list[int]:
    if not input_value:
        return []
    if isinstance(input_value, str):
        input_value = input_value.split(",")
    final = []
    for item in input_value:
        offset = 0
        item = item.replace(" ", "")
        if ":" in item:
            start, end = item.split(":")
            if len(start) == 2:
                offset = 26
                start = start[1]
                end = end[1]
            for i in range(ord(start) - 65 + offset, ord(end) - 65 + offset + 1):
                final.append(i)
        else:
            if len(item) == 2:
                offset = 26
                item = item[1]
            final.append(ord(item) - 65 + offset)
    return final
