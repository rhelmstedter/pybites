def snake_case_keys(data):
    processed = {}
    for k, v in data.items():
        if isinstance(v, dict):
            processed[k] = snake_case_keys(data[v])
        if isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    processed[k] = snake_case_keys(item)
        try:
            seen = False
            for c in k:
                if c.isupper():
                    k = k.replace(c, "_" + c.lower())
                elif c == "-":
                    k = k.replace(c, "_")
                elif c.isalpha() and k[k.find(c) + 1].isdigit() and not seen:
                    k = k.replace(c, c + "_")
                    seen = True
        except IndexError:
            pass
        processed[k.lstrip("_")] = v
    return processed

