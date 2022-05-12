def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    hex_color = "#"
    for value in rgb:
        if 0 <= value <= 255:
            hex_color += f"{hex(value).lstrip('0x'):02}"
        else:
            raise ValueError
    return hex_color.upper()
